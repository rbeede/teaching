#!/bin/bash

# © 2023 Rodney Beede

set -x


# Ubuntu tested
apt-get update
apt-get install -y curl netcat git

##################################

apt-get install -y python3 python3-paramiko python3-pip

# pip install paramiko


cd /tmp/

git clone https://github.com/cheeseandcereal/fake-ssh.git

cd /tmp/fake-ssh/

python3 ./fake_ssh.py &


########################

cd /tmp/

nc -k -l  -vvv -n -p 3389 &


########################


cd /tmp/

curl -OL 'https://raw.githubusercontent.com/rbeede/teaching/main/security/simplehttpserver.py'

python3 /tmp/simplehttpserver.py 8080  &
