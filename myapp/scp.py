import pexpect
child = pexpect.spawn('scp -r /data/myproject/myapp root@192.168.2.236')
child.expect('.*password:')
child.sendline('hello')