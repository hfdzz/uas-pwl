# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import kategori_pb2 as kategori__pb2


class KategoriStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetKategori = channel.unary_unary(
                '/proto.Kategori/GetKategori',
                request_serializer=kategori__pb2.KategoriRequest.SerializeToString,
                response_deserializer=kategori__pb2.KategoriResponse.FromString,
                )


class KategoriServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetKategori(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KategoriServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetKategori': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKategori,
                    request_deserializer=kategori__pb2.KategoriRequest.FromString,
                    response_serializer=kategori__pb2.KategoriResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.Kategori', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Kategori(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetKategori(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Kategori/GetKategori',
            kategori__pb2.KategoriRequest.SerializeToString,
            kategori__pb2.KategoriResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
