# SKILL LAB PRATICAL HACKATHON

Hand Gesture Recognition - A Computer Vision Application for Recognizing Traditional Yoga Hand Gestures TechWizards

> **Project Weight:** 100%  
> **Team Size:** 4/3 students  
> **Project Duration:** 16 hours  
> **Total Time Available:** 32 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---



# 1. Team Identity

## 1.1 Tech Wizards

## 1.2 Team Members

| Name                  | Primary Role                    | Secondary Role   | Strengths Brought to the Project |
| --------------        | ------------------------------- | --------------   | -------------------------------- |
| Purva Patil (Team Leader) |System Implementation | Testing, Coding | Electronics, Logical Thinking,Software|
| Amey Padwal           | Testing, Training              | Debugging        | Hardware Handling    |
| Animish Pradhan       | Documentation                   | Github           | Documentation|
| Avdhoot Dinkar        | Literature survey               | Hardware Support        | Research Knowlegde    |

## 1.3 Project Title

Hand Gesture Recognition- A Computer Vision Application for Recognizing Traditional Yoga Hand Gestures

## 1.4 One-Line Pitch

A webcam-based Hand Gesture Recognition system that identifies various hand gestures and specifically detects different traditional Yoga Mudras along with their meanings

## 1.5 Expanded Project Idea 

Yoga Mudras are traditional hand gestures used in yoga, meditation, and wellness practices. This project uses a webcam to recognize different yoga mudras by analyzing hand shape, contour area, and finger gaps using OpenCV. The system captures live video, processes the hand region, detects the gesture, and displays the mudra name along with its meaning on the screen.
The experience created by this project is an interactive yoga learning assistant. Beginners can place their hand in front of the camera and instantly know which mudra they are performing. The project involves Python, OpenCV, webcam-based image processing, HSV skin detection, contour detection, convex hull analysis, and rule-based classification.


# 2. Inspiration

## 2.1 References

List what inspired the project.

| Source Type | Title / Link                                                        | What Inspired You|
| ----------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------|
| Raspberry Pi   | https://www.raspberrypi.com/ | Use of low-cost embedded systems to build the project | 
| Research Paper | Real-time Recognition of Yoga Poses using computer Vision for Smart Health Care | Inspired the idea of using computer vision to detect yoga mudras and provide feedback |
|             |                                     |                                                                                           |

## 2.2 Original Twist
 
This project combines traditional yoga knowledge with modern computer vision. Instead of just detecting gestures, the system also explains the meaning of each mudra in real time. It acts as a beginner friendly learning assistant, allowing users to practice yoga mudras interactively using only a webcam. The focus on Indian cultural elements (yoga mudras) with low-cost hardware like Raspberry Pi makes it unique and practical

# 3. Project Intent

## 3.1 User Journey 

A user sits in front of the system where a Raspberry Pi is connected to a webcam and display. When the program starts, the Raspberry Pi runs the Python application and shows a live video feed on the screen with a guide box. The user places their hand inside the box and performs a yoga mudra. The Raspberry Pi captures the video through the webcam, processes each frame using OpenCV, and analyzes the hand shape.
The system identifies the mudra and displays its name along with its meaning on the screen. The Raspberry Pi acts as the main processing unit, handling image processing and decision making. The user can try different mudras and instantly learn their benefits. This creates an interactive and educational experience where low cost hardware and computer vision technology help users practice yoga correctly
                                                  

# 4. Definition of Success

## 4.1 Definition of “Usable”
The project is considered usable when a user can:
- Successfully place their hand in front of the webcam
- Get real time detection of at least 3–4 different Yoga Mudras
- See the mudra name and its meaning displayed clearly on the screen
- Use the system comfortably in normal room lighting with minimal errors


## 4.2 Minimum Usable Version

- Real time webcam input with a guide box
- Skin detection and hand contour extraction
- Recognition of minimum 3-4 Yoga Mudras
- Display of mudra name and short meaning on screen
- Basic "Unknown" gesture handling

## 4.3 Stretch Features

- Add more mudras
- Improve accuracy using Machine Learning
- Voice output 
- Add language support
- Add practice timer 
- GUI interface with buttons/menu

# 5. System Overview

## 5.1 Project Type

Check all that apply.

- [x] Electronics-based

- [ ] Mechanical

- [x] Sensor-based

- [ ] App-connected

- [ ] Motorized

- [ ] Sound-based

- [ ] Light-based

- [x] Screen/UI-based

