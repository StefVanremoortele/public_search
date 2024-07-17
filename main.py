from concurrent import futures
import logging
import grpc

import public_search_pb2
import public_search_pb2_grpc

from public_search.functions import get_company_details
from data.companies import btw_nr, companies


class Greeter(public_search_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return public_search_pb2.HelloReply(message="Hello, %s!" % request.name)


def run():
    print("public search works")
    company_details = get_company_details(btw_nr)
    print(company_details)


# def start_server():
#     import os
#     import socket

#     s = socket.socket()
#     # host = socket.gethostname()
#     host = '0.0.0.0'
#     port = 8080
#     s.bind((host, port))
#     print("Server started at: ", host)
#     s.listen(1)
#     conn, addr = s.accept()
#     print(addr, "connected")

#     # CLIENT
#     import os
#     import socket

#     s = socket.socket()
#     port = 8080
#     host = "YOUR DESKTOP ID"


run()

# start_server()


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    public_search_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    # logging.basicConfig()
    logging.basicConfig(level=logging.INFO)
    serve()
