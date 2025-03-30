import rclpy  # imports ROS2 library for programming in Python
from rclpy.node import Node
from std_msgs.msg import String  # a dependency necessary for generating messages

class ChatPublisher(Node):
    def __init__(self):  # constructor
        super().__init__('chat_publisher')
        self.publisher_ = self.create_publisher(String, 'chat_topic', 10)  # Queue size = 10
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = input("You: ")  # Take message from the user
        self.publisher_.publish(msg)
        self.get_logger().info(f"Sent: {msg.data}")

def main():
    rclpy.init()  # Initializes ROS2
    node = ChatPublisher()  # Creates the publisher node
    rclpy.spin(node)  # Keeps node alive to send messages
    node.destroy_node()  # Cleans up before shutdown
    rclpy.shutdown()

if __name__ == "__main__":
    main()

