# Gold Price Prediction

By Jadhav Abhishek and Harshit Gupta</br>

![logo](./data/logo.png)

---

# 1. Setting Hadoop
- Install hypervisor to run Virtual machine

    ```bash
    sudo apt-get install qemu-system virt-manager 
    ```
- [Download guest os file, like Ubuntu](https://ubuntu.com/download)
- Install Ubuntu on host by virt-manager
- Set static ip for guest machine[^1]
    ```bash
    virsh  net-list # displays 'name' as $NETWORK_NAME,Probably "default"
    virsh  net-edit  $NETWORK_NAME
    ```
    >Note : write mac,name and desired ip of guest vm
    >```bash
    ><dhcp>
    >    <range start="192.168.122.100" end="192.168.122.254"/>
    >    <host mac="52:54:00:6c:3c:01" name="Project_Main" ip="192.168.122.100"/>
    >    <host mac="52:54:00:6c:3c:02" name="Project_Data" ip="192.168.122.101"/>
    >    <host mac="52:54:00:6c:3c:03" name="Project_Secondary" ip="192.168.122.102"/>
    >    <host mac="52:54:00:6c:3c:03" name="Project_Redundant" ip="192.168.122.103"/>
    ></dhcp>
    >```
- Restart network and vm
    ```bash
    virsh  net-destroy  $NETWORK_NAME  
    virsh  net-start    $NETWORK_NAME 
    virsh  net-autostart    $NETWORK_NAME 
    ```
    >If that still doesn't work, you might have to
    >- stop the libvirtd service
    >- kill any dnsmasq processes that are still alive
    >- start the libvirtd service

- In all guest vms install ssh
    ```bash
    sudo apt install openssh-server
    sudo systemctl start ssh.service
    sudo systemctl start ssh.socket
    ```

- Install other software using ssh
    ```bash
    ssh guest_user@192.168.122.100
    ```
    >Once you login to guest vm install softwares
    >```bash
    >sudo apt install vim net-tools openjdk-8-jdk git
    >exit
    >```
    >Repeat for other guest vms

- 




---
# Important links:

module used : 
https://pypi.org/project/yfinance/

module wikis : 
https://github.com/ranaroussi/yfinance/wiki/


[^1]:https://serverfault.com/questions/627238/kvm-libvirt-how-to-configure-static-guest-ip-addresses-on-the-virtualisation-ho