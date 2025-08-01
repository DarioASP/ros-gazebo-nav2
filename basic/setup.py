from setuptools import find_packages, setup

package_name = 'basic'

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
    maintainer='Dario',
    maintainer_email='dario5feb6b@outlook.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [#Instalar nodos
            'custom_dario_talker = basic.custom_talker:main',
            'mover_tortuga = basic.tortuga:main',
            'custom_dario_listener = basic.Custom_listener:main'
        ],
    },
)