- [ ] Fabricated structure

- [ ] Game logic based

- [ ] Installation

- [ ] Other:

## 5.2 High-Level System Description

The system is a Yoga Mudra Recognition using Hand Gestures Detection setup built using a Raspberry Pi and a USB webcam. The webcam acts as the input device, capturing live video of the user’s hand. The Raspberry Pi processes this video using Python and OpenCV. The captured frames are converted into HSV color space to detect skin regions, and contour detection is used to identify the hand shape. Based on contour area and convexity defects, the system classifies the gesture into different yoga mudras.

The output is displayed on a screen connected to the Raspberry Pi, where the detected mudra name and its meaning are shown in real time. The physical structure includes the Raspberry Pi unit, webcam, and display setup. The system does not require a mobile app, as all interaction happens directly through the screen interface, making it simple and self contained.

## 5.3 Input / Output Map

| System Part | Type | What It Does |
| -------- | -------- | -------- |
|  USB Webcam | Input	 | Captures live video of hand gestures |
|  Raspberry Pi | Processing  | Runs Python + OpenCV to process images |
|  OpenCV Software | Processing	 | Detects skin, contours, and classifies mudra |
|  Display (Monitor) | Output  | Shows video feed with detected mudra name |
|  User Hand | Input  | Performs yoga mudras |
---

# 6. System Design, Sketches and Visual Planning 

## 6.1 Concept Architecture/sketch/schematic

Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:

```md

```



## 6.2 Labeled Build Sketch/architecture/flow diagram/algorithm

Add a sketch with labels showing:

- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/95637f31-b4e7-4427-a9e1-4b63fbeb0ac5" />

## 6.3 Approximate Dimensions

| Dimension        | Value   |
| ---------------- | ------- |
| Length           | `16 cm` |
| Width            | `16 cm` |
| Height           | `8 cm`  |
| Estimated weight | `400 g` |

---

# 7. Electronics Planning

## 7.1 Electronics Used

| Component                 | Quantity | Purpose                               |
| ------------------------- | --------| ------------------------------------- |
| Raspberry Pi              | 1      |    Main processing unit    |
| Camera (Webcam)           | 1      | Captures Hand gesture      |
| Display (Monitor)         | 1      | Displays Output & UI      |
| Power Adapter        | 1      | Power Supply      |

## 7.2 Wiring Plan

The USB webcam is directly connected to the Raspberry Pi via a USB port. The Raspberry Pi is powered using a standard power adapter. A display monitor is connected through HDMI to show the live camera feed and detected results. No complex wiring is required, as the system relies mainly on software processing. All components operate through simple plug-and-play connections, making the setup compact and easy to use.

## 7.3 Circuit Diagram/architecture diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="" src="" />


# 7.4. Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | 5V DC Adapter (USB Type-C) for Raspberry Pi                                                                                                               |
| Voltage required | 5V regulated supply for Raspberry Pi and USB webcam                                                                  |
| Current concerns | High CPU usage during real-time processing may increase current draw and cause heating                                      |
| Safety concerns  | Use certified adapter, avoid overloading USB ports, ensure proper ventilation to prevent overheating |

---

# 8. Software Planning/

## 8.1 Software Tools

| Tool / Platform                | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |

| `[Python/PyGame/OpenCV]`       | `Track markers, game logic, create projection` |
| `[Fusion/Blender/Illustrator]` | `[Prototyping structure]`                      |
|                                |                                                |

## 8.2 Software Logic/Algorithm

Describe what the code must do.

Include:

- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`

- **Sample Startup behavior:**  
  The Raspi/FPGA initializes motor pins, PWM control, and starts a WiFi access point with a web server. The laptop initializes camera input, tracking system, and projection mapping.
- **Input handling:**  
  Movement commands are received from the laptop (pygame sends http requests)
- **Sensor reading:**  
  The camera continuously captures frames, and OpenCV detects ArUco markers to determine the car’s position and orientation.
- **Decision logic:**  
  The system maps the car’s position into a virtual coordinate system and checks for nearby obstacles or collisions. If movement is valid, the command is allowed; if not, it is blocked or replaced with a feedback action (like a slight shake).
- **Output behavior:**  
  The ESP32 drives the motors using PWM signals to control speed and direction. The projector displays the updated game environment, including obstacles, targets, and feedback visuals.
- **Communication logic:**  
  The laptop sends HTTP requests (e.g., `/forward`, `/left`) to the ESP32 over WiFi. The ESP32 parses these commands and executes motor actions.
- **Reset behavior:**  
  If no command is received within a short timeout, the ESP32 stops the motors. The game resets when a level is completed or restarted.`

