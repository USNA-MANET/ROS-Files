#!/bin/bash
#!/usr/bin/expect -f

#####################################
# CREATES HALT FILES IN TURTLEBOTS
#####################################

if [ $1 == donatello ] || [ $1 == d ]; 
then
    ssh donatello@192.168.0.102 touch Montgomery/halt.x
elif [ $1 == leonardo ] || [ $1 == l ];
then 
    ssh leonardo@192.168.0.103 touch Montgomery/halt.x
elif [ $1 == michelangelo ] || [ $1 == m ]; 
then
    ssh michelangelo@192.168.0.101 touch Montgomery/halt.x
elif [ $1 == raphael ] || [ $1 == r ];
then 
    ssh raphael@192.168.0.105 touch Montgomery/halt.x
else 
    echo "ERROR: unknown Turtle Bot";
fi