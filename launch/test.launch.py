import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

kobuki_node = os.path.join(
    get_package_share_directory('kobuki_node'),
    'launch',
    'kobuki_node-launch.py'
)

cmd_vel_mux = os.path.join(
    get_package_share_directory('cmd_vel_mux'),
    'launch',
    'cmd_vel_mux-launch.py'
)


def generate_launch_description():
    # share_dir = get_package_share_directory('kobuki_teleop')
    # # There are two different ways to pass parameters to a non-composed node;
    # # either by specifying the path to the file containing the parameters, or by
    # # passing a dictionary containing the key -> value pairs of the parameters.
    # # When starting a *composed* node on the other hand, only the dictionary
    # # style is supported.  To keep the code between the non-composed and
    # # composed launch file similar, we use that style here as well.
    # params_file = os.path.join(share_dir, 'config', 'safety_controller_params.yaml')
    # with open(params_file, 'r') as f:
    #     params = yaml.safe_load(f)['kobuki_safety_controller_node']['ros__parameters']
    # safety_controller_node = Node(package='kobuki_safety_controller',
    #                               node_executable='kobuki_safety_controller_node',
    #                               output='both',
    #                               parameters=[params])

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([kobuki_node])
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([cmd_vel_mux])
        )
    ])