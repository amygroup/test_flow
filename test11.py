
from testflows.core import *
from testflows.connect import Shell
from testflows.asserts import error
with Test("check 'ls -author' behaviour" ):
        with Shell() as bash:
            cmd=bash('ls -l  --author')
            with When("no auther name"):
                
                assert cmd.exitcode==2,error()
                         
