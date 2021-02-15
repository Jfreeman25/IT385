#!/bin/bash

#Add users
ansible -i inventory.txt linux -m user -a 'name=egoad password="$5$Bx9OQi9jCnNVR0$hIwnfi2DuxP3AXxyyb.cMSbqO9CSq5c/U3eA1vkI4a3"' -b 

#Configure web servers
ansible -i inventory.txt web -m apt -a 'name=apache2 state=present' -b
ansible -i inventory.txt web -m ansible.builtin.service -a 'name=apache2 state=started' -b

#Configure databases
ansible -i inventory.txt db -m ansible.builtin.yum -a 'name=mariadb-server state=present' -b
ansible -i inventory.txt db -m ansible.builtin.service -a 'name=mariadb state=started' -b