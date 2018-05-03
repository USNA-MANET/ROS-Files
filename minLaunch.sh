#!/bin/bash
#!/usr/bin/expect -f

#ensure correct path to roslaunch
PATH="$PATH:/opt/ros/indigo/bin";

#Splinter should create file for startup
#touch kobuki_auto_docking.x
# and remove for startup
#rm halt.x

while [ -e halt.x ]
do sleep 1
done

#autonomously dock to charge
if [ -e kobuki_auto_docking.x ]
then
    roslaunch turtlebot_bringup minimal.launch >& /dev/null &
    echo "bringup minimal.launch"
    sleep 5
    roslaunch kobuki_auto_docking minimal.launch >& /dev/null &
    echo "auto_docking minimal.launch"
    python client.py 
    roslaunch kobuki_auto_docking activate.launch >& /dev/null &
    echo "activate.launch"

    while [ -e kobuki_auto_docking.x ]
    do sleep 1
    done

    #kill the three processes for auto docking
    echo "killing kobuki_auto_docking"
    kill %1 %2 %3 
fi

if [ -e goforward.x ] 
then
    roslaunch turtlebot_bringup minimal.launch >& /dev/null &
    echo "bringup minimal.launch"
    sleep 5
    python client.py 
    python goforward.py >& /dev/null &
    echo "going forward"

    while [ -e goforward.x ]
    do sleep 1
    done

    #kill the two processes for going forward
    echo "killing goforward"
    kill %1 %2
fi

if [ -e goCircular.x ] 
then
    roslaunch turtlebot_bringup minimal.launch >& /dev/null &
    echo "bringup minimal.launch"
    sleep 5
    python client.py 
    python goCircular.py >& /dev/null &
    echo "going circular"

    while [ -e goCircular.x ]
    do sleep 1
    done

    #kill the two processes for going Circular
    echo "killing goCircular.py"
    kill %1 %2
fi

if [ -e goForwardAvoid.x ] 
then
    roslaunch turtlebot_bringup minimal.launch >& /dev/null &
    echo "bringup minimal.launch"
    sleep 5
    roslaunch turtlebot_navigation amcl_demo.launch map_file:/tmp/my_map.yaml >& /dev/null &
    echo "bringup yaml file"
    sleep 5
    python client.py 
    python goforward_and_avoid_obstacle.py >& /dev/null &
    echo "going forward & avoiding obstacles"

    while [ -e goForwardAvoid.x ]
    do sleep 1
    done

    #kill the two processes for going forward
    echo "killing goforward_and_avoid_obstacles.py"
    kill %1 %2
fi

#re-make haltng file
touch halt.x 
sleep 1

#exit success
echo "exiting"
exit 0

