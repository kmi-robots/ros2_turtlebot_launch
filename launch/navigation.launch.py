import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    map_dir = LaunchConfiguration(
        'map',
        default=os.path.join(
            get_package_share_directory('ros2_turtlebot_launch'),
            'map',
            '46perivale.yaml'))

    param_dir = LaunchConfiguration(
        'params_file',
        default=os.path.join(
            get_package_share_directory('ros2_turtlebot_launch'),
            'config',
            'nav2_tb2.config.yaml'))

    nav2_launch_file_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map',
            default_value=map_dir,
            description='Full path to map file to load'),

        DeclareLaunchArgument(
            'params_file',
            default_value=param_dir,
            description='Full path to param file to load'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_dir, '/bringup_launch.py']),
            launch_arguments={
                'map': map_dir,
                'params_file': param_dir}.items(),
        )
    ])
