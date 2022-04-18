import os
import getpass
import socket
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
passwd = getpass.getpass("Enter your password👉")
if passwd != "redhat":
    print("password incorrect")
    exit()

location = input("For local press 1 or press 2 for remote==>")
os.system('figlet -f slant "ARTH Learner" | lolcat')
os.system("python3 menuindex.py | lolcat")

if int(location) == 1:
    ch = input("Enter your number==>")
    if int(ch) == 1:
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

    elif int(ch) == 2:
        NNip=input("Enter Name-Node IP ...>>> ")
        
        os.system('rm -rf /namenode')
        os.system('mkdir /namenode')
        os.system('cp /root/fileUpdate/core-site.xml  /etc/hadoop/core-site.xml')
        os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
        os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
        os.system('echo "<name>fs.default.name</name>"  >> /etc/hadoop/core-site.xml')
        os.system(f'echo "<value>hdfs://{NNip}:9001</value>" >> /etc/hadoop/core-site.xml')
        os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
        os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
        os.system('echo "   " >> /etc/hadoop/core-site.xml')
        
        os.system('cp /root/fileUpdate/hdfs-site.xml  /etc/hadoop/hdfs-site.xml')
        
        os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "<name>dfs.name.dir</name>"  >> /etc/hadoop/hdfs-site.xml')
        os.system(f'echo "<value>/namenode</value>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "</configuration>" >> /etc/hadoop/hdfs-site.xml')
        
        os.system('echo "   " >> /etc/hadoop/hdfs-site.xml')
        
        os.system('hadoop namenode -format -force')
        os.system('hadoop-daemon.sh start namenode')
    elif int(ch) == 3:
        NNip=input("Enter Name-Node IP ...>>> ")
        
        os.system('rm -rf /datanode')
        os.system('mkdir /datanode')
        os.system('cp /root/fileUpdate/core-site.xml  /etc/hadoop/core-site.xml')
        
        os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
        os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
        os.system('echo "<name>fs.default.name</name>"  >> /etc/hadoop/core-site.xml')
        os.system(f'echo "<value>hdfs://{NNip}:9001</value>" >> /etc/hadoop/core-site.xml')
        os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
        os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
        
        os.system('echo "   " >> /etc/hadoop/core-site.xml')
        
        
        os.system('cp /root/fileUpdate/hdfs-site.xml  /etc/hadoop/hdfs-site.xml')
        
        os.system('echo "<configuration>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "<property>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "<name>dfs.data.dir</name>"  >> /etc/hadoop/hdfs-site.xml')
        os.system(f'echo "<value>/datanode</value>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "</property>" >> /etc/hadoop/hdfs-site.xml')
        os.system('echo "</configuration>" >> /etc/hadoop/hdfs-site.xml')
        
        os.system('echo "   " >> /etc/hadoop/hdfs-site.xml')
        os.system('hadoop-daemon.sh start datanode')
    elif int(ch) == 4:
        NNip=input("Enter Name-Node IP ...>>> ")
        
        os.system('cp /root/fileUpdate/core-site.xml  /etc/hadoop/core-site.xml')
        
        os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
        os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
        os.system('echo "<name>fs.default.name</name>"  >> /etc/hadoop/core-site.xml')
        os.system(f'echo "<value>hdfs://{NNip}:9001</value>" >> /etc/hadoop/core-site.xml')
        os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
        os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')
        
        os.system('echo "   " >> /etc/hadoop/core-site.xml')

    elif int(ch) == 5:
        instance_id = input("instance_id")
        os.system("aws ec2 start-instances --instance-ids {0}".format(instance_id) )
    elif int(ch) == 6:
        instance_id = input("instance_id")
        volume_id = input("volume_id")
        os.system("aws ec2 attach-volume --device /dev/sdf --instance-id {0} --volume-id {1}".format(instance_id,volume_id) )
    elif int(ch) == 7:
        ff=input("Enter the location of .csv file-->")
        data=pd.read_csv(ff)
        x=data['YearsExperience']
        y=data['Salary']
        print(data)
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        x=x.values.reshape(-1,1)
        model.fit(x,y)
        arr=int(input('Enter your exprience-->'))
        v=np.array(arr)
        newarr=v.reshape(-1,1)
        pp=model.predict(newarr)
        b=model.intercept_
        print(f"Your Baised of this model is {b}")
        c=model.coef_
        print(f"Your Weight of this model is {c}")
        y = b+(c*newarr)
        print(y)
        print(f"Estimated salary would be {y}")


    elif int(ch) == 8:
        pp=input('Enter your file path .csv format')
        data=pd.read_csv(pp)
        print(data)
        x=data['YearsExperience']
        y=data['Salary']
        plt.scatter(x,y,alpha=0.5)
        plt.plot(x,y,marker="o")
        plt.title('Graph of Salary prediction')
        plt.show()
    elif int(ch) == 9:
        os.system("fdisk -l")
        x=input("Enter your partation name==>")
        os.system("pvcreate "+x+"")
        os.system("pvdisplay "+x+"")
        y=input("Enter your volume group name==>")
        os.system("vgcreate "+y+" "+x+"")
        os.system("vgdisplay "+y+"")
        a=input("Enter the name of Logical volume==>")
        z=input("Enter the size you want to create Logical volume in MB==>")
        os.system("lvcreate --name "+a+" --size "+z+" "+y+"")
    elif int(ch) == 10:
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
    else:
        print("Nothing found what you are looking")
elif int(location) == 2:
    ch = input("Enter your number==>")
    IP = input("Input your remote system IP ==>")
    if int(ch) == 1:
        os.system("scp webserver.py "+IP+":/tmp/webserver.py")
        os.system("ssh "+IP+" python3 /tmp/webserver.py")
    elif int(ch) == 2:
       os.system("scp NNconfig.py "+IP+":/tmp/NN.py")
       os.system("ssh "+IP+" python3 /tmp/NN.py")

    elif int(ch) == 3:
        os.system("scp DNconfig.py "+IP+":/tmp/DN.py")
        os.system("ssh "+IP+" python3 /tmp/DN.py")

    elif int(ch) == 4:
        os.system("scp CNconfig.py "+IP+":/tmp/CN.py")
        os.system("ssh "+IP+" python3 /tmp/CN.py")

    elif int(ch) == 5:
        os.system("scp awslaunchinstance.py "+IP+":/tmp/aws.py")
        os.system("ssh "+IP+" python3 /tmp/aws.py")

    elif int(ch) == 6:
        os.system("scp ebsattaching.py "+IP+":/tmp/ebs.py")
        os.system("ssh "+IP+" python3 /tmp/ebs.py")

    elif int(ch) == 7:
        os.system("scp psalery.py "+IP+":/tmp/psalery.py")
        os.system("ssh "+IP+" python3 /tmp/psalery.py")

    elif int(ch) == 8:
        os.system("scp graph.py "+IP+":/tmp/graph.py")
        os.system("ssh "+IP+" python3 /tmp/graph.py")

    elif int(ch) == 9:
        os.system("scp lvm.py "+IP+":/tmp/lvm.py")
        os.system("ssh "+IP+" python3 /tmp/lvm.py")

    elif int(ch) == 10:
        os.system("scp webansible.py "+IP+":/tmp/ans.py")
        os.system("ssh "+IP+" python3 /tmp/ans.py")
    else:
        print("Nothing found what you are looking")
else:
    print("Your system crash")
