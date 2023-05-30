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
	#dist_tol=rospy.get_param("~dist_tol")
	while not rospy.is_shutdown():
		message=Twist()

		if turtlePose is not None:

			#partie1
			angleD=math.atan2( waypoint[1]-turtlePose.y,waypoint[0]-turtlePose.x)
			print("Angle desirer=",angleD)
			e=math.atan(math.tan((angleD-turtlePose.theta)/2))
			print("e=", e)
			u = kp * e
			print("u=",u)
			message.angular.z = u


			#partie2

			distance=math.sqrt((math.pow(waypoint[1]-turtlePose.y,2) )+( math.pow(waypoint[0]-turtlePose.x,2))) 
			print("Distance=",distance)
			v=kpl*distance
			print("v=",v)

			message.linear.x=v
			pub.publish(message)

			#t0=rospy.Time.now().to_sec()
			#distance_tolerance=0

			rate.sleep()



def getPose(pose):
	global turtlePose
	turtlePose=pose


if __name__=="__main__":

	try:
		subscribe_pose()
	except rospy.ROSInterruptException:
		pass
