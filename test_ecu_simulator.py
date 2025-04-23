import pytest
from ecu_simulator import log_fault

# Test if fault is logged when speed exceeds the threshold
def test_high_speed_fault():
    log_fault(130, "High Speed Fault")  # simulate a high-speed fault
    with open("logs/fault_log.csv", "r") as f:
        logs = f.readlines()
    assert "High Speed Fault" in logs[-1]  # Check if the last log entry contains "High Speed Fault"

# Test if idle fault is logged after 5 minutes of 0 speed
def test_idle_fault():
    # Simulate idle speed (0 km/h) and timestamp 5+ minutes
    log_fault(0, "Idle Fault")
    with open("logs/fault_log.csv", "r") as f:
        logs = f.readlines()
    assert "Idle Fault" in logs[-1]  # Check if the last log entry contains "Idle Fault"
    
# Add more tests as needed for other features or faults...