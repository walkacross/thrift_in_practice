#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:21:05 2019

@author: allen
"""

import sys
sys.path.append('./gen-py')
  
from helloworld import HelloWorld
from helloworld.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket

class HelloWorldHandler:
    def __init__(self):
        self.log = {}
 
    def ping(self):
        print("ping()")
 
    def sayHello(self):
        print("sayHello()")
        return "say hello from " + socket.gethostbyname(socket.gethostname())
 
    def sayMsg(self, msg):
        print("sayMsg(" + msg + ")")
        return "say " + msg + " from " + socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    handler = HelloWorldHandler()
    processor = HelloWorld.Processor(handler)
    transport = TSocket.TServerSocket('127.0.0.1',30303)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    
    print("Starting python server...")
    server.serve()
    print("done!")