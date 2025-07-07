from setuptools import find_packages, setup

package_name = 'ros2_inter_node_practice'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dario',
    maintainer_email='dario5feb6b@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['camera_pub = ros2_inter_node_practice.camera_publisher:main', 
                            'img_proc = ros2_inter_node_practice.image_processor:main',
        ],
    },
)
