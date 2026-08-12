import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.state = 'forward'
        self.counter = 0
        self.forward_ticks = 20
        self.turn_ticks = 16

    def timer_callback(self):
        msg = Twist()
        if self.state == 'forward':
            msg.linear.x = 2.0
        else:
            msg.angular.z = 1.0

        self.publisher_.publish(msg)
        self.counter += 1

        if self.state == 'forward' and self.counter >= self.forward_ticks:
            self.state = 'turn'
            self.counter = 0
        elif self.state == 'turn' and self.counter >= self.turn_ticks:
            self.state = 'forward'
            self.counter = 0

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSquare()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
