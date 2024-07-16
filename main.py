from public_search.functions import get_company_details
from data.companies import btw_nr, companies


def run():
    print("public search works")
    company_details = get_company_details(btw_nr)
    print(company_details)


def start_server():
    import os
    import socket

    s = socket.socket()
    # host = socket.gethostname()
    host = '0.0.0.0'
    port = 8080
    s.bind((host, port))
    print("Server started at: ", host)
    s.listen(1)
    conn, addr = s.accept()
    print(addr, "connected")

    # CLIENT
    import os
    import socket

    s = socket.socket()
    port = 8080
    host = "YOUR DESKTOP ID"


run()

start_server()
