import os
import subprocess

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
