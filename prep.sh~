#!/bin/bash
#!/usr/bin/expect -f

#pick which operation
# 1 = auto docking
# 2 = gofoward
# 3 = create halt.x file
if [ $2 == auto_docking ] || [ $2 == 1 ]
then
    op="kobuki_auto_docking.x"
elif [ $2 == goforward ] || [ $2 == 2 ]
then
    op="goforward.x"
elif [ $2 == halt ] || [ $2 == 3 ]
then
    op="halt.x"
fi

PATH="$PATH:/opt/ros/indigo/bin/roslaunch";
if [ $1 == donatello ] || [ $1 == d ]; 
then
    echo export ROS_MASTER_URI=http://192.168.0.102:11311 >> ~/.bashrc
    ssh donatello@192.168.0.102 touch Montgomery/$op
    ssh donatello@192.168.0.102 rm Montgomery/halt.x
    
    #ask user to quit
    printf "Enter any key to quit: "
    read response
    #kill file keeping processes running
    ssh donatello@192.168.0.102 rm Montgomery/$op
elif [ $1 == leonardo ] || [ $1 == l ];
then 
    echo export ROS_MASTER_URI=http://192.168.0.103:11311 >> ~/.bashrc
    ssh leonardo@192.168.0.103 touch Montgomery/$op
    ssh leonardo@192.168.0.103 rm Montgomery/halt.x
    
    #ask user to quit
    printf "Enter any key to quit: "
    read response
    #kill file keeping processes running
    ssh leonardo@192.168.0.103 rm Montgomery/$op    
elif [ $1 == michelangelo ] || [ $1 == m ]; 
then
    echo export ROS_MASTER_URI=http://192.168.0.101:11311 >> ~/.bashrc
    ssh michelangelo@192.168.0.101 touch Montgomery/$op
    ssh michelangelo@192.168.0.101 rm Montgomery/halt.x
    
    #ask user to quit
    printf "Enter any key to quit: "
    read response
    #kill file keeping processes running
    ssh michelangelo@192.168.0.101 rm Montgomery/$op
elif [ $1 == raphael ] || [ $1 == r ];
then 
    echo export ROS_MASTER_URI=http://192.168.0.105:11311 >> ~/.bashrc
    ssh raphael@192.168.0.105 touch Montgomery/$op
    ssh raphael@192.168.0.105 rm Montgomery/halt.x
    
    #ask user to quit
    printf "Enter any key to quit: "
    read response
    #kill file keeping processes running
    ssh raphael@192.168.0.105 rm Montgomery/$2 
else 
    echo "ERROR: unknown Turtle Bot";
fi