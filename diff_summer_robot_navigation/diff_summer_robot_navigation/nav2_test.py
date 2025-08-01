import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped 
import tf_transformations 
import numpy as np

def create_poste_stamped(navigator:BasicNavigator, position_x:float, position_y:float, orientation_z):
    q_x, q_y,q_z,q_w=tf_transformations.quaternion_from_euler(0.0,0.0,np.deg2rad(orientation_z))#angulos de rotacion en el eje x y z
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = 0.0
    pose.pose.position.y = 0.0
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w

    return pose 


def main():
    rclpy.init()
    nav = BasicNavigator()

    # set initial pose
    q_x, q_y,q_z,q_w=tf_transformations.quaternion_from_euler(0.0,0.0,0.0)#angulos de rotacion en el eje x y z
    initial_pose = create_poste_stamped(nav,0.0,0.0,0.0)

    nav.setInitialPose(initial_pose)

    # wait for Nav2
    nav.waitUntilNav2Active()

    goal_pose = create_poste_stamped(nav,1.5,2.5,135.)

    nav.goToPose(goal_pose)
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        nav.get_logger().info(f'x:{feedback.current_pose.pose.position.x}, y:{feedback.current_pose.pose.position.y}')

    result=nav.getResult()
    nav.get_logger().info(f'result:{result.error_msg}')



    # shutdown
    rclpy.shutdown()

if __name__=='__main__':
    main()
