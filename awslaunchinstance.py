#starting aws ec2 instance

import os
instance_id = input("instance_id")
os.system("aws ec2 start-instances --instance-ids {0}".format(instance_id) )
