from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue
from launch.substitutions import Command
import os 
from ament_index_python.packages import get_package_share_path

def generate_launch_description():

    urdf_path = os.path.join(
        get_package_share_path('diff_test_description'),
        'urdf',
        'diff_sumer_robot_tutor.xacro'
    )

    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    rviz_config_path = os.path.join(
        get_package_share_path('diff_test_description'),
        'rviz',
        'config.rviz'
    )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config_path],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz2_node
    ])
