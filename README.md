# 🚀 Moby_Dock  

### Repository Overview  
This repository contains the final deliverables for the **Cybot Mission & Docking Project**, developed as part of the Embedded Systems class (CPR E 288) by **Team Moby Dock** at ISU.  

#### Structure:  
- **`controller.py`**: Converts PS4 controller components to byte values.  
- **`transmitt.py`**: Transmits controller data to the iRobot using hexadecimal values.  
- **`variables.py`**: Defines global variables with default values.  
- **`README.md`**: Provides an overview of the project.  
  [Project Diagram](https://rb.gy/hj9re)  

---

## 📚 Project Description  
The goal of the project was to create an **autonomously guided system** for an iRobot (Roomba) to navigate within a designated area, adhering to constraints:  
- Navigate between thin pillars, avoid tall objects, touch short objects only once, and dock autonomously.  

Our team focused on:  
1. **Cybot Mission Algorithms**: Obstacle detection/avoidance using Embedded C.  
2. **GUI Design**: Python and WebSockets for user-friendly control.  
3. **Dynamic Controlling**: Integration of a PS4 controller via Bluetooth to a Raspberry Pi B+, connected to the iRobot's baseboard via UART.

---

## 🛠️ Implementation  

1. **Understanding Requirements**:  
   Ensured alignment with class material and project constraints. Developed autonomous navigation and docking capabilities while integrating bonus features (PS4 controller, Raspberry Pi, GUI).  

2. **Hardware Design**:  
   Utilized iRobot sensors, PS4 controller, Raspberry Pi B+, and UART communication for efficient control.  

3. **Software Development**:  
   - Programmed navigation algorithms and obstacle detection in Embedded C.  
   - Configured the PS4 controller to send raw hex data (e.g., toggle modes, control bot movement, initiate scans).  
   - Developed a Python GUI and WebSocket interface for seamless control.  

4. **Testing & Iteration**:  
   Conducted rigorous testing to validate performance. Result: **Successful project demo!**  

---

## 🛰️ Inspiration  
The **Crew Dragon** by SpaceX, with its intuitive GUI, autonomous docking system, and manual override capability, inspired our project. We aimed to replicate its innovative features within our iRobot system.  

> *“The touchscreen controls of SpaceX’s Crew Dragon give astronauts a sci-fi way to fly in space.”*  
> – [Space.com](https://www.space.com/spacex-crew-dragon-touchscreen-astronaut-thoughts.html)  

---
