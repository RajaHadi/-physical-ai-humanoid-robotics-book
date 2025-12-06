import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition # Import IfCondition

def generate_launch_description():
    pkg_name = 'ros2_foundations'
    pkg_share_dir = get_package_share_directory(pkg_name)
    urdf_path = os.path.join(pkg_share_dir, 'urdf', 'humanoid.urdf')

    use_jsp_gui = LaunchConfiguration('use_jsp_gui', default='true')

    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_jsp_gui',
            default_value='true',
            description='Flag to enable joint_state_publisher_gui'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_path).read()}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            condition=IfCondition(use_jsp_gui), # Use IfCondition directly
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(pkg_share_dir, 'rviz', 'urdf_config.rviz')], # Placeholder rviz config
        )
    ])