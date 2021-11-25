#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math
import copy
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Quaternion, Pose, PoseStamped, Vector3

######################################
# MAIN
######################################

def main():

    # init node
    rospy.init_node("motoman_gp8_node")

    # configuration for moveit
    robot = moveit_commander.RobotCommander()
    # display of group name (rarm,larm,upper_body...
    print ""
    print "Robot groups:", robot.get_group_names() #manip
    # display of robot current state
    print ""
    print "Robot state:", robot.get_current_state()
    
    # group name manip
    manip = moveit_commander.MoveGroupCommander("manip")

    # display of joint name 
    print ""
    print "manp Joint names:", robot.get_joint_names("manip") 

    joint_goal = manip.get_current_joint_values()
    # initial angule 
    joint_goal[0] = 0.0
    joint_goal[1] = 0.7
    joint_goal[2] = 0.4
    joint_goal[3] = 0.0
    joint_goal[4] = -1.3
    joint_goal[5] = 0.0

    # plan and excute
    print "manip",manip.go(joint_goal, wait=True)
    
    # display of joint values
    print ""
    print "manip Joint values:",manip.get_current_joint_values()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
