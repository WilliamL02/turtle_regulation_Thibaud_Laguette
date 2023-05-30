#!/usr/bin/env python

import rospy
import math

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

global waypoint
global angleD
global e

waypoint=[7,7]

def subscribe_pose():
	global turtlePose
	kp = None
	turtlePose=None

	rospy.init_node('set_way_point',anonymous=False)
	rospy.Subscriber("pose",Pose,getPose)

	pub=rospy.Publisher("cmd_vel",Twist,queue_size=1)
	rate=rospy.Rate(10)

	kp=rospy.get_param("~kp")
	kpl=rospy.get_param("~kpl")

	while not rospy.is_shutdown():
		message=Twist()

		if turtlePose is not None:

			angleD=math.atan2( waypoint[1]-turtlePose.y,waypoint[0]-turtlePose.x)
			print("Angle desirer",angleD)
			e=math.atan(math.tan((angleD-turtlePose.theta)/2))
			print("e egale", e)
			u = kp * e
			print("u egale",u)
			message.angular.z = u
			pub.publish(message)
		rate.sleep()

#def move_turtle(pub,rate,linear_speed):


def getPose(pose):
	global turtlePose
	turtlePose=pose


if __name__=="__main__":

	try:
		subscribe_pose()
	except rospy.ROSInterruptException:
		pass
