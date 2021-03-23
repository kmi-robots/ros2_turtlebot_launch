import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    launch_dir = os.path.join(get_package_share_directory('ros2_turtlebot_launch'), 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource([launch_dir, '/hokuyo.launch.py'])),
        IncludeLaunchDescription(PythonLaunchDescriptionSource([launch_dir, '/minimal.launch.py'])),
        IncludeLaunchDescription(PythonLaunchDescriptionSource([launch_dir, '/teleop.launch.py']))
        ])
