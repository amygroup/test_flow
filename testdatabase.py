from clickhouse_driver import Client
from testflows.core import *

from testflows.asserts import *
def open_connection(host):

    client=Client(host='localhost')
    return client
def execute_query(client,query):    
    x=client.execute(query)
    print(x)
    return x
#r=open_connection(host="local host")
#x=execute_query(client=r,query="select 1")
with Test("check clickhouse query" ):
        r=open_connection(host="local host")    
        x=execute_query(client=r,query="select 1")
        
        with Then("query result"):
            assert (1,) in x,ok
            
