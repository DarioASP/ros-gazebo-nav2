import rclpy #ros comand line python library
from rclpy.node import Node #ros node class
from std_msgs.msg import String

class CustomListener(Node):
    def __init__(self, node_name = 'custom_listener'):
        super().__init__(node_name) #initialize the node with a name
        self.subscription = self.create_subscription(String, 'chisme', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibí: [{msg.data}]')#que es el get-logger?
        

def main():
    rclpy.init()#acepta argumentos de entrada
    myNode = CustomListener()
    rclpy.spin(myNode)#tiempo de vida, el spin es el basico y se ejecuta hasta q matemos
    rclpy.shutdown()

if __name__ == "main":
    main()
