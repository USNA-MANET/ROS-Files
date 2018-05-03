#!/bin/bash
#!/usr/bin/expect -f

###################################
#   FOR DOWNLOADING FROM SPLINTER 
#   TO TURTLEBOTS
###################################

if [ $1 == donatello ] || [ $1 == d ]; 
then
    scp $2 donatello@192.168.0.102:~/Montgomery
elif [ $1 == leonardo ] || [ $1 == l ];
then 
    scp $2 leonardo@192.168.0.103:~/Montgomery
elif [ $1 == michelangelo ] || [ $1 == m ]; 
then
    scp $2 michelangelo@192.168.0.101:~/Montgomery 
elif [ $1 == raphael ] || [ $1 == r ];
then 
    scp $2 raphael@192.168.0.105:~/Montgomery
elif [ $1 == all ] || [ $1 == a ];
then
    scp $2 donatello@192.168.0.102:~/Montgomery
    scp $2 leonardo@192.168.0.103:~/Montgomery
    scp $2 michelangelo@192.168.0.101:~/Montgomery 
    scp $2 raphael@192.168.0.105:~/Montgomery
else 
    echo "ERROR: unknown Turtle Bot";
fi 