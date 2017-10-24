#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import PoseWithCovarianceStamped as pose
file=open("odom_data.txt","w")

def record(data):

    file.write("Frame: "+data.header.frame_id+"\n")
    file.write("stamp: "+str(data.header.stamp)+"\n")
    file.write("seq: "+str(data.header.seq)+"\n")
    file.write("Position:\n")
    file.write(" x: "+str(data.pose.pose.position.x)+"\n")
    file.write(" y: "+str(data.pose.pose.position.y)+"\n")
    file.write(" z: "+str(data.pose.pose.position.z)+"\n")
    file.write("Orientation:\n")
    file.write(" x: "+str(data.pose.pose.orientation.x)+"\n")
    file.write(" y: "+str(data.pose.pose.orientation.y)+"\n")
    file.write(" z: "+str(data.pose.pose.orientation.z)+"\n")
    file.write(" w: "+str(data.pose.pose.orientation.w)+"\n")

def recorder():
    rospy.init_node('recorder',anonymous=True)
    rospy.Subscriber('/svo/pose_imu',pose,record)
    rospy.spin()

    
if __name__ == '__main__':
    recorder()