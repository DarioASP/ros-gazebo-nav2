from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='diff_summer_robot_navigation',  # Reemplaza con el nombre real de tu paquete
            executable='set_inital_pose',
            output='screen',
        ),
        Node(
            package='diff_summer_robot_navigation',
            executable='clicked_nav',
            output='screen',
        ),
    ])


