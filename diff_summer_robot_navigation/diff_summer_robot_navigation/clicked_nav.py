import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PointStamped, PoseStamped
import tf_transformations
import numpy as np

class ClickedNav(Node):
    def __init__(self):
        super().__init__('clicked_nav')
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()

        self.create_subscription(
            PointStamped,
            '/clicked_point',
            self.clicked_point_callback,
            10
        )
        self.get_logger().info("Esperando clicks en Rviz ")

    def clicked_point_callback(self, msg):
        self.get_logger().info(f"Click recibido en x={msg.point.x}, y={msg.point.y}")
        q_x, q_y, q_z, q_w = tf_transformations.quaternion_from_euler(0.0, 0.0, 0.0)

        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = msg.point.x
        pose.pose.position.y = msg.point.y
        pose.pose.position.z = 0.0
        pose.pose.orientation.x = q_x
        pose.pose.orientation.y = q_y
        pose.pose.orientation.z = q_z
        pose.pose.orientation.w = q_w

        self.navigator.goToPose(pose)

        while not self.navigator.isTaskComplete():
            feedback = self.navigator.getFeedback()
            if feedback:
                self.get_logger().info(
                    f"Moviéndose en x={feedback.current_pose.pose.position.x:.2f}, "
                    f"y={feedback.current_pose.pose.position.y:.2f}"
                )

        result = self.navigator.getResult()
        self.get_logger().info(f"Navigation result: {result}")

        

def main():
    rclpy.init()
    node = ClickedNav()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
