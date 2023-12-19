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

import grpc_pb.produk_pb2_grpc as produk_pb2_grpc
import grpc_pb.produk_pb2 as produk_pb2
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
class ProdukApi():
    def __init__(self, request: Request):
        self.request = request

    @view_config(route_name='store_produk', request_method='POST')
    def store_produk(self):
        # request validation
        if not self.request or \
        (
        'judul' not in self.request.json_body or \
        'penulis' not in self.request.json_body or \
        'deskripsi' not in self.request.json_body or \
        'harga' not in self.request.json_body or \
        'kategori' not in self.request.json_body or \
        'gambar' not in self.request.json_body
        ):
            return Response('Bad Request', status=400)
        with connection.cursor() as cursor:
            sql = "INSERT INTO produk (judul, penulis, deskripsi, harga, kategori_id, gambar) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                self.request.json_body['judul'],
                self.request.json_body['penulis'],
                self.request.json_body['deskripsi'],
                self.request.json_body['harga'],
                self.request.json_body['kategori'],
                self.request.json_body['gambar']
            ))
            connection.commit()
            return {'message': 'Created', 'id': cursor.lastrowid}
        
    @view_config(route_name='update_produk', request_method='POST')
    def update_produk(self):
        # request validation
        if not self.request:
            return Response('Bad Request', status=400)
        with connection.cursor() as cursor:
            sql = "UPDATE produk SET judul=%s, penulis=%s, deskripsi=%s, harga=%s, kategori_id=%s, gambar=%s WHERE id=%s"
            cursor.execute(sql, (
                self.request.json_body['judul'],
                self.request.json_body['penulis'],
                self.request.json_body['deskripsi'],
                self.request.json_body['harga'],
                self.request.json_body['kategori'],
                self.request.json_body['gambar'],
                self.request.json_body['id']
            ))
            connection.commit()
            return {'message': 'Updated'}
        
    @view_config(route_name='delete_produk', request_method='POST')
    def delete_produk(self):
        # request validation
        if not self.request or 'id' not in self.request.json_body:
            return Response('Bad Request', status=400)
        with connection.cursor() as cursor:
            # check if produk exist
            sql = "SELECT * FROM produk WHERE id=%s"
            cursor.execute(sql, (self.request.json_body['id']))
            result = cursor.fetchone()
            if not result:
                return {'message': 'Not Found'}
            sql = "DELETE FROM produk WHERE id=%s"
            cursor.execute(sql, (self.request.json_body['id']))
            connection.commit()
            return {'message': 'Deleted'}

    @view_config(route_name='get_produk', request_method='GET')
    def get_produk(self):
        """ Get specific produk by id from params """
        # request validation
        if not self.request or ('id' not in self.request.matchdict):
            return Response('Bad Request', status=400)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM produk WHERE id=%s"
            cursor.execute(sql, (self.request.matchdict['id']))
            result = cursor.fetchone()
            if result:
                return result
            else:
                return {'message': 'Not Found'}
            
    @view_config(route_name='get_produk_by_kategori', request_method='GET')
    def get_produk_by_kategori(self):
        """ Get specific produk by kategori from params """
        # request validation
        if not self.request or ('kategori' not in self.request.matchdict):
            return Response('Bad Request', status=400)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM produk WHERE kategori_id=%s"
            cursor.execute(sql, (self.request.matchdict['kategori']))
            result = cursor.fetchall()
            if result:
                return result
            else:
                return {'message': 'Not Found'}
            
    @view_config(route_name='get_all_produk', request_method='GET')
    def get_all_produk(self):
        """ Get all produk with pagination """
        # request validation
        if not self.request or \
        (
        'page' not in self.request.matchdict or \
        'limit' not in self.request.matchdict
        ):
            # default value
            self.request.matchdict['page'] = 1
            self.request.matchdict['limit'] = 10
        with connection.cursor() as cursor:
            sql = "SELECT * FROM produk LIMIT %s OFFSET %s"
            cursor.execute(sql, (
                int(self.request.matchdict['limit']),
                (int(self.request.matchdict['page']) - 1) * int(self.request.matchdict['limit'])
            ))
            result = cursor.fetchall()
            if result:
                return result
            else:
                return {'message': 'Not Found'}
            
    @view_config(route_name='store_produk', request_method='OPTIONS')
    @view_config(route_name='update_produk', request_method='OPTIONS')
    @view_config(route_name='delete_produk', request_method='OPTIONS')
    @view_config(route_name='get_produk', request_method='OPTIONS')
    @view_config(route_name='get_produk_by_kategori', request_method='OPTIONS')
    @view_config(route_name='get_all_produk', request_method='OPTIONS')
    def options(self):
        return Response('OK', status=200)
            
class GrpcHandler(produk_pb2_grpc.ProdukServicer):
    def GetPrice(self, request, context):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM produk WHERE id=%s"
            cursor.execute(sql, (request.id))
            result = cursor.fetchone()
            if result:
                return produk_pb2.PriceResponse(price=result['harga'])
            else:
                return produk_pb2.PriceResponse(price=0)
            
    def GetPrices(self, request_iterator, context):
        total_price = 0
        with connection.cursor() as cursor:
            for request in request_iterator:
                sql = "SELECT * FROM produk WHERE id=%s"
                cursor.execute(sql, (request.id))
                result = cursor.fetchone()
                if result:
                    total_price += result['harga']
        return produk_pb2.PriceResponse(price=total_price)

class GrpcAuthClient():
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = auth_pb2_grpc.AuthStub(self.channel)

    def check_if_auth(self, token):
        return self.stub.CheckIfAuth(auth_pb2.CheckIfAuthRequest(token=token))


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
    config.add_route('store_produk', '/add')
    config.add_route('update_produk', '/edit')
    config.add_route('delete_produk', '/delete')
    config.add_route('get_produk', '/get/{id}')
    config.add_route('get_produk_by_kategori', '/get/kategori/{kategori}')
    config.add_route('get_all_produk', '/get/all/{page}/{limit}')
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    config.scan()
    app = config.make_wsgi_app()

server_grpc = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
produk_pb2_grpc.add_ProdukServicer_to_server(GrpcHandler(), server_grpc)
server_grpc.add_insecure_port('[::]:50054')
server_grpc.start()

server = make_server('127.0.0.1', 6546, app)
print('Server started at http://127.0.0.1:6546')
server.serve_forever()