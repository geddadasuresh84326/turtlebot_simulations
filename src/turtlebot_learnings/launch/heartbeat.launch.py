from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot_learnings',
            executable='heartbeat_executable',
            output='screen'),
        Node(
            package='turtlebot_learnings',
            executable='heartbeat_node_executable',
            output='screen')
    ])