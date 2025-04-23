# Test Cases for Vehicle Speed Monitoring and Fault Logging System

| TC ID | Requirement ID | Description                                                | Input/Condition                          | Expected Output                     |
|-------|----------------|------------------------------------------------------------|------------------------------------------|-------------------------------------|
| TC01  | R1             | Validate speed reading every 100 ms                        | Simulate varying speeds                  | Speed updated every 100 ms          |
| TC02  | R2             | Detect high speed fault (>120 km/h)                        | Speed = 130 km/h                          | Log "High Speed Fault"              |
| TC03  | R2             | No fault if speed is under threshold                       | Speed = 100 km/h                          | No fault logged                     |
| TC04  | R3             | Detect idle fault after 5 minutes of 0 speed               | Speed = 0 for 5+ minutes                  | Log "Idle Fault"                    |
| TC05  | R3             | No idle fault before 5 minutes                             | Speed = 0 for 4 minutes 59 seconds        | No fault logged                     |
| TC06  | R4             | Log event with timestamp                                   | Any fault condition                      | Log contains correct timestamp      |
| TC07  | R5             | Simulation loop should run continuously                    | Run for 10 minutes                       | Simulation completes without crash  |
| TC08  | R6             | Export fault logs to file                                  | Generate faults, end simulation          | `fault_log.csv` or `.txt` created   |
| TC09  | NF1            | Verify script runs on Python 3.x                           | Run with `python3 ecu_simulator.py`      | No syntax or runtime errors         |
| TC10  | NF2            | Test simulation with pytest                                | Run pytest on test file                  | All tests pass                      |
| TC11  | NF3            | Verify repo has version control                            | Check GitHub commit history              | Changes properly committed          |
