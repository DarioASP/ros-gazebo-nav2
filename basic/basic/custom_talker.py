import rclpy #ros comand line python library
from rclpy.node import Node #ros node class
from std_msgs.msg import String

class CustomTalker(Node):
    def __init__(self, node_name = 'custom_talker'):
        super().__init__(node_name) #initialize the node with a name
        self.get_logger().info("Nodo creanding")
        self.publisher_ = self.create_publisher(String, 'chisme', qos_profile=10)
        self.timer_ = self.create_timer(1, self.timer_callback)
        self.i = 0

    def timer_callback(self):

        mensaje = String()
        mensaje.data = f"Holiwis{self.i}"
        self.publisher_.publish(mensaje)
        self.get_logger().info(f"Estoy publicando este mensaje: [{mensaje.data}]")
        self.i += 1
        

def main():
    rclpy.init()#acepta argumentos de entrada
    myNode = CustomTalker()
    rclpy.spin(myNode)#tiempo de vida, el spin es el basico y se ejecuta hasta q matemos
    rclpy.shutdown()

if __name__ == "main":
    main()
