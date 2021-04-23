from setuptools import setup
from glob import glob

package_name = 'ros2_turtlebot_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + "/launch/", glob('launch/*.launch.py')),
        ('share/' + package_name + "/config/", glob('config/*.config.yaml')),
        ('share/' + package_name + "/map/", glob('map/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rubik',
    maintainer_email='gianluca.bardaro@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
