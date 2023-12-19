from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.events import NewRequest
from concurrent import futures
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.view import notfound_view_config
from pyramid.response import Response
from pyramid.request import Request
import pymysql
import random
import string
import time 
import grpc

import pyramid.httpexceptions as exc

import grpc_pb.auth_pb2_grpc as auth_pb2_grpc
import grpc_pb.auth_pb2 as auth_pb2

# db connection
connection = pymysql.connect(host='localhost',
    user='uas_pwl',
    password='',
    db='pwl',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

# View class
@view_defaults(renderer='json')
class AuthApi():
    def __init__(self, request: Request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {}

    @view_config(route_name='auth', request_method='POST')
    def auth(self):
        print(self.request.json_body)
        # request validation
        if not self.request or 'email' not in self.request.json_body or 'password' not in self.request.json_body or 'token' not in self.request.json_body:
            return Response('Bad Request', status=400)
        credential = self.request.json_body
        with connection.cursor() as cursor:
            # check if has token
            if 'token' in credential and credential['token'] != '':
                print('has token')
                # check if token valid
                sql = "SELECT * FROM users WHERE token=%s"
                cursor.execute(sql, (credential['token']))
                result = cursor.fetchone()
                if result:
                    # return user id
                    return {'id': result['id']}
                else:
                    return Response('Unauthorized', status=401)

            print('no token')
            # check if email and password valid
            sql = "SELECT * FROM users WHERE email=%s AND password=%s"
            cursor.execute(sql, (credential['email'], credential['password']))
            result = cursor.fetchone()
            # check if token is not empty
            if result and result['token'] != '':
                return {'id': result['id'], 'token': result['token']}
            if result:
                # create random token (16-char string)
                token = generate_token()
                # update token
                sql = "UPDATE users SET token=%s WHERE id=%s"
                cursor.execute(sql, (token, result['id']))
                connection.commit()

                # return user id
                return {'id': result['id'], 'token': token}
            else:
                return {'message': 'Unauthorized'}
                

    @view_config(route_name='register', request_method='POST')
    def register(self):
        # request validation
        if not self.request or 'email' not in self.request.json_body or 'password' not in self.request.json_body or 'nama' not in self.request.json_body:
            return Response('Bad Request', status=400)
        credential = self.request.json_body
        with connection.cursor() as cursor:
            # check if email already registered
            sql = "SELECT * FROM users WHERE email=%s"
            cursor.execute(sql, (credential['email']))
            result = cursor.fetchone()
            if result:
                return Response('Email already registered', status=409)
            
            # get last inserted id
            sql = "SELECT id FROM users ORDER BY id DESC LIMIT 1"
            cursor.execute(sql)
            result = cursor.fetchone()
            last_id = result['id'] if result else 0

            # insert new user
            sql = "INSERT INTO users (id, email, password, nama) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (last_id + 1, credential['email'], credential['password'], credential['nama']))
            connection.commit()

            token = generate_token()

            return {'id': cursor.lastrowid, 'token': token}
    
    @view_config(route_name='get_auth', request_method='POST')
    def get_auth(self):
        # request validation
        if not self.request or 'id' not in self.request.json_body:
            return Response('Bad Request', status=400)
        credential = self.request.json_body
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (credential['id']))
            result = cursor.fetchone()
            if result:
                # return user id, email, and nama
                return {'id': result['id'], 'email': result['email'], 'nama': result['nama']}
            else:
                return {'message': 'Unauthorized'}

    @view_config(route_name='logout', request_method='POST')
    def logout(self):
        # request validation
        if not self.request or 'token' not in self.request.json_body:
            return Response('Bad Request', status=400)
        credential = self.request.json_body
        if not credential['token'] or credential['token'] == '':
            return {'message': 'Unauthorized'}
        with connection.cursor() as cursor:
            # get user id by token
            print(credential['token'])
            sql = "SELECT id FROM users WHERE token=%s"
            cursor.execute(sql, (credential['token']))
            result = cursor.fetchone()
            if result:
                print(result['id'])
                # update token to empty string
                sql = "UPDATE users SET token='' WHERE id=%s"
                cursor.execute(sql, (result['id']))
                connection.commit()
                return {'message': 'OK'}
            else:
                return {'message': 'Unauthorized'}
        
    @view_config(route_name='auth', request_method='OPTIONS')
    @view_config(route_name='register', request_method='OPTIONS')
    @view_config(route_name='get_auth', request_method='OPTIONS')
    @view_config(route_name='logout', request_method='OPTIONS')
    def options(self):
        return Response(status=200)


    # @view_defaults(method='OPTIONS')
    # def options(self):
    #     return Response(status=200)
        

    # @notfound_view_config()
    # def notfound(request):
    #     request.response.status = 404
    #     return {}
    

class GrpcHandler(auth_pb2_grpc.AuthServicer):
    def GetAuthByID(self, request, context):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (request.id))
            result = cursor.fetchone()
            if result:
                return auth_pb2.UserData(id=result['id'], email=result['email'], nama=result['nama'])
            else:
                return auth_pb2.UserData()

    def GetAuthByToken(self, request, context):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE token=%s"
            cursor.execute(sql, (request.token))
            result = cursor.fetchone()
            if result:
                return auth_pb2.UserData(id=result['id'], email=result['email'], nama=result['nama'])
            else:
                return auth_pb2.UserData()

    def CheckIfAuth(self, request, context):
        with connection.cursor() as cursor:
            # print(request)
            # check if token is not empty
            if request.token != '':
                # check if token valid
                sql = "SELECT * FROM users WHERE token=%s"
                cursor.execute(sql, (request.token))
                result = cursor.fetchone()
                if result:
                    return auth_pb2.IsAuth(isAuth=True, id=result['id'])
                else:
                    return auth_pb2.IsAuth(isAuth=False)
            else:
                # check if email and password valid
                sql = "SELECT * FROM users WHERE email=%s AND password=%s"
                cursor.execute(sql, (request.email, request.password))
                result = cursor.fetchone()
                if result:
                    return auth_pb2.IsAuth(isAuth=True, id=result['id'])
                else:
                    return auth_pb2.IsAuth(isAuth=False)

def generate_token():
    # generate 16-char string toke with 4 random char and 12 timestamp
    current_time = time.time()
    current_time = str(current_time).replace('.', '')
    random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return random_char + current_time[:12]
    


def add_cors_headers_response_callback(event):
    """
        Add CORS headers to every response.
    """
    def cors_headers(request, response):
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)

with Configurator() as config:
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/auth')
    config.add_route('register', '/register')
    config.add_route('get_auth', '/get_auth')
    config.add_route('logout', '/logout')
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    config.scan()
    app = config.make_wsgi_app()

server_grpc = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
auth_pb2_grpc.add_AuthServicer_to_server(GrpcHandler(), server_grpc)
server_grpc.add_insecure_port('[::]:50051')
server_grpc.start()

server = make_server('127.0.0.1', 6543, app)
print('Server started at http://127.0.0.1:6543')
server.serve_forever()