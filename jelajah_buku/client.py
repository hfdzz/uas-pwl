import grpc
from grpc_pb import auth_pb2_grpc as auth_pb2_grpc
from grpc_pb import auth_pb2 as auth_pb2
from grpc_pb import cart_pb2_grpc as cart_pb2_grpc
from grpc_pb import cart_pb2 as cart_pb2
from grpc_pb import kategori_pb2_grpc as kategori_pb2_grpc
from grpc_pb import kategori_pb2 as kategori_pb2
from grpc_pb import produk_pb2_grpc as produk_pb2_grpc
from grpc_pb import produk_pb2 as produk_pb2

def runAuth():
    print("== AUTH ==")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = auth_pb2_grpc.AuthStub(channel)
        response = stub.CheckIfAuth(auth_pb2.Credential(token='CUU7E5UKZZNF14K8'))
        print(response)

def runCart():
    print("== CART ==")
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = cart_pb2_grpc.CartStub(channel)
        # response = stub.ClearCart(cart_pb2.ClearCartRequest(user_id=2))
        # print(response)
        print(stub.GetTotal(cart_pb2.GetTotalRequest(user_id=2)))

def prices_gen():
    for i in range(1, 3):
        yield produk_pb2.PriceRequest(id=i)

def runProduk():
    print("== PRODUK ==")
    with grpc.insecure_channel('localhost:50054') as channel:
        stub = produk_pb2_grpc.ProdukStub(channel)
        response = stub.GetPrice(produk_pb2.PriceRequest(id=3))
        print(response)
        print(stub.GetPrices(prices_gen()))

if __name__ == '__main__':
    runAuth()
    runCart()
    runProduk()