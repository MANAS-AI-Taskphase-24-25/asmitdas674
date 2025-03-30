import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChatSubscriber(Node):
    def __init__(self):
        super().__init__('chat_subscriber')
        self.subscription = self.create_subscription(
            String, 'chat_topic', self.receive_message, 10
        )
        self.subscription  # Prevent unused variable warning

    def receive_message(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main():
    rclpy.init()
    node = ChatSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

