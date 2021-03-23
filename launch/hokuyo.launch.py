import launch
import launch_ros.actions


def generate_launch_description():
    hokuyo = launch_ros.actions.Node(
        package='urg_node',
        executable='urg_node_driver',
        name='hokuyo_node',
        output='both',
        parameters=[{'serial_port': '/dev/hokuyo'}]
    )

    tf_laser = launch_ros.actions.Node(
        package='tf2_ros',
        name='tf_hokuyo',
        executable='static_transform_publisher',
        arguments=['0.0', '0.0', '0.38',
                   '0.0', '0.0', '0.0', '1.0',
                   'base', 'laser']
    )

    return launch.LaunchDescription([
        hokuyo,
        tf_laser
    ])
