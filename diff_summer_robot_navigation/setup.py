from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'diff_summer_robot_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #Esta línea agrega los archivos .launch.py
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dario',
    maintainer_email='dario5feb6b@outlook.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'set_inital_pose = diff_summer_robot_navigation.set_initial_pose:main',
            'clicked_nav = diff_summer_robot_navigation.clicked_nav:main'
        ],
    },
)   
