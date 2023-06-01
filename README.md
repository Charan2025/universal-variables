# Moby_Dock

Repository Structure

The repository contains the following files and directories:

/controller.py: This file converts all the PS4 Controller Components to byte values. 

/transmitt.py: This file transmits the Controller Data to the iRobot VIA Hexadecimal vals. 

/variables.py: This file contains all the global variables we utilized and there default values. 

README.md: This file, which provides an overview of the project. For more information about the functionality
of Team Moby Dock's Project, please reference our diagram: https://rb.gy/hj9re

**NOTE** 

These files encapsulate the final deliverables of my side of the Cybot Mission & Docking Project 

--------------------------------------------------------------------------------------------------------------------------

Project Description

This project was developed as a final project for the Embedded Systems class (CPR E 288) by Team Moby Dock at ISU. 
The goal was to create an autonomously guided system for iRobots (Roomba) to navigate within a designated 
area while adhering to specific constraints. The system needed to navigate between four thin pillars, stay within 
predefined boundaries, avoid tall objects, touch short objects only once, and eventually dock.


Team Moby Dock identifies three main areas: Cybot Mission Algorithms, GUI Design, and Dynamic Controlling. 
Our group concentrated on developing algorithms for detecting and avoiding obstacles w/ Embedded C Language. 
Additionally, we leveraged WebSockets and a Python GUI Design to create a user-friendly interface. On the hardware 
side, we used a PS4 Controller to control the iRobot (MY SIDE). The controlled linked VIA Bluetooth to a Raspberry Pi B+ while
the Pi connected w/ the Baseboard of the iRobot VIA Universal Asynchronous Receiver-Transmitter Communication (UART).

--------------------------------------------------------------------------------------------------------------------------

Project Implementation

The project required a combination of hardware and software skills to achieve the desired functionality. The following steps were 
followed to develop the system:

1. Understanding the Requirements: Thoroughly review the project requirements to gain a clear understanding of the desired features 
   and constraints. In our case, we had to ensure our ideas releated to class material and were developable in our constrained time.
   Furthermore, we had to ensure our iRobot could autonomously avoid obstacles and be able to dock without supervision. We also had
   to analyze how our bonus features of the PS4 Controller, Pi, GUI, and Websockets would function in tandem. 

2. Designing the Hardware Setup: Determine the necessary hardware components for the project, such as iRobot Sensors, Ps4 Cotnroller, 
   Rasberry Pi B+, and any additional peripherals required for navigation and object detection.

3. Implementing the Software: Develop the software logic and algorithms required for autonomous navigation, object detection, and 
   decision-making processes. This involves programming the iRobot and integrating the sensors into the system. Additionally, we
   utilized to Python to interface the Pi w/ the iRobot Baseboard. Once we configured the controller and set all the global variables,
   we forwarded hexadecimal values to the iRobot VIA UART Protocol, allowing the other half of our group to manipulate the raw data 
   and control specific actions on the bot. We defined and converted individual component values of the left/right joystick, square, 
   triangle, and circle buttons (e.g., the triangle button toggles between autonomous and manual mode, the square button initiates a 
   scan, the circle button plays music, the left joystick controls the bot's movement in the up, down, left, and right directions, 
   and the right joystick assists w/ moving our target) to raw hex data, which we sent over via UART to achieve this. Our Python GUI 
   and Websockets were also designed in the our integral third step. 

4. Testing and Iteration: Conduct rigorous testing to validate the system's performance. Identify any issues or limitations and 
   iterate on the design to improve its functionality and reliability. RESULT: OUR PROJECT DEMOED SUCCESSFULLY!

---------------------------------------------------------------------------------------------------------------------------------

Our Inspiration For The Project

The Crew Dragon is a human-rated spacecraft designed and manufactured by SpaceX. It is designed to transport astronauts 
to and from the International Space Station (ISS) and other low-orbit destinations. The Crew Dragon is part of NASA's 
Commercial Crew Program, which aims to provide astronauts with safe, reliable, and cost-effective access to space. The 
spacecraft can carry up to 7 passengers and has a modular design that can be configured for both crew and cargo missions.

The Crew Dragon is equipped with an intuitive GUI w/ multiple displays, including a central touchscreen display and several smaller 
displays throughout the capsule. The touchscreen controls various functions: the spacecraft's thrusters, life support systems, and 
comms. It also features an autonomous docking system that enables it to dock w/ the ISS; however, the astronauts can still take 
control of the spacecraft if needed and re-steer onto its destination. 

C. Gohd, “The touchscreen controls of SpaceX’s Crew Dragon give astronauts a sci-fi way to fly in space,” Space.com, May 29, 2020. https://www.space.com/spacex-crew-dragon-touchscreen-astronaut-thoughts.html
S. O’Kane, “Watch NASA astronauts fly SpaceX’s Crew Dragon using touchscreens,” The Verge, May 30, 2020. https://www.theverge.com/2020/5/30/21275753/nasa-spacex-astronauts-fly-crew-dragon-touchscreen-controls
“This is certainly different’: astronauts on controlling the Dragon spacecraft,” May 04, 2020. https://techcrunch.com/2020/05/04/this-is-certainly-different-astronauts-on-controlling-the-dragon-spacecraft-via-touchscreen/
