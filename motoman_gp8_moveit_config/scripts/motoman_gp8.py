#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math
import copy
import moveit_commander
import moveit_msgs.msg
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Quaternion, Pose, PoseStamped, Vector3

#grobal
manip = moveit_commander.MoveGroupCommander("manip")

# "X+"
def joint_1_st(array):
    # number "0"
    if array.data[0] == 1:
        print "array.data[0] =", array.data[0]
        joint_goal = manip.get_current_joint_values()
        joint_goal[0] -=0.3
        print "manip:", manip.go(joint_goal, wait=True)

    #alphabet "w"
    elif array.data[6] == 1:
        print "array.data[6] =", array.data[6]
        joint_1_s_waypoints = []
        joint_1_s_wpose = manip.get_current_pose().pose
        joint_1_s_wpose.position.y += -1 * 0.1
        joint_1_s_waypoints.append(copy.deepcopy(joint_1_s_wpose))
        (plan, fraction) = manip.compute_cartesian_path(joint_1_s_waypoints,0.01,0.0)
        print "CARTESIAN",manip.execute(plan, wait=True)
    

# "X-"
def joint_1_ss(array):
    #number "1"
    if array.data[1] == 1:
        print "array.data[1] =", array.data[1]
        joint_goal = manip.get_current_joint_values()
        joint_goal[0] +=0.3
        print "manip:",manip.go(joint_goal, wait=True)

    #alphabet "a"
    elif array.data[7] == 1:
        print "array.data[7] =", array.data[7] 
        joint_2_l_waypoints = []
        joint_2_l_wpose = manip.get_current_pose().pose
        joint_2_l_wpose.position.y -= -1 * 0.1
        joint_2_l_waypoints.append(copy.deepcopy(joint_2_l_wpose))
        (plan, fraction) = manip.compute_cartesian_path(joint_2_l_waypoints,0.01,0.0)
        print "CARTESIAN",manip.execute(plan, wait=True)
    

# "Y+"
def joint_2_lt(array):
    #number "2"
    if array.data[2] == 1:
        print "array.data[2] =", array.data[2]
        joint_goal = manip.get_current_joint_values()
        joint_goal[1] -=0.3
        print "manip",manip.go(joint_goal, wait=True)

    #alphabet "s"
    elif array.data[8] == 1:
        print "array.data[8] =", array.data[8]
        joint_3_u_waypoints = []
        joint_3_u_wpose = manip.get_current_pose().pose
        joint_3_u_wpose.position.z -= -1 * 0.1
        joint_3_u_waypoints.append(copy.deepcopy(joint_3_u_wpose))
        (plan, fraction) = manip.compute_cartesian_path(joint_3_u_waypoints,0.01,0.0)
        print "CARTESIAN",manip.execute(plan, wait=True)
    

# "Y-"
def joint_2_ls(array):
    #number "3"
    if array.data[3] == 1:
        print "array.data[3] =", array.data[3]
        joint_goal = manip.get_current_joint_values()
        joint_goal[1] +=0.3
        print "manip",manip.go(joint_goal, wait=True)
    
    #alphabet "d"
    elif array.data[9] == 1:
        print "array.data[9] =", array.data[9]
        joint_4_r_waypoints = []
        joint_4_r_wpose = manip.get_current_pose().pose
        joint_4_r_wpose.position.z += -1 * 0.1
        joint_4_r_waypoints.append(copy.deepcopy(joint_4_r_wpose))
        (plan, fraction) = manip.compute_cartesian_path(joint_4_r_waypoints,0.01,0.0)
        print "CARTESIAN",manip.execute(plan, wait=True)

# "Z+"
def joint_3_ut(array):
    #number "4"
    if array.data[4] == 1:
        print "array.data[4] =", array.data[4]
        joint_goal = manip.get_current_joint_values()
        joint_goal[2] +=0.3
        print "manip",manip.go(joint_goal, wait=True)

    #alphabet "x"
    elif array.data[10] == 1:
        print "array.data[10] =", array.data[10]
        joint_5_b_waypoints = []
        joint_5_b_wpose = manip.get_current_pose().pose
        joint_5_b_wpose.position.x -= -1 * 0.1
        joint_5_b_waypoints.append(copy.deepcopy(joint_5_b_wpose))
        (plan, fraction) = manip.compute_cartesian_path(joint_5_b_waypoints,0.01,0.0)
        print "CARTESIAN",manip.execute(plan, wait=True)

# "Z-"
def joint_3_us(array):
    #number "5"
    if array.data[5] == 1:
        print "array.data[5] =", array.data[5]
        joint_goal = manip.get_current_joint_values()
        joint_goal[2] -=0.3
        print "manip",manip.go(joint_goal, wait=True)
    
    #alphabet "f"
    elif array.data[11] == 1:
        print "array.data[11] =", array.data[11]
        joint_6_t_waypoints = []
        joint_6_t_wpose = manip.get_current_pose().pose
        joint_6_t_wpose.position.x += -1 * 0.1
        joint_6_t_waypoints.append(copy.deepcopy(joint_6_t_wpose))
        (plan, fraction) = manip.compute_cartesian_path(joint_6_t_waypoints,0.01,0.0)
        print "CARTESIAN",manip.execute(plan, wait=True)

# default joint 
def joint_default(array):
        joint_goal = manip.get_current_joint_values()
        joint_goal[0] = 0.0
        joint_goal[1] = 0.7
        joint_goal[2] = 0.4
        joint_goal[3] = 0.0
        joint_goal[4] = -1.3
        joint_goal[5] = 0.0
        print "manip",manip.go(joint_goal, wait=True)


def arraycallback(array):

    robot = moveit_commander.RobotCommander()
    #print "Robot state:", robot.get_current_state()
    print "Robot groups:", robot.get_group_names()
    # group name manip
    Manip = moveit_commander.MoveGroupCommander("manip")
    #joint_goal = manip.get_current_joint_values()
    
    # initial angule 
    #joint_goal[0] = 0.0
    #joint_goal[1] = 0.7
    #joint_goal[2] = 0.4
    #joint_goal[3] = 0.0
    #joint_goal[4] = -1.3
    #joint_goal[5] = 0.0

    # plan and excute
    #print "manip",manip.go(joint_goal, wait=True)
    #print "manip Joint values:",Manip.get_current_joint_values()

    print "array.data[0] =", array.data[0]
    print "array.data[1] =", array.data[1]
    print "array.data[2] =", array.data[2]
    print "array.data[3] =", array.data[3]
    print "array.data[4] =", array.data[4]
    print "array.data[5] =", array.data[5]
    
    

    #number joint
    if array.data[0] == 1 or array.data[6] == 1:
        joint_1_st(array)

    elif array.data[1] == 1 or array.data[7] == 1:
        joint_1_ss(array)

    elif array.data[2] == 1 or array.data[8] == 1:
        joint_2_lt(array)

    elif array.data[3] == 1 or array.data[9] == 1:
        joint_2_ls(array)

    elif array.data[4] == 1 or array.data[10] == 1:
        joint_3_ut(array)

    elif array.data[5] == 1 or array.data[11] == 1:
        joint_3_us(array) 

    elif array.data[12] == 1:
        joint_default(array)

 
def main():
     rospy.init_node('motoman_gp8_node', anonymous=True)
     
     rospy.Subscriber("chatter", Float32MultiArray, arraycallback)

     print "Waiting for Number and Alphabet ... \n"
     
     rospy.spin()
 
if __name__ == '__main__':
     try:
         main()
     except rospy.ROSInterruptException: pass