## 8.3 Code Flowchart

Insert a flowchart showing your code logic.

Suggested sequence:

- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1600" height="1200" alt="image" src="" />
<img width="1600" height="1200" alt="image" src="" />




# 9. Bill of Materials

## 9.1 Full BOM

| Item                             | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec               | Why This Choice?          |
| -------------------------------- | --------:| ------- | ------------ | --------------:| ----------------------------- | ------------------------- |
| `[RASPI]`                        | `1`      | `Yes`   | `No`         | `0`            | 4GB RAM board                 | Compact, low-cost device for final deployment` |
| Webcam              | `[1]`    | `No` | `Yes`       | `1000`            | 720p/1080p USB Camera                     | Easy to use, captures real-time hand gestures clearly  |

## 9.2 Material Justification

The materials and components for this project were selected based on simplicity, cost, and ease of use. A webcam is used because it is easily available and can capture real-time hand movements clearly. The software libraries OpenCV were chosen because they make image processing and hand detection much easier and faster, even for beginners. Python was used as the programming language since it is simple to understand and works well with these libraries. For the final implementation, a Raspberry Pi 4 Model B can be used because it is compact, affordable, and allows the system to run independently without a full computer. Overall, all components were selected to keep the project efficient, low-cost, and easy to implement.

## 9.3 Items You chose

| Item                 | Why Needed               | Purchase Link | Latest Safe Date to Procure | Status       |
| -------------------- | ------------------------ | ------------- | --------------------------- | ------------ |
| Ras pi  | Main Body of our Project   | NA     |NA               | NA |
| Webcam     | Captures real-time hand gestures |NA | NA           |NA |

## 9.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
|  Webcam       |1000                     |
|Raspberry Pi 4 Model B      | 6000                     |


## 9.5 Budget Reflection

The major cost of the project comes from the Raspberry Pi and the webcam. If the overall cost needs to be reduced, the Raspberry Pi can be substituted with a personal laptop or desktop system for development and testing, as the core processing can be performed using software tools like OpenCV. Additionally, instead of purchasing a new webcam, an already available laptop camera or a shared external webcam can be used. These alternatives significantly reduce the project cost while still allowing successful implementation and testing of the system 

---

# 10. Planning the Work

## 10.1 Team Working Agreement

  
The project was divided among four team members based on responsibilities:

Member 1: Installation of OS, setup of required libraries, execution of code, and making necessary modifications.

Member 2: Development of software prototype, testing on laptop, and partial documentation work.

Member 3: Topic finalization, improvement suggestions, and research paper analysis.

Member 4: GitHub repository management, documentation updates, and debugging support.


Decisions were taken through group discussions. Final decisions were made based on feasibility, performance, and project requirements after considering suggestions from all members.

Progress was tracked regularly through:
Weekly discussions
Code execution and testing results
Updates on GitHub repository
If any task was delayed:
Work was redistributed among team members
Priority tasks were completed first
Extra time was allocated to ensure deadlines were met
Documentation was maintained and updated regularly on GitHub
Each member contributed to their respective sections
Final documentation was reviewed and refined collectively



## 10.2 Task Breakdown

| Task ID | Task                    | Owner    | Estimated Hours | Deadline     | Dependency | Status |
| ------- | ----------------------- | -------- | ---------------:| ------------ | ---------- | ------ |
| T1      |Problem Identification & Idea Finalization   | Purva | 1           | Day 1  | `None`     | `Done` |
| T2      | System Design (Architecture + Flowchart)   | Amey | 2            | Day 1  | T1     | `Done` |
| T3      | Implementation (OpenCV + MediaPipe Code)    |Avdhoot | 4             | Day1  | T2     | `Done` |
| T4      | Testing, Output & Documentation    | Animesh | 4             |Day 2  | T1     | `Not Done` |


## 10.3 Responsibility Split

| Area                 | Main Owner     | Support Owner |
| -------------------- | ----------     | ------------- |
| Electronics, Logic Thinking        | Purva  | Amey      |
|Coding & Testing         | Amey , Avdhoot          | Purva          |
| Integration    |Avdhoot           | Amey          |
| Documentation        | Animesh          |Purva        |

---

# 11 hour Milestones

## 11.1 8-hour Plan(tentetively you may set)

### Bi Hour 1 — Plan and De-risk

Expected outcomes:

- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Bi Hour 2 — Build Subsystems

Expected outcomes:

- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Bi Hour 3 — Integrate

Expected outcomes:

- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Bi Hour 4 — Refine and Finish

Expected outcomes:

- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 12.2  Update Log

| Days   | Planned Goal   | What Actually Happened | What Changed   | Next Steps     |
| ------ | -------------- | ---------------------- | -------------- | -------------- |
| Day 1 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 2 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 3 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 4 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |

---

# 13. Risks and Unknowns

## 13.1 Risk Register

| Risk                                                            | Type         | Likelihood | Impact   | Mitigation Plan                                                                       | Owner                |
| --------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------------------------------------------------------- | -------------------- |
| WiFi connection between laptop and ESP32 becomes unstable       | `Technical`  | `Medium`   | `High`   | Keep ESP32 close, ensure stable power supply, reduce network load, add fail-safe stop | `[Gopal]`           |


## 13.2 Biggest Unknown Right Now

What is the single biggest uncertainty in your project at this stage?

**Response:**  


---

# 14. Testing 

## 14.1 Technical Testing Plan

| What Needs Testing     | How You Will Test It                                                                 | Success Condition                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `[Wifi connection]`    | `[Check if motor spins via app button]`                                              | `[Both motors accurately respond to wifi signals]`                                                   |
                       |
## 14.2 Testing and Debugging Log

| Date          | Problem Found                         | Type         | What You Tried                                | Result               | Next Action                                    |
| ------------- | ------------------------------------- | ------------ | --------------------------------------------- | -------------------- | ---------------------------------------------- |
| `18th April`  | `Car not balancing properly`          | `Mechanical` | `Add low-friction caster support to one side` | `Worked`             | `improve caster structure`                     |


## 14.3 Playtesting Notes

| Tester      | What They Did                        | What Confused Them                    | What They Enjoyed                         | What You Will Change                          |
| ----------- | ------------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| `Gopal` | `Tried navigating through obstacles` | `Some obstacles ewren't clear enough` | `Liked projection + real car interaction` | `Add a slight red highlight around obstacles` |


