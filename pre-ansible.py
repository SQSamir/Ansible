#!/usr/bin/python3
import sys, paramiko
import os
if len(sys.argv) < 4:
    print("Qayda aşağıdakı kimidir")
    print("Məsələn : "+sys.argv[0],"username password hostsfile newusername","{yeni password newusername123 olacaq}")
    sys.exit(1)
password=sys.argv[2]
username=sys.argv[1]
hostsfayl=sys.argv[3]
newuser=sys.argv[4]
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

useradd="sudo useradd {new} && echo {new}123 |sudo passwd {new} --stdin ".format(new=newuser)
addsudoers="echo '{new} ALL=(ALL) NOPASSWD:ALL'|sudo tee -a  /etc/sudoers".format(new=newuser)
port = 22
fo = open(hostsfayl, "r+")
lines=fo.readlines()
for line in lines:
   hostname=str(line.split()[0])
   print(hostname)
   try:
       client.connect(hostname, port=port, username=username, password=password)      
       stdin, stdout, stderr = client.exec_command(useradd)
       for files in stdout.readlines():
          print(files)
       client.exec_command(addsudoers)
       addsshkey="sshpass -p {new}123 ssh-copy-id  {new}@{hostname}".format(new=newuser,hostname=hostname)
       os.system(addsshkey)

   except paramiko.AuthenticationException:
            print("Authentication failed, zəhmət olmasa parolun və ya istifadəçi adının düzgünlüyün yoxlayın bu serverdə -> {} ".format(hostname))
   except paramiko.SSHException as sshException:
            print("Serverə qoşula bilmədi: %s" % sshException)
   except:
       pass
   finally:
       client.close()
fo.close()
