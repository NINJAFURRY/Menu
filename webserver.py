import os
import socket

Soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP=Soc.getsockname()[0]
T=input("/t Enter the text you want in your webpage -->>")


os.system('yum install httpd')
os.system('cd /var/www/html/')
os.system('touch web.html')
os.system(f'echo "{T}" > /var/www/html/web.html')
os.system('systemctl start httpd')
os.system('systemctl stop firewalld')
os.system(f'firefox http://"{IP}"/web.html')

