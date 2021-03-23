import os

import ament_index_python.packages

from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

import yaml


def generate_launch_description():
    share_dir = ament_index_python.packages.get_package_share_directory('ros2_turtlebot_launch')
    params_file = os.path.join(share_dir, 'config', 'kobuki.config.yaml')

    with open(params_file, 'r') as f:
        yaml_file = yaml.safe_load(f)
        cmd_vel_mux_params = yaml_file['cmd_vel_mux']['ros__parameters']
        kobuki_node_params = yaml_file['kobuki_ros_node']['ros__parameters']

    container = ComposableNodeContainer(
            name='kobuki_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='kobuki_node',
                    plugin='kobuki_node::KobukiRos',
                    name='kobuki_ros_node',
                    parameters=[kobuki_node_params]),
                ComposableNode(
                    package='cmd_vel_mux',
                    plugin='cmd_vel_mux::CmdVelMux',
                    name='cmd_vel_mux',
                    parameters=[cmd_vel_mux_params],
                    remappings=[("cmd_vel", "commands/velocity")]
                ),
            ],
            output='both',
    )

    return LaunchDescription([container])
