# Tactical Traffic Engineering (TTE)
Based off findings from ONOS-TACNET thesis and due to shortfalls with the ONOS application development support, this is a developmental GUI for network operators to implement tactical traffic engineering controls using an ONOS SDN controller. For testing purposes we are utilizing Mininet to emulate our network.

## Prerequisites:
### First Time Installation and Configuration
#### ONOS Installation
Pull and run ONOS Docker image (Ref: https://github.com/jatj/sdn_onos/blob/master/INSTALL.md)
```
sudo docker pull onosproject/onos
sudo docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --name onos onosproject/onos
```
After creating the docker image, ensure to start the docker image.
```
sudo docker start onos
```
You can check current running dockers with the following:
```
sudo docker ps
```
Login to ONOS (Username: ```onos```  Password: ```rocks```)
```
ssh -p 8101 onos@172.17.0.1
```
Enable OpenFlow on ONOS (And any other ONOS applications you may want, like ReactiveForwarding)
```
app activate org.onosproject.openflow
app activate org.onosproject.fwd
```
#### Mininet Installation
Install Mininet (Ref: http://mininet.org/download/)
```
git clone https://github.com/mininet/mininet
./mininet/util/install.sh -a
```

## Project setup
Start Mininet with OpenFlow14 enabled OVS switches, connected to our ONOS SDN controller on IP ```172.17.0.2``` (using tree topology, for example)
```
sudo mn --switch ovs,protocols=OpenFlow14 --controller=remote,ip=172.17.0.2 --topo=tree,2,2
```
***Without enabling the OpenFlow application on ONOS, Mininet won't be able to connect to the OpenFlow port 6653/6633. You should receive an error such as: 
```
*** Adding controller
Unable to contact the remote controller at 172.17.0.2:6653
Unable to contact the remote controller at 172.17.0.2:6633
```

Start Flask application. This serves as the backend server which will send, receive, and process HTTP requests between the ONOS server and frontend server.
```
python3 app.py
```
Install and run Vue server. This serves as the frontend web server/GUI.
```
npm install
npm run serve
```
