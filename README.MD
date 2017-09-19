This project is purely for experimenting with ROS architecture and code.
Everything in here is subject to change once we've established the conceptual design,
partially based on the knowledge gained through experimenting.

Usage:
```bash
cd $proj
catkin_make
source $proj/devel/setup.bash

roscore
rosrun minor <command>
```

Ex:
```bash
roscore
rosrun minor scripts/arduino.py
rosrun minor scripts/keyboard.py
rosrun minor scripts/display.py

[Connect android to roscore]
rosrun minor scripts/camera.py
```

Current nodes consist of:
```
arduino.py <--[controller]--  keyboard.py
            ---[sensors]----> display.py
android     -[camera/image]-> camera.py
```

The keyword between [] represents the ROS topic name.
All topics that arduino communicates with should be using ROSSerial (USB) at a later stage.

A rough description of their purpose and responsability:
- arduino.py: mock Arduino sensor input and command sink
- keyboard.py: send basic controls such as Left/Right, pump On/Off to Arduino
- display.py: display sensor output from Arduino
- Android: publish camera stream on [/camera/image/compressed] ([apk](camera.apk) included in repo, [source](https://github.com/rosjava/android_core/tree/kinetic/android_tutorial_camera))
- camera.py: display a preview of camera input on [/camera/image/compressed]
