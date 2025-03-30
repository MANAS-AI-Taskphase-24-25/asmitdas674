from setuptools import setup

package_name = 'simple_chat_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],  # Ensures Python finds the package
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asmitdas_ubu',
    maintainer_email='your_email@example.com',
    description='A simple chat interface using ROS2 publishers and subscribers',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'chat_publisher = simple_chat_interface.chat_publisher:main',
            'chat_subscriber = simple_chat_interface.chat_subscriber:main',
        ],
    },
)

