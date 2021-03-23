import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions


def generate_launch_description():
    joy_config = launch.substitutions.LaunchConfiguration('joy_config')
    joy_dev = launch.substitutions.LaunchConfiguration('joy_dev')
    config_filepath = launch.substitutions.LaunchConfiguration('config_filepath')

    velocity_smoother = launch_ros.actions.Node(
        package='velocity_smoother',
        executable='velocity_smoother',
        name='velocity_smoother',
        output='both',
        parameters=[config_filepath],
        remappings=[('velocity_smoother/input', 'input/joystick_raw'),
                    ('velocity_smoother/feedback/cmd_vel', 'commands/velocity'),
                    ('velocity_smoother/smoothed', 'input/joystick')
                    ]
    )

    joy_node = launch_ros.actions.Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        parameters=[{
            'dev': joy_dev,
            'deadzone': 0.3,
            'autorepeat_rate': 20.0,
        }])

    teleop_node = launch_ros.actions.Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy_node',
        parameters=[config_filepath],
        remappings=[('cmd_vel', 'input/joystick_raw')]
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('joy_config', default_value='xf710'),
        launch.actions.DeclareLaunchArgument('joy_dev', default_value='/dev/f710'),
        launch.actions.DeclareLaunchArgument('config_filepath', default_value=[
            launch.substitutions.TextSubstitution(text=os.path.join(
                get_package_share_directory('ros2_turtlebot_launch'), 'config', '')),
            joy_config, launch.substitutions.TextSubstitution(text='.config.yaml')]),
        joy_node,
        teleop_node,
        velocity_smoother
    ])
