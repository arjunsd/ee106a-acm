#!/usr/bin/env python
#The line above tells Linux that this file is a Python script,
#and that the OS should use the Python interpreter in /usr/bin/env
#to run it. Don't forget to use "chmod +x [filename]" to make
#this script executable.

#Import the dependencies as described in example_pub.py
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import lab3_skeleton as lab3

#Define the callback method which is called whenever this node receives a 
#message on its subscribed topic. The received message is passed as the 
#first argument to callback().
def callback(message):

    #Print the contents of the message to the console
    theta = []
    #print(rospy.get_name() + ": I heard %s" % message.data)
    message.name
    message.position
    message.velocity
    message.effort
    theta.append(message.position[4])
    theta.append(message.position[5])
    theta.append(message.position[2])
    theta.append(message.position[3])
    theta.append(message.position[6])
    theta.append(message.position[7])
    theta.append(message.position[8])
    print("theta = ")
    print(theta)
    print("\n")
    print("----")
    print("gst = ")
    print(lab3.lab3(theta))
    print("----")


# header: 
#   seq: 438136
#   stamp: 
#     secs: 1442601878
#     nsecs: 256716155
#   frame_id: ''
# name: ['head_nod', 'head_pan', 'left_e0', 'left_e1', 'left_s0', 'left_s1', 'left_w0', 'left_w1', 'left_w2', 'right_e0', 'right_e1', 'right_s0', 'right_s1', 'right_w0', 'right_w1', 'right_w2', 'torso_t0']
# position: [0.0, -0.06366020262451172, -0.0007669903930664063, 0.0015339807861328126, -0.04640291878051758, 0.0019174759826660157, -0.0015339807861328126, -0.0007669903930664063, -1.602626426312256, -0.07554855371704101, 0.9111845869628907, 0.04141748122558594, 0.4740000629150391, -0.38081073015747074, -0.12962137642822266, 3.041116908508301, -12.565987104803467]
# velocity: [0.0, -0.009737182724475862, 0.013107745975255967, 0.01610380219817162, -0.011984224891662598, 0.011984224891662598, 0.02247042167186737, 0.019474365448951723, -0.009362675696611405, -0.014231267058849336, -0.0011235210835933687, 0.018350844365358353, -0.008613661640882493, -0.008613661640882493, -0.0003745070278644562, -0.009362675696611405, 0.0]
# effort: [0.0, 0.0, -1.02, -17.78, -1.776, -12.632, 0.044, -2.4, 0.036, -0.532, -4.164, 0.9, 3.996, 0.108, -0.7, -0.224, -20.48]
# ---

#Define the method which contains the node's main functionality
def listener():

    #Run this program as a new node in the ROS computation graph
    #called /listener_<id>, where <id> is a randomly generated numeric
    #string. This randomly generated name means we can start multiple
    #copies of this node without having multiple nodes with the same
    #name, which ROS doesn't allow.
    rospy.init_node('listener', anonymous=True)

    #Create a new instance of the rospy.Subscriber object which we can 
    #use to receive messages of type std_msgs/String from the topic /chatter_talk.
    #Whenever a new message is received, the method callback() will be called
    #with the received message as its first argument.
    rospy.Subscriber("robot/joint_states", JointState, callback)


    #Wait for messages to arrive on the subscribed topics, and exit the node
    #when it is killed with Ctrl+C
    rospy.spin()


#Python's syntax for a main() method
if __name__ == '__main__':
    listener()
