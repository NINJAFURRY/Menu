import os
import subprocess

NNip=input("Enter Name-Node IP ...>>> ")


os.system('cp /root/fileUpdate/core-site.xml  /etc/hadoop/core-site.xml')

os.system('echo "<configuration>" >> /etc/hadoop/core-site.xml')
os.system('echo "<property>" >> /etc/hadoop/core-site.xml')
os.system('echo "<name>fs.default.name</name>"  >> /etc/hadoop/core-site.xml')
os.system(f'echo "<value>hdfs://{NNip}:9001</value>" >> /etc/hadoop/core-site.xml')
os.system('echo "</property>" >> /etc/hadoop/core-site.xml')
os.system('echo "</configuration>" >> /etc/hadoop/core-site.xml')

os.system('echo "   " >> /etc/hadoop/core-site.xml')

