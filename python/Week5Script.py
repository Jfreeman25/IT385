#!/usr/bin/env python3
# Login and create users, create web servers, and create databases
# By Joseph Freeman
# Date: 02/05/2021

from pexpect import pxssh
allIPs = ['192.168.0.111','192.168.0.112', '192.168.0.121', '192.168.0.122']
for address in allIPs:
    # Connect to remote system
    session = pxssh.pxssh()
    session.login(address,'justincase', 'Password01')
    print("SSH login successful")

    # Send commands
    session.sendline('sudo adduser egoad')
    session.prompt()
    session.sendline('Password01')
    session.prompt()
    session.sendline('RubberDuck!')
    session.prompt()
    session.sendline('RubberDuck!')
    session.prompt()
    session.sendline('')
    session.sendline('')
    session.sendline('')
    session.sendline('')
    session.sendline('')
    session.prompt()
    session.sendline('y')
    print('User has been created.')


# Create and start web servers
webIPs = ['192.168.0.111', '192.168.0.112']
for addresses in webIPs: 
    session = pxssh.pxssh()
    session.login(addresses,'justincase', 'Password01' )
    print("SSH login successful")

    session.sendline('sudo apt update -y')
    session.prompt()
    session.sendline('Password01')
    session.prompt()
    session.sendline('sudo apt-get install apache2')
    session.prompt()
    session.sendline('y')
    session.prompt()
    print('Apache2 successfully installed.')
    session.sendline('sudo systemctl start apache2.service')
    session.prompt()
    print('Apache2 server is running.')
    session.sendline('sudo systelctl enable apache2')
    print('Apache2 set to start after reboot.')

# Create and configure databases
dbIPs = ['192.168.0.121', '192.168.0.122']
for addresses in dbIPs: 
    session = pxssh.pxssh()
    session.login(addresses,'justincase', 'Password01' )
    print("SSH login successful")

    session.sendline('sudo apt update -y')
    session.prompt()
    session.sendline('Password01')
    session.prompt()
    session.sendline('sudo apt upgrade')
    session.prompt()
    session.sendline('y')
    session.prompt()
    session.sendline('sudo apt install mysql-server')
    session.prompt()
    session.sendline('y')
    session.prompt()
    print('Mysql installed.')
    session.sendline('sudo systemctl start mysql')
    session.prompt()
    session.sendline('sudo systemctl enable mysql-server')
    print('Mysql started and configured.')
    
