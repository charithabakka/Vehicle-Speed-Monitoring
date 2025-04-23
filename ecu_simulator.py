import time
import random
from datetime import datetime

# Constants
HIGH_SPEED_THRESHOLD = 120  # km/h
IDLE_TIME_THRESHOLD = 5 * 60  # 5 minutes in seconds
LOG_FILE = "logs/fault_log.csv"

# Track idle time
last_movement_time = time.time()

# Create log file
def init_log():
    with open(LOG_FILE, "w") as f:
        f.write("Timestamp,Speed (km/h),Fault\n")

def log_fault(speed, fault):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp},{speed},{fault}\n")
        print(f"[LOGGED] {fault} at {speed} km/h")

def simulate_speed():
    return random.randint(0, 150)  # Simulated speed

def run_simulation(duration=60):
    global last_movement_time
    print("Starting ECU Simulation...")

    start_time = time.time()
    init_log()

    while time.time() - start_time < duration:
        speed = simulate_speed()
        print(f"Speed: {speed} km/h")

        # High speed fault
        if speed > HIGH_SPEED_THRESHOLD:
            log_fault(speed, "High Speed Fault")

        # Idle fault
        if speed == 0:
            if time.time() - last_movement_time >= IDLE_TIME_THRESHOLD:
                log_fault(speed, "Idle Fault")
        else:
            last_movement_time = time.time()

        time.sleep(1)  # Simulate 1 second interval

    print("Simulation ended.")

if __name__ == "__main__":
    run_simulation(120)  # Run for 2 minutes
