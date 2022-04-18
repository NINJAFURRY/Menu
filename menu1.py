import os
import cv2
os.system('tput setaf 5')
location = input("\t\t\tPress 1 for local \n\t\t\tPress 2 for remote \n\t\t\t= ")
os.system('tput setaf 0')
if int(location) == 1:
	os.system("tput setaf 5")
	print("\t\t----------Superhero entry in local---------")
	os.system("tput setaf 0")
	print("""\t\t\t#Press 1 for capture a selfi
		 \t\t#Press 2 for say cheese 
		 \t\t#Press 3 for setup web server
		 \t\t#Press 4 for ssh keygen
		 \t\t#Press 5 for install python
		 \t\t#Press 6 for setup hadoop in local
		 \t\t#Press 7 for setup namenode
		 \t\t#Press 8 for setup datanode
		 \t\t#Press 9 for setup client
		 \t\t#Press 10 for setup jobtracker
		 \t\t#Press 11 for setup tasktracker
		 \t\t#Press 12 for install and start docker 
		 \t\t#Press 13 for run docker image""")
	os.system("tput setaf 3")
	print("\t\tWaiting for you choice:",end=' ' )
	ch = input()
	os.system("tput setaf 0")
	if int(ch) == 1:                                                                               #photo
		os.system("python36 web.py")
                                                                                                    
	elif int(ch) == 2:                                                                            os.system("python36 video.py")
		
	elif int(ch) == 3:
		os.system("yum install httpd")
		os.system('gedit /var/www/html/index.html')
		os.system('systemctl start httpd')
		os.system('iptables -F')
		
	elif int(ch) == 4:
		os.system('ssh-keygen')
		IP = input("Enter friend IP:")
		os.system('ssh-copy-id '+ IP +'')
		
		
	elif int(ch) == 5:
		os.system("yum install python -y")
		os.system('yum install python36-pip -y')
		os.system('pip3 install opencv_python-4.0.0.21-cp36-cp36m-manylinux1_x86_64.whl --no-	index -f .')
	
				
	elif int(ch) == 6:
		os.system("rpm -ivh jdk-8u171-linux-x64.rpm") 
		os.system("export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/")
		os.system("export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH")
		x=("""# .bashrc
		
		# User specific aliases and functions
		
			alias rm='rm -i'
		alias cp='cp -i'
			alias mv='mv -i'
		
		# Source global definitions
		if [ -f /etc/bashrc ]; then
		        . /etc/bashrc
		fi
		export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/
		export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH""")
		f=open("/root/.bashrc","w")
		f.write(x)
		f.close
		os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force")
	
	
		
	elif int(ch) == 7:
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
		
		<!-- Put site-specific property overrides in this file. -->
			
		<configuration>
		<property>
		<name>dfs.name.dir</name>
		<value>/nn</value>
		</property>
		</configuration>""")
		f=open("/etc/hadoop/hdfs-site.xml","w")
		f.write(x)
		f.close
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>fs.default.name</name>
		<value>hdfs://192.168.43.135:9001</value>
			</property>
		</configuration> 
		""")
		f=open("/etc/hadoop/core-site.xml","w")
		f.write(x)
		f.close
		os.system('hadoop namenode -format ')
		os.system('hadoop-daemon.sh start namenode')

	
	elif int(ch) == 8:
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>dfs.data.dir</name>
		<value>/nn</value>
		</property>
		</configuration>""")
		f=open("/etc/hadoop/hdfs-site.xml","w")
		f.write(x)
		f.close
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>fs.default.name</name>
		<value>hdfs://nn.lw.com:9001</value>
		</property>
		</configuration> 
		""")
		f=open("/etc/hadoop/core-site.xml","w")
		f.write(x)
		f.close
		os.system('hadoop-daemon.sh start datanode')



	elif int(ch) == 9:
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>mapred.job.tracker</name>
		<vlaue>jt.lw.com:9002</value>
		</property>
	
		</configuration>""")
		f=open("/etc/hadoop/mapred-site.xml","w")
		f.write(x)
		f.close
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>fs.default.name</name>
		<value>hdfs://nn.lw.com:9001</value>
		</property>
		</configuration> """)
		f=open("/etc/hadoop/core-site.xml","w")
		f.write(x)
		f.close
	elif int(ch) == 10:
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>mapred.job.tracker</name>
		<value>jt.lw.com:9002</value>
		</property>
	
		</configuration>""")
		f=open("/etc/hadoop/mapred-site.xml","w")
		f.write(x)
		f.close
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>fs.default.name</name>
		<value>hdfs://nn.lw.com:9001</value>
		</property>
		</configuration> """)
		f=open("/etc/hadoop/core-site.xml","w")
		f.write(x)
		f.close
		os.system('hadoop-daemon.sh start jobtracker')
	elif int(ch) == 11:
		x=("""<?xml version="1.0"?>
		<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	
		<!-- Put site-specific property overrides in this file. -->
	
		<configuration>
		<property>
		<name>mapred.job.tracker</name>
		<value>jt.lw.com:9002</value>
		</property>
		</configuration> """)
		f=open("/etc/hadoop/core-site.xml","w")
		f.write(x)
		f.close
		os.system("hadoop-daemon.sh start testtracker")
	elif int(ch) == 12:
		os.system('yum install docker-ce')
		os.system('systemctl start docker')
	elif int(ch) == 13:
		OS = input("Enter docker image name :")
		os.system(f'docker load -i {OS}')
		NAME = input("Enter imagename and version :")
		os.system(f'docker run -it {NAME}')
	else:
		os.system('tput setaf 3')
		print('\t\twait jams bond is searching for it')
		os.system('tput setaf 0')
