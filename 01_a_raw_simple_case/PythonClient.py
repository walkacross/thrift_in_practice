#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:31:34 2019

@author: allen
"""

import sys
sys.path.append('./gen-py')
 
from helloworld import HelloWorld
from helloworld.ttypes import *
from helloworld.constants import *
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    try:
        # Make socket
        transport = TSocket.TSocket('127.0.0.1', 30303)
 
        # Buffering is critical. Raw sockets are very slow
        transport = TTransport.TBufferedTransport(transport)
 
        # Wrap in a protocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
 
        # Create a client to use the protocol encoder
        client = HelloWorld.Client(protocol)
  
        # Connect!
        transport.open()
 
        client.ping()
        print("ping()")
 
        msg = client.sayHello()
        print(msg)
        msg = client.sayMsg(HELLO_YK)
        print(msg)
 
        transport.close()
 
    except Thrift.TException as tx:
        print("%s" % (tx.message))

if __name__ == "__main__":
    main()