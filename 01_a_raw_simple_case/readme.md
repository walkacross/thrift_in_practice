# step1: Writing a .thrift file
After the Thrift compiler is installed you will need to create a .thrift file. This file is an interface definition made up of thrift types and Services. The services you define in this file are implemented by the server and are called by any clients.

# step2: Generate Thrift to source code 
The Thrift compiler is used to generate your Thrift file into source code which is used by the different client libraries and the server you write. To generate the source from a Thrift file run
~~~
thrift --gen <language> <Thrift filename>
~~~
To recursivly generate source code from a Thrift file and all other Thrift files included by it, run
~~~
thrift -r --gen <language> <Thrift filename>
~~~
The sample tutorial.thrift file defines a basic calculator service. This sample calculator service .thrift file includes another file called shared.thrift. Both files will be used to demonstrate how to build a Thrift client and server pair.

# step3: realize the server code
write PythonServer.py
~~~
python PythonServer.py
~~~

# ste4: realize the client code
write PythonClient.py
~~~
python PythonClient.py
~~~
