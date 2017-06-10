#!/usr/bin/python
import pexpect
import sys
import os
child=pexpect.spawn('ssh root@192.168.0.179')
#fout=file('mylog.txt','w')
#child.logfile=fout
index=child.expect(['Are you sure you want to continue connecting (yes/no)?','password:'])
if (index == 0):
    child.sendline("yes")
    child.expect("password:")
    child.sendline("123456")
else:
    child.sendline("123456")
child.expect('#')
child.sendline('cd /home && touch hellokiii.txt')
child.expect('#')