---

# 15. Build Documentation

## 15.1 Fabrication Process(if any)

Describe how the project was physically made.

Include:

- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The fabrication process involved designing, manufacturing, assembling, and refining both the physical structure and electronic integration of the system.`

`Design (CAD Modeling):
The initial model was created using CAD software, where components were designed based on the actual dimensions of the electronic parts. This ensured accurate fitting and minimized errors during assembly.
Cutting (Laser Cutting):
The designed parts were fabricated using laser cutting techniques. Sheets were cut precisely according to the CAD model to create the structural base and mounts for components.`

`Components were fixed using adhesives and mechanical supports. Certain parts were intentionally kept modular (not permanently fixed) to allow easy replacement and modification of electronics.
Surface Finishing:
Some parts were sanded to smooth rough edges after cutting. Sawdust mixed with adhesive was used to fill gaps and uneven edges, improving structural finish. The final structure was then painted for better aesthetics and durability.`

`Environment Setup (Dark Room Fabrication):
To enhance projection visibility, a controlled dark environment was created using Z-boards, paper sheets, and bedsheets. This minimized external light interference and improved projection clarity.
Revisions and Iterations:
Multiple adjustments were made throughout the process, including refining alignment, improving structural stability, repositioning components, and optimizing the interaction between the physical car and projected environment.`

## 16 Build Photos

Add photos throughout the project.

Suggested images:

- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- <img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM (1)" src="https://github.com/user-attachments/assets/74baa570-5770-483e-be6d-d2f03386e37c" />





# 17. Final Outcome

## 17.1 Final Description

Describe the final version of your project.

**Response:**  


## 17.2 What Works Well



## 17.3 What Still Needs Improvement


## 17.4 What Changed From the Original Plan

How did the project change from the initial idea?

**Response:**  


---

# 18. Reflection

## 18.1 Team Reflection

What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  


## 18.2 Technical Reflection

What did you learn about:

- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  


## 18.3 Design Reflection

What did you learn about:

- designing ,
- delight,
- clarity,
- physical interaction,
- understanding,
- iteration?

**Response:**  


## 18.4 If You Had One More hour

What would you improve next?

**Response:**  

` `

---

# 19. Final Submission Checklist

Before submission, confirm that:

- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written
<img width="1131" height="1600" alt="image" src="" />

---


---


