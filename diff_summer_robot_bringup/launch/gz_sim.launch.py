from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory 


def generate_launch_description():
    gz_launch_path=os.path.join(get_package_share_directory('ros_gz_sim'), 'launch')
    urdf_path=os.path.join(get_package_share_directory('diff_test_description'), 'urdf', 'diff_sumer_robot_tutor.xacro')
    gz_bridge_config_path=os.path.join(get_package_share_directory('diff_summer_robot_bringup'), 'config', 'gz_bridge.yaml')
    gazebo_world_path=os.path.join(get_package_share_directory('diff_summer_robot_bringup'), 'world', 'my_first_world.sdf')
    robot_description=ParameterValue(Command(['xacro ', urdf_path]), value_type=str)
    robot_state_publisher_node=Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}],
    )
    gz_sim_launch=IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gz_launch_path, '/gz_sim.launch.py']),
        launch_arguments={
            'gz_args': f'{gazebo_world_path} -r'}.items()
    )    
    
    rviz2_node=Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', os.path.join(get_package_share_directory('diff_test_description'), 'rviz', 'config.rviz')]
    )

    gz_create_entity=Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', '/robot_description']
    )

    gz_bridge_node=Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{'config_file': gz_bridge_config_path}]
    )
    return LaunchDescription([
        robot_state_publisher_node,
        gz_sim_launch,
        gz_create_entity,
        rviz2_node,
        gz_bridge_node
    ]
        )