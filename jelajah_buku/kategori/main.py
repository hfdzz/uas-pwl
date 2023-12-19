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

import grpc_pb.kategori_pb2_grpc as kategori_pb2_grpc
import grpc_pb.kategori_pb2 as kategori_pb2

# db connection
connection = pymysql.connect(host='localhost',
    user='uas_pwl',
    password='',
    db='pwl',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

# View class
@view_defaults(renderer='json')
class KategoriApi():
    def __init__(self, request: Request):
        self.request = request

    @view_config(route_name='get_kat_by_id', request_method='GET')
    def get_kategori_by_id(self):
        print('kat_id')
        # request validation
        if not self.request or ('id' not in self.request.matchdict):
            return Response('Bad Request', status=400)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM kategori WHERE id=%s"
            cursor.execute(sql, (self.request.matchdict['id']))
            result = cursor.fetchone()
            if result:
                return {'kategori': result['kategori'], 'text': result['text']}
            else:
                return {'message': 'Not Found'}
        
    @view_config(route_name='get_kat_text', request_method='GET')
    def get_text_kategori(self):
        # request validation
        if not self.request or ('id' not in self.request.matchdict):
            return Response('Bad Request', status=400)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM kategori WHERE id=%s"
            cursor.execute(sql, (self.request.matchdict['id']))
            result = cursor.fetchone()
            if result:
                return {'text': result['text']}
            else:
                return Response('Not Found', status=404)
            
    @view_config(route_name='get_kat_by_id', request_method='OPTIONS')
    def options(self):
        return Response('OK', status=200)

class GrpcHandler(kategori_pb2_grpc.KategoriServicer):
    def GetKategori(self, request, context):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM kategori WHERE id=%s"
            cursor.execute(sql, (request.id))
            result = cursor.fetchone()
            if result:
                return kategori_pb2.KategoriResponse(kategori=result['kategori'], text=result['text'])
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details('Not Found')
                return kategori_pb2.KategoriResponse()

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
    # config.add_route('home', '/')
    config.add_route('get_kat_by_id', '/kategori/{id}')
    config.add_route('get_kat_text', '/kategori/{id}/text')
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    config.scan()
    app = config.make_wsgi_app()

server_grpc = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
kategori_pb2_grpc.add_KategoriServicer_to_server(GrpcHandler(), server_grpc)
server_grpc.add_insecure_port('[::]:50053')
server_grpc.start()

server = make_server('127.0.0.1', 6545, app)
print('Server started at http://127.0.0.1:6545')
server.serve_forever()
