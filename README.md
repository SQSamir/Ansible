 Ansible-dan öncə serverlərin sazlanması..
 
Yeni istifadəçənin yaradılması, 
Yaradılmış istifadəçinin sudoers fayla əlavə olunması
Public ssh key-in əlavə edilməsi

Istifadəsi:
Öncə paramiko module-u install olunur, əgər yoxdursa. 
pip3 install paramiko --user

Ansible vasitəsi ilə idarə olunacaq serverlərin İP addressi hosts.txt fayla əlavə olunur və aşağıdakı qaydada script işə salınır. 

Scripti 'executable' etməyi unutmuruq.  chmod +x pre-ansible.py

root@ansible# ./pre-ansible.py root rootpassword hosts.txt ansible
