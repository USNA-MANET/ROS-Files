#!/bin/bash
#!/usr/bin/expect -f


###################################
#   FOR DOWNLOADING TO SPLINTER 
#   FROM TURTLEBOTS
###################################

#check if location was specified

if [ $# == 2 ];
then
    homeLoc="./"
else
    homeLoc= $3
fi

if [ $1 == donatello ] || [ $1 == d ]; 
then
    scp donatello@192.168.0.102:~/Montgomery/$2 $homeLoc
elif [ $1 == leonardo ] || [ $1 == l ];
then 
    scp leonardo@192.168.0.103:~/Montgomery/$2 $homeLoc
elif [ $1 == michelangelo ] || [ $1 == m ]; 
then
    scp michelangelo@192.168.0.101:~/Montgomery/$2 $homeLoc
elif [ $1 == raphael ] || [ $1 == r ];
then 
    scp raphael@192.168.0.105:~/Montgomery/$2 $homeLoc
else 
    echo "ERROR: unknown Turtle Bot";
fi 