from setuptools import setup
import os
from glob import glob

package_name = 'ros2_foundations'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Student',
    maintainer_email='student@example.com',
    description='Module 1 examples for Physical AI & Humanoid Robotics book',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = ros2_foundations.talker:main',
            'listener = ros2_foundations.listener:main',
            'control_loop = ros2_foundations.control_loop:main',
            'ai_bridge = ros2_foundations.ai_bridge:main',
        ],
    },
)
