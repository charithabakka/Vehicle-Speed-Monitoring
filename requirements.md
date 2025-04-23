# Vehicle Speed Monitoring and Fault Logging System – Requirements
## 1. Project Overview
A simulated ECU system that monitors vehicle speed, logs specific fault conditions, and outputs logs for analysis.

## 2. System Functions

| ID  | Requirement Description |
|-----|--------------------------|
| R1  | The system shall read simulated vehicle speed every 100 milliseconds. |
| R2  | The system shall log a **"High Speed Fault"** if speed exceeds 120 km/h. |
| R3  | The system shall log an **"Idle Fault"** if speed is 0 km/h continuously for more than 5 minutes. |
| R4  | The system shall maintain a log of all events with timestamps. |
| R5  | The system shall run as a simulation loop for a defined period or until manually stopped. |
| R6  | The system shall export the fault logs to a `.txt` or `.csv` file. |

## 3. Non-functional Requirements

| ID  | Description |
|-----|-------------|
| NF1 | The system should be written in Python 3.x |
| NF2 | The simulation must be testable using `pytest` or a similar test framework. |
| NF3 | Code must be pushed to GitHub with clear version control. |