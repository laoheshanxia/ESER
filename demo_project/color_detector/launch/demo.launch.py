from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['python3', 'mock_camera.py'],
            output='screen',
            name='mock_camera'
        ),
        Node(
            package='color_detector',
            executable='color_detector_node',
            name='color_detector_node',
            output='screen'
        ),
    ])
