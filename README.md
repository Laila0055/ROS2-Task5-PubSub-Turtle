 Publisher/Subscriber and Turtle Square Movement

Part 1: Talker and Listener
Created a Publisher (talker.py) and Subscriber (listener.py) using ROS2, 
sending a custom message instead of "hello world":
"Hello from Laila's ROS2 project"

The talker publishes the message every second on the "chatter" topic, 
and the listener subscribes to the same topic and prints the received messages.

Commands used:
python3 talker.py
python3 listener.py

Part 2: Turtle Square Movement
Modified the turtle simulation code so the turtle moves in a square path 
instead of a circle, by alternating between moving forward and turning 
at fixed time intervals.

Commands used:
ros2 run turtlesim turtlesim_node
python3 turtle_square.py

Result
Both parts were successfully implemented and tested, with screenshots 
and video attached as proof.
