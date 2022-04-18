#attaching pre created ebs volume to ec2 instance

import os
instance_id = input("instance_id")
volume_id = input("volume_id")
os.system("aws ec2 attach-volume --device /dev/sdf --instance-id {0} --volume-id {1}".format(instance_id,volume_id) )
