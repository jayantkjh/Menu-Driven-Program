import os
import getpass
os.system("tput setaf 3")
print("\t\t\t\tWelcomes to my Menu...")
os.system("tput setaf 7")
print("\t\t\t\t---------------------")
attempt=3
print("you can attempt only thrice")
for i in range(3):
	
	password = getpass.getpass('Enter password:')
	if password != "hello":
		attempt=attempt-1
		print('\t\tInvalid password!!')
		if attempt==0:
			print("\t\tclosing Menu....")
			exit()
		print("\t\tYou have {} attempts remainining".format(attempt))
		print("\t\tpls try again")
		continue
	else:
		break
    
print('You are good to go😀')
r = input('How do you want to login as?(local/remote):')
print("\n\n")
while True:
	os.system("clear")
	print("""
        Press 1 to run date command
        Press 2 to display calender
	Press 3 to check private ip address
        Press 4 to start the services for datanode
	Press 5 to start the service for namenode
	Press 6 to stop the services for datanode
	Press 7 to stop the services for namenode
	Press 8 to check whether hadoop namenode or datanode is running or not
	Press 9 to check the status of hadoop cluster
        Press 10 to start docker services
	Press 11 to pull a docker image
	Press 12 to see all the docker images
	Press 13 to launch a docker container
	Press 14 to start any stopped container
	Press 15 to check the details of running containers
	Press 16 to shutdown any container
	Press 17 to land inside the container
	Press 18 to check all the details of containers(running+stopped)
	Press 19 to permanently remove any os
	Press 20 to install python 
	Press 21 to run Python Interpreter online
	Press 22 to check the status of attached hard disk
	Press 23 to check all the mounted storage
	Press 24 to create logical volume
	Press 25 to check the size contributed by slave
	Press 26 to extend the size of logical volume
	Press 27 to extend volume group	
	Press 28 to Launch an EC2 Instance
	Press 29 to Create an EBS Volume
	Press 30 to Attach EBS Volume to the Instance
	Press 31 to Configure Web Server
	Press 32 to read the packets
	Press 33 to Configure YUM
	Press 34 to Shutdown the System
        """)
	if r=="local":
		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
      			os.system("date")
		if i==2:
			os.system("cal")
		if i==3:
			os.system("ifconfig enp0s3")
		if i==4:
			os.system("hadoop-daemon.sh start datanode")
		if i==5:
			print('Error:this system is configured for datanode')
		if i==6:
			os.system("hadoop-daemon.sh stop datanode")
		if i==7:
			print('Error:this system is configured for datanode')
		if i==8:
 			os.system("jps")
		if i==9:
			os.system("hadoop dfsadmin -report")
		if i==10:
			os.system("systemctl start docker")
		if i==11:
			i=input("enter image name")
			os.system("docker pull {}".format(i))
		if i==12:
			os.system("docker images")
		if i==13:
			i=input("enter image name:")
			n=input("provide os name:")
			os.system("docker run -it --name {} {}".format(n,i))
		if i==14:
			n=input("enter os name:")
			os.system("docker start {}".format(n))
		if i==15:
			os.system("docker ps")
		if i==16:
			n=input("enter os name:")
			os.system("docker stop {}".format(n))
		if i==17:
			n=input("enter os name:")
			os.system("docker attach {}".format(n))
		if i==18:
			os.system("docker ps -a")
		if i==19:
			n=input("enter os name:")
			os.system("docker rm {}".format(n))
		if i==20:
			os.system("yum install python3")
		if i==21:
			os.system("python3")
		if i==22:
      			os.system("fdisk -l")
		if i==23:
			os.system("df -h")
		if i==24:
			hn=input("enter hard disk name:")
			print("Creating Physical Volume.....")
			os.system("pvcreate {}".format(hn));
			vgn=input("provide volume group name:")
			print("Creating Volume Group.....")
			os.system("vgcreate {} {}".format(vgn,hn))
			lvn=input("provide logical volume name:")
			lvs=input("provide logical volume size:")
			print("creating logical volume.....")
			os.system("lvcreate --size {} --name {} {}       	           	".format(lvs,lvn,vgn))
			lvp="/dev"+"/"+vgn+"/"+lvn
			print("formatting logical volume.......")
			os.system("mkfs.ext4 {}".format(lvp))
			print("mounting the logical volume with directory of 	   data 			node......");
			os.system("mount {} /dn".format(lvp))
		if i==25:
			os.system("hadoop dfsadmin -report")
   
		if i==26:
			es=input("Enter the size you want  to increase:")
			vgn=input("provide volume group name:")
			lvn=input("provide logical volume name:")
			lvp="/dev"+"/"+vgn+"/"+lvn
			print("increasing logical volume........")
			os.system("lvextend --size +{} {}".format(es,lvp))
			os.system("resize2fs {}".format(lvp))
		if i==27:
			hn1=input("enter hard disk name:")
			print("Creating Physical Volume.....")
			os.system("pvcreate {}".format(hn1));
			print("increasing volume group.....")
			os.system("vgextend {} {}".format(vgn,hn1))
			es=input("Enter the size you want  to increase:")
			vgn=input("provide volume group name:")
			lvn=input("provide logical volume name:")
			print("increasing logical volume........")
			lvp="/dev"+"/"+vgn+"/"+lvn
			os.system("lvextend --size +{} {}".format(es,lvp))
			os.system("resize2fs {}".format(lvp))
		
		if i==28:
			print("Name your Key Pair:",end='')
			kp=input()
			os.system(f"aws ec2 create-key-pair --key-name {kp}")
			print("Name your Security Group:",end='')
			sg=input()
			os.system(f"aws ec2 create-security-group --description virtualfirewall --group-name {sg}")
			print("Type your security group id from above:",end='')
			sgi=input()
			os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id subnet-b3222bdb --security-group-ids {} --key-name {}".format(sgi,kp))
			print("--------------------------EC2 Instance launched-----------------------------")
		if i==29:
			print("Availability Zone:",end='')
			az=input()
			print("Size of EBS Volume:",end='')
			sz=input()
			os.system(f"aws ec2 create-volume --availability-zone {az} --size {sz}")
			print("-----------------------------Volume Created-------------------------------")
		if i==30:
			print("Volume Id:",end='')
			vi=input()
			print("Instance ID:",end='')
			ii=input()
			os.system(f"aws ec2 attach-volume --device /dev/sdc --instance-id {ii} --volume-id {vi}")
			print("-------------------------EBS Volume is attached to above ec2 Instance--------------------------")
		if i==31:
			os.system("yum install httpd")
			os.system("systemctl start httpd")
			print("-------------------------Web Configuration Completed------------------------")
		if i==32:
			pro=input("Enter the protocol for which u have to read the packet:")
			if pro=="ssh":			
				os.system("tcpdump -i enp0s3 tcp port 22 -n")
			else:
				os.system(f"tcpdump -i enp0s3 {pro} -n")

	
		if i==33:

			print("Configuring YUM... wait!")

			os.system("echo \[dvd1] >> test.repo")

			os.system("echo  \bbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream >> test.repo")

			os.system("echo  \gpgcheck=0 >> test.repo")

			os.system("echo \n >> test.repo")

			os.system("echo \[dvd2] >> test.repo")

			os.system("echo \bbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS >> test.repo")

			os.system("echo \gpgcheck=0 >> test.repo")

			os.system("cp test.repo /etc/yum.repos.d")

			os.system("yum repolist >> test.repo")

		if i==34:
			print("System is shutting down.......")
			os.system("init 0")
			
		
				
	elif r=="remote":
		ip = input("Enter Remote Ip:")
		print(ip)
		i = int(input("Enter ur choice:"))
		print(i)
		if i==1:
			os.system("ssh {} date".format(ip))
		if i==2:
			os.system("ssh {} cal".format(ip))
		if i==3:
			os.system("ssh {} ifconfig enp0s3".format(ip))
		if i==4:
			print('Error:this system is configured for namenode')
		if i==5:
			os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
		if i==6:
			print('Error:this system is configured for namenode')
		if i==7:
			os.system("ssh {} hadoop-daemon.sh stop namenode".format(ip))						
		if i==8:
 			os.system("ssh {} jps".format(ip))
		if i==9:
			os.system("ssh {} hadoop dfsadmin -report".format(ip))	
		if i==10:
			os.system("ssh {} systemctl start docker".format(ip))
		if i==11:
			i=input("enter image name:")
			os.system("ssh {} docker pull {}".format(ip,i))
		if i==12:
			os.system("ssh {} docker images".format(ip))
		if i==13:
			i=input("enter image name:")
			n=input("provide os name:")
			os.system("ssh {} docker run -it --name {} {}".format(ip,n,i))
		if i==14:
			n=input("enter os name:")
			os.system("ssh {} docker start {}".format(ip,n))
		if i==15:
			os.system("ssh {} docker ps".format(ip))
		if i==16:
			n=input("enter os name:")
			os.system("ssh {} docker stop {}".format(ip,n))
		if i==17:
			n=input("enter os name:")
			os.system("ssh {} docker attach {}".format(ip,n))
		if i==18:
			os.system("ssh {} docker ps -a".format(ip))
		if i==19:
			n=input("enter os name:")
			os.system("ssh {} docker rm {}".format(ip,n))
		if i==20:
			os.system("ssh {} yum install python3".format(ip))
		if i==21:
			os.system("ssh {} python3".format(ip))
		if i==22:
      			os.system("ssh {} fdisk -l".format(ip))
		if i==23:
			os.system("ssh {} df -h".format(ip))
		if i==24:
			hn=input("enter hard disk name:")
			print("Creating Physical Volume.....")
			os.system("ssh {} pvcreate {}".format(ip,hn));
			vgn=input("provide volume group name:")
			print("Creating Volume Group.....")
			os.system("ssh {} vgcreate {} {}".format(ip,vgn,hn))
			lvn=input("provide logical volume name:")
			lvs=input("provide logical volume size:")
			print("creating logical volume.....")
			os.system("ssh {} lvcreate --size {} --name {} {}       	           	".format(ip,lvs,lvn,vgn))
			lvp="/dev"+"/"+vgn+"/"+lvn
			print("formatting logical volume.......")
			os.system("ssh {} mkfs.ext4 {}".format(ip,lvp))
			print("mounting the logical volume with directory of data 			node......");
			os.system("ssh {} mount {} /dn".format(ip,lvp))
		if i==25:
			os.system("ssh {} hadoop dfsadmin -report".format(ip))
   
		if i==26:
			es=input("Enter the size you want  to increase:")
			vgn=input("provide volume group name:")
			lvn=input("provide logical volume name:")
			lvp="/dev"+"/"+vgn+"/"+lvn
			print("increasing logical volume........")
			os.system("ssh {} lvextend --size +{} {}".format(ip,es,lvp))
			os.system("ssh {} resize2fs {}".format(ip,lvp))
		if i==27:
			hn1=input("enter hard disk name:")
			print("Creating Physical Volume.....")
			os.system("ssh {} pvcreate {}".format(ip,hn1));
			print("increasing volume group.....")
			os.system("ssh {} vgextend {} {}".format(ip,vgn,hn1))
			es=input("Enter the size you want  to increase:")
			vgn=input("provide volume group name:")
			lvn=input("provide logical volume name:")
			print("increasing logical volume........")
			lvp="/dev"+"/"+vgn+"/"+lvn
			os.system("ssh {} lvextend --size +{} {}".format(ip,es,lvp))
			os.system("ssh {} resize2fs {}".format(ip,lvp))	
		if i==31:
			os.system(f"ssh {ip} yum install httpd")
			os.system(f"ssh {ip} systemctl start httpd")
		if i==32:
			pro=input("Enter the protocol for which u have to read the packet:",end='')
			if pro=="ssh":			
				os.system("tcpdump -i enp0s3 tcp port 22 -n")
			else:
				os.system(f"tcpdump -i enp0s3 {pro} -n")
		if i==33:

			print("Configuring YUM... wait!")

			os.system("echo \[dvd1] >> test.repo")

			os.system("echo  \ \bbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream >> test.repo")

			os.system("echo  \gpgcheck=0 >> test.repo")

			os.system("echo \ \b\n >> test.repo")

			os.system("echo \[dvd2] >> test.repo")

			os.system("echo \ \bbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS >> test.repo")

			os.system("echo \gpgcheck=0 >> test.repo")

			os.system("scp test.repo {}:/etc/yum.repos.d".format(ip))

			os.system("yum repolist >> test.repo")

			os.system("rm -rf test.repo")


				
	else:
		print("login not supported")
		exit()
	input("please enter to continue")
      
      
                