elif int(location) == 2:     #remote command is started
	
	os.system("tput setaf 1")
	print("\t\t----------Superhero entry in remote ---------")
	os.system("tput setaf 0")
	print("""\t\t\t#Press 1 see remotehost live photo
	\t\t#Press 2 for live stream of remote
	\t\t#Press 3 for setup remote web server
	\t\t#Press 4 for remote ssh keygen
	\t\t#Press 5 for remote install python
	\t\t#Press 6 for remote setup hadoop 
	\t\t#Press 7 for remote setup namenode
	\t\t#Press 8 for remote setup datanode
	\t\t#Press 9 for remote setup jobtracker
	\t\t#Press 10 for remote setup client
	\t\t#Press 11 for remote setup tasktracker
	\t\t#Press 12 for remote install and start docker 
	\t\t#Press 13 for remote run docker image""")
	os.system("tput setaf 5")
	print("\t\tWaiting for you choice:",end=' ' )
	ch = input()
	os.system("tput setaf 0")
	if int(ch) == 1:                                                                               #photo
	      IP = input("Enter your IP :")
	      x="scp web.py "+ IP +":/root/Desktop/web.py"
	      y="ssh "+ IP +" python36 /root/Desktop/web.py"
	      z="scp "+ IP +":/root/Desktop/my.png /root/Desktop/my.png"
	      os.system(x)
	      os.system(y)
	      os.system(z)
		
	elif int(ch) == 2:                                                                              #live 		stream
		IP = input("Enter remote IP :")
		v="scp video.py "+ IP +":/tmp/video.py"
		w="ssh -X "+ IP +" python3 /tmp/video.py"
		os.system(v)
		os.system(w)
		
	elif int(ch) == 3:
		IP = input("Enter your IP :")
		os.system(f'ansible-playbook "{IP}," play.yml')
	elif int(ch) == 4:
		IP = input("Enter friend IP :")
		os.system(f'ssh {IP} ssh-keygen')
		os.system(f'ssh {IP} ssh-copy-id ')
		
		
	elif int(ch) == 5:
		IP = input('enter your remote IP :')
		os.system(f'ansible-playbook -i "{IP}," python.yml')
		os.system(f'ssh {IP} yum install python36-pip -y')
	
				
	elif int(ch) == 6:
		IP = input('enter your IP :')
		os.system(f'ansible-playbook -i "{IP}," hadoop.yml')
	
	elif int(ch) == 7:
		IP = input("enter remote IP :")
		os.system(f'ansible-playbook -i "{IP}," namenode.yml')

	elif int(ch) == 8:
		IP = input("enter remote IP :")
		os.system(f'ansible-playbook -i "{IP}," datanode.yml')

	elif int(ch) == 9:
		IP = input('enter your remote IP :')
		os.system(f'ansible-playbook -i "{IP}," jobtracker.yml')
	elif int(ch) == 10:
		IP = input("enter remote IP :")
		os.system(f'ansible-playbook -i "{IP}," client.yml')
	elif int(ch) == 11:
		IP = input ('enter your remote IP :')
		os.system(f"scp testtracker.py {IP}:/tmp/tasktracker.py")
		os.system(f"ssh {IP} python36 /tmp/tasktracker.py")
		os.system(f"ssh {IP} hadoop-daemon.sh start tasktracker")
	elif int(ch) == 12:
		IP = input("enter your remote IP :")
		os.system(f'ansible-playbook "{IP}," docker.yml')
	elif int(ch) == 13:
		IP = input('enter your remote IP :')
		os.system(f'ansible-playbook -i "{IP}," centos.yml')
	elif int(ch) == 14:
		IP = input('Enter your IP :')
		os.system(f'ansible-playbook -i "{IP}," ubuntu.yml')
		os.system('tput setaf 4')
		print('\t\tIts a secret that is not found ')
	else:
		print('be hold at your place this input is not not found')
		os.system('tput setaf 0')
else:
	os.system('tput setaf 4')
	print("\t\tPlease stand by there is comming destriction")
	os.system('tput setaf 0')
