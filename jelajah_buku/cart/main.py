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

import grpc_pb.auth_pb2_grpc as auth_pb2_grpc
import grpc_pb.auth_pb2 as auth_pb2
import grpc_pb.cart_pb2_grpc as cart_pb2_grpc
import grpc_pb.cart_pb2 as cart_pb2

# db connection
connection = pymysql.connect(host='localhost',
    user='uas_pwl',
    password='',
    db='pwl',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

# View class
@view_defaults(renderer='json')
class ProfilApi():
    def __init__(self, request: Request):
        self.request = request
        self.authClient = GrpcAuthClient()

    @view_config(route_name='add_to_cart', request_method='POST')
    def add_to_cart(self):
        # request validation
        if not self.request or \
        (
            'id' not in self.request.json_body or \
            'token' not in self.request.json_body
        ):
            return Response('Bad Request', status=400)
        
        # get user id
        user_id = self.authClient.check_if_auth(self.request.json_body['token']).id
        if not user_id:
            return Response('Unauthorized', status=401)
        
        # check if product exist
        with connection.cursor() as cursor:
            sql = "SELECT * FROM produk WHERE id=%s"
            cursor.execute(sql, (self.request.json_body['id']))
            result = cursor.fetchone()
            if not result:
                return Response('Not Found', status=404)
            
            # check if product already in cart
            sql = "SELECT * FROM carts WHERE user_id=%s AND produk_id=%s"
            cursor.execute(sql, (user_id, self.request.json_body['id']))
            result = cursor.fetchone()
            if result:
                # update quantity
                sql = "UPDATE carts SET amount=%s WHERE user_id=%s AND produk_id=%s"
                cursor.execute(sql, (result['amount'] + 1, user_id, self.request.json_body['id']))
                connection.commit()
                return {'message': 'success'}
            
            # add to cart
            sql = "INSERT INTO carts (user_id, produk_id, amount) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user_id, self.request.json_body['id'], 1))
            connection.commit()
            return {'message': 'success'}
        
    @view_config(route_name='remove_from_cart', request_method='POST')
    def remove_from_cart(self):
        # request validation
        if not self.request or \
        (
            'id' not in self.request.json_body or \
            'token' not in self.request.json_body
        ):
            return Response('Bad Request', status=400)
        
        # get user id
        user_id = GrpcAuthClient().check_if_auth(self.request.json_body['token']).id
        if not user_id:
            return Response('Unauthorized', status=401)
        
        # check if product exist
        with connection.cursor() as cursor:
            # check if product already in cart
            sql = "SELECT * FROM carts WHERE user_id=%s AND produk_id=%s"
            cursor.execute(sql, (user_id, self.request.json_body['id']))
            result = cursor.fetchone()
            if result:
                # update quantity
                if result['amount'] > 1:
                    sql = "UPDATE carts SET amount=%s WHERE user_id=%s AND produk_id=%s"
                    cursor.execute(sql, (result['amount'] - 1, user_id, self.request.json_body['id']))
                    connection.commit()
                    return {'message': 'success'}
                else:
                    sql = "DELETE FROM carts WHERE user_id=%s AND produk_id=%s"
                    cursor.execute(sql, (user_id, self.request.json_body['id']))
                    connection.commit()
                    return {'message': 'success'}
            else:
                return {'message': 'Not Found'}
            
    @view_config(route_name='get_cart', request_method='POST')
    def get_cart(self):
        # request validation
        if not self.request or \
        (
            'token' not in self.request.json_body
        ):
            return Response('Bad Request', status=400)
        
        # get user id
        user_id = self.authClient.check_if_auth(self.request.json_body['token']).id
        if not user_id:
            return Response('Unauthorized', status=401)
        
        # get cart
        with connection.cursor() as cursor:
            sql = "SELECT * FROM carts WHERE user_id=%s"
            cursor.execute(sql, (user_id))
            result = cursor.fetchall()
            return result
        
    @view_config(route_name='add_to_cart', request_method='OPTIONS')
    @view_config(route_name='remove_from_cart', request_method='OPTIONS')
    @view_config(route_name='get_cart', request_method='OPTIONS')
    def options(self):
        return Response(status=200)
    
        

class GrpcHandler(cart_pb2_grpc.CartServicer):
    def ClearCart(self, request, context):
        # check if user exist
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (request.user_id))
            result = cursor.fetchone()
            if not result:
                print('User not found')
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('User not found')
                return cart_pb2.ClearCartResponse(message='User not found')
            
            # clear cart
            sql = "DELETE FROM carts WHERE user_id=%s"
            cursor.execute(sql, (request.user_id))
            connection.commit()
            return cart_pb2.ClearCartResponse(success=True)
        
    def GetTotal(self, request, context):
        # check if user exist
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE id=%s"
            cursor.execute(sql, (request.user_id))
            result = cursor.fetchone()
            if not result:
                print('User not found')
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('User not found')
                return cart_pb2.GetTotalResponse(message='User not found')
            
            # get cart
            sql = "SELECT * FROM carts WHERE user_id=%s"
            cursor.execute(sql, (request.user_id))
            result = cursor.fetchall()
            total_price = 0
            print(result)
            for item in result:
                sql = "SELECT * FROM produk WHERE id=%s"
                cursor.execute(sql, (item['produk_id']))
                produk = cursor.fetchone()
                total_price += produk['harga'] * item['amount']
            return cart_pb2.GetTotalResponse(total=total_price)
        


class GrpcAuthClient():
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = auth_pb2_grpc.AuthStub(self.channel)

    def check_if_auth(self, token):
        return self.stub.CheckIfAuth(auth_pb2.Credential(token=token))


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
    config.add_route('add_to_cart', '/add')
    config.add_route('remove_from_cart', '/remove')
    config.add_route('get_cart', '/get')
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    config.scan()
    app = config.make_wsgi_app()

server_grpc = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
cart_pb2_grpc.add_CartServicer_to_server(GrpcHandler(), server_grpc)
server_grpc.add_insecure_port('[::]:50052')
server_grpc.start()

server = make_server('127.0.0.1', 6544, app)
print('Server started at http://127.0.0.1:6544')
server.serve_forever()