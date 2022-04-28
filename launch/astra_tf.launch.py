import launch
import launch_ros.actions


def generate_launch_description():

    tf_camera = launch_ros.actions.Node(
        package='tf2_ros',
        name='camera_broadcaster',
        executable='static_transform_publisher',
        arguments=['0.12', '0.0', '0.35',
                   '0.0', '-0.044', '0.0', '0.999',
                   'base_link', 'camera_link']
    )
        
    tf_camera_base_link = launch_ros.actions.Node(
        package='tf2_ros',
        name='camera_base_link',
        executable='static_transform_publisher',
        arguments=['0.0', '-0.02', '0.0',
                   '0.0', '0.0', '0.0', '1.0',
                   'camera_link', 'camera_depth_frame']
    )

    tf_camera_base_link1 = launch_ros.actions.Node(
        package='tf2_ros',
        name='camera_base_link1',
        executable='static_transform_publisher',
        arguments=['0.0', '-0.045', '0.0',
                   '0.0', '0.0', '0.0', '1.0',
                   'camera_link', 'camera_rgb_frame']
    )

    tf_camera_base_link2 = launch_ros.actions.Node(
        package='tf2_ros',
        name='camera_base_link2',
        executable='static_transform_publisher',
        arguments=['0.0', '0.0', '0.0',
                   '-0.5', '0.5', '-0.5', '0.5',
                   'camera_depth_frame', 'camera_depth_optical_frame']
    )
        
    tf_camera_base_link3 = launch_ros.actions.Node(
        package='tf2_ros',
        name='camera_base_link3',
        executable='static_transform_publisher',
        arguments=['0.0', '0.0', '0.0',
                   '-0.5', '0.5', '-0.5', '0.5',
                   'camera_rgb_frame', 'camera_rgb_optical_frame']
    )

    return launch.LaunchDescription([
        tf_camera,
        tf_camera_base_link,
        tf_camera_base_link1,
        tf_camera_base_link2,
        tf_camera_base_link3
    ])
