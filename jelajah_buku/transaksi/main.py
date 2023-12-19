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
class TransaksiApi():
    def __init__(self, request: Request):
        self.request = request
        self.authClient = GrpcAuthClient()
        self.cartClient = GrpcCartClient()

    @view_config(route_name='get_payment', request_method='POST')
    def get_payment(self):
        # request validation
        if not self.request or \
        (
            'token' not in self.request.json_body
        ):
            return Response('Bad Request', status=400)
        
        # get user id
        user_id = self.authClient.check_if_auth(self.request.json_body['token']).id
        if not user_id:
            return {'message': 'Unauthorized'}
        
        # get total price
        print(user_id)
        total = self.cartClient.get_total(user_id).total
        return {'total': total}
    
    @view_config(route_name='do_payment', request_method='POST')
    def do_payment(self):
        # request validation
        if not self.request or \
        (
            'token' not in self.request.json_body
        ):
            return Response('Bad Request', status=400)
        
        # get user id
        user_id = self.authClient.check_if_auth(self.request.json_body['token']).id
        if not user_id:
            return {'message': 'Unauthorized'}
        
        # clear cart
        self.cartClient.clear_cart(user_id)
        
        return {'message': 'OK'}
    
    @view_config(route_name='get_payment', request_method='OPTIONS')
    @view_config(route_name='do_payment', request_method='OPTIONS')

    def options(self):
        return Response('OK', status=200)


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

class GrpcAuthClient():
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = auth_pb2_grpc.AuthStub(self.channel)
    
    def check_if_auth(self, token):
        return self.stub.CheckIfAuth(auth_pb2.Credential(token=token))
    
class GrpcCartClient():
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50052')
        self.stub = cart_pb2_grpc.CartStub(self.channel)
    
    def get_total(self, user_id):
        return self.stub.GetTotal(cart_pb2.GetTotalRequest(user_id=user_id))
    
    def clear_cart(self, user_id):
        return self.stub.ClearCart(cart_pb2.ClearCartRequest(user_id=user_id))

with Configurator() as config:
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('get_payment', '/get')
    config.add_route('do_payment', '/pay')
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    config.scan()
    app = config.make_wsgi_app()

server_grpc = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
server_grpc.add_insecure_port('[::]:50055')
server_grpc.start()

server = make_server('127.0.0.1', 6547, app)
print('Server started at http://127.0.0.1:6547')
server.serve_forever()