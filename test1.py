
        
from testflows.core import *
from testflows.connect import Shell
from testflows.asserts import *
with Test("check 'ls -a -all' behaviour" ):
        with Shell() as bash:
            cmd=bash('ls -a -all')
        
        with Then("ls -a -all,expect behaviour"):
                assert cmd.exitcode==0,ok
        with When("no file start with ."):

                #assert "ls -a -all: no file  starting with ." in cmd.output.error()
                assert cmd.exitcode==2,error()
