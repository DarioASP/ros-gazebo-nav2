import rclpy #ros comand line python library
from rclpy.node import Node #ros node class
from geometry_msgs.msg import Twist

class CustomTalker(Node):
    def __init__(self, node_name = 'custom_talker'):
        super().__init__(node_name) #initialize the node with a name
        self.get_logger().info("Nodo creanding")
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', qos_profile=10)
        self.timer_ = self.create_timer(1, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        mensaje = Twist()
        mensaje.linear.x=3.0
        mensaje.linear.y=0.5
        mensaje.linear.z = 0.0
        mensaje.angular.x = 1.5
        mensaje.angular.y=0.5
        mensaje.angular.z=2.0  
        self.publisher_.publish(mensaje)
        self.get_logger().info(f"Estoy publicando este mensaje: [{mensaje.linear} {mensaje.angular}]")
        self.i += 1
        

def main():
    rclpy.init()#acepta argumentos de entrada
    myNode = CustomTalker()
    rclpy.spin(myNode)#tiempo de vida, el spin es el basico y se ejecuta hasta q matemos
    rclpy.shutdown()

if __name__ == "main":
    main()
