[Beck to README.md](./README.md)

# Setting up Hadoop

- In all guest vms install ssh
    ```bash
    sudo apt install openssh-server
    sudo systemctl start ssh.service
    sudo systemctl start ssh.socket
    sudo systemctl enable ssh.service
    sudo systemctl enable ssh.socket
    ```
    - Check if you can ssh from host machine to guest vms
        ```bash
        ssh a@192.168.122.100
        exit
        ```
        >Repeat for all guest vms

- For all guest vms find their network node hostname and user_name
    - Open terminal and check printed text
        >Example:
        >```bash
        >a@a0:~$
        >```
        >Here `a` is user_name or user_id and `a0` is host_name

    - If the above text is not printed after you open terminal
        ```bash
        uname -n
        ```
        >This is host_name of that vm
        >```bash
        >a
        >```
        ```bash
        whoami
        ```
        >This is user_name or user_id of that vm
        >```bash
        >a0
        >```
        >Repeat for all guest vms
    - Here all guest vm user_name@host name are:
        - a@a0
        - a@a1
        - a@a2
        - a@a3

- Install other software using ssh
    ```bash
    ssh guest_vm_user_name@192.168.122.100
    ```
    >Once you login to guest vm install softwares
    >```bash
    >sudo apt install vim net-tools openjdk-8-jdk git wget
    >exit
    >```
    >Repeat for other guest vms

- Download hadoop and send it to all guest vms
    ```bash
    wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.2/hadoop-3.3.2.tar.gz
    scp /home/a/Downloads/hadoop-3.3.2.tar.gz 192.168.122.100:~/
    scp /home/a/Downloads/hadoop-3.3.2.tar.gz 192.168.122.101:~/
    scp /home/a/Downloads/hadoop-3.3.2.tar.gz 192.168.122.102:~/
    scp /home/a/Downloads/hadoop-3.3.2.tar.gz 192.168.122.103:~/
    ```
- On all guest vms
    ```bash
    tar xvf hadoop-3.3.2.tar.gz
    ```
    >Repeat for all guest vms

- On all guest vms bind ip address to their respective host name
    ```bash
    sudo vim /etc/hosts
    ```
    >In /etc/hosts add these line on all guest vms
    > Here a0,a1,a2,a3 are hostname and remaining are ip addresses
    >```bash
    > 192.168.122.100 a0
    > 192.168.122.101 a1
    > 192.168.122.102 a2
    > 192.168.122.103 a3
    >```

- On Primary name node, generate ssh id and copy to all nodes.
    ```bash
    ssh-keygen -t rsa -P ""
    ssh-copy-id a@a0
    ssh-copy-id a@a1
    ssh-copy-id a@a2
    ssh-copy-id a@a3
    ```
    >Test if you can ssh without entering password from Primary name node
    >```bash
    >ssh a@a1
    >exit
    >```
    >Repeat for other guest vms

- On all guest vms
    ```bash
    vim ~/.bashrc
    ```
    >In ~/.bashrc add following lines
    >```bash
    >export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    >export HADOOP_HOME=$HOME/hadoop-3.3.2
    >export PATH=$HADOOP_HOME/sbin:$HADOOP_HOME/bin:$PATH
    >```
    
    ```bash
    source ~/.bashrc
    ```
    >Repeat for all guest vms


- On master
    ```bash
    stop-yarn.sh
    stop-dfs.sh
    ```
- Manually move csv to hdfs
    ```bash
    hadoop fs -mkdir -p /user/$USER/emp/input

    hadoop fs -put /home/a/gold_rate.csv /user/$USER/emp/input
    ```