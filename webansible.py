import os

I=input("Enter the IP  of the agent or target node -->> ")
U=input("Enter the username of your target node -->> ")
P=input("Enter the password of your target node -->> ")
T=input("Enter the text you want in your webpage -->> ")

os.system('touch cp.txt')
os.system(f'echo ""{I}" ansible_user="{U}" ansible_ssh_pass="{P}" ansible_connection=ssh" >> /cp.txt')
os.system('cd /etc/ansible')
os.system(f'echo "[defaults]" > /etc/ansible/ansible.cfg')
os.system(f'echo "inventory=/cp.txt" >> /etc/ansible/ansible.cfg')
os.system(f'echo "host_key_checking=false" >> /etc/ansible/ansible.cfg')
os.system('ansible all -m package -a "name=httpd state=present"')
os.system('cd /var/www/html/')
os.system('touch ansible.html')
os.system(f'echo "{T}" > /var/www/html/ansible.html')
os.system('ansible all -m copy -a "src=ansible.html dest=/var/www/html"')
os.system('ansible all -m service -a "name=httpd state=started"')
