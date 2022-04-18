import os
import netifaces as ni
ni.ifaddresses("enp0s3")
ip = ni.ifaddresses('enp0s3')[ni.AF_INET][0]['addr']

T = input("/t Enter the text you want in your webpage :-")

os.system('yum intsall httpd')
os.system('cd var/www/html')
os.system('touch web.html')
os.system(f'echo "{T}" > /var/www/html/web.html')
os.system('systemctl start httpd')
os.system('systemctl stop firewalld')
os.system(f'firefox http://"{ip}"/web.html')
