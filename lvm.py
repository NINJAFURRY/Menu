import os
os.system("python3 /ascii.py")
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
