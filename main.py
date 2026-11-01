import time
import os
import sys

# --- Configuration ---
SIMULATED_RECORDING_DURATION = 8 # seconds for each recording session
MONITOR_INTERVAL = 2 # seconds between checks for triggers
START_TRIGGER_FILE = "start_recording_now.trigger"
STOP_TRIGGER_FILE = "stop_recording_now.trigger"

# --- Simulation State ---
is_recording = False
recording_start_time = 0

print("--- Simulated Ghostly Screen Recorder Monitor ---")
print(f"This script simulates a screen recorder that starts/stops based on internal logic or external triggers.")
print(f"To manually start recording: create a file named '{START_TRIGGER_FILE}' in this directory.")
print(f"To manually stop recording: create a file named '{STOP_TRIGGER_FILE}' in this directory.")
print(f"Recording will also stop automatically after {SIMULATED_RECORDING_DURATION} seconds if started.")
print("Press Ctrl+C to exit.")
print("-------------------------------------------------")

try:
    while True:
        current_time = time.time()

        # --- Check for START triggers ---
        if not is_recording:
            # External trigger: user creates a specific file
            if os.path.exists(START_TRIGGER_FILE):
                print(f"\n[{time.strftime('%H:%M:%S')}] Screen recorder STARTED recording! (Triggered by '{START_TRIGGER_FILE}')")
                is_recording = True
                recording_start_time = current_time
                os.remove(START_TRIGGER_FILE) # Clean up the trigger file after use
            # Internal trigger: a simple time-based condition (simulating a schedule or event)
            # This condition ensures it triggers roughly every 20 seconds, only once per interval.
            elif int(current_time) % 20 == 0 and int(current_time) != 0: 
                if not hasattr(sys.modules[__name__], '_last_internal_start_trigger_time') or \
                   current_time - sys.modules[__name__]._last_internal_start_trigger_time > MONITOR_INTERVAL * 2:
                    print(f"\n[{time.strftime('%H:%M:%S')}] Screen recorder STARTED recording! (Internal scheduled trigger)")
                    is_recording = True
                    recording_start_time = current_time
                    sys.modules[__name__]._last_internal_start_trigger_time = current_time

        # --- Check for STOP triggers ---
        if is_recording:
            # External stop trigger: user creates a specific file
            if os.path.exists(STOP_TRIGGER_FILE):
                print(f"\n[{time.strftime('%H:%M:%S')}] Screen recorder STOPPED recording! (Triggered by '{STOP_TRIGGER_FILE}')")
                is_recording = False
                os.remove(STOP_TRIGGER_FILE) # Clean up the trigger file after use
            # Internal stop trigger: recording duration limit reached
            elif current_time - recording_start_time >= SIMULATED_RECORDING_DURATION:
                print(f"\n[{time.strftime('%H:%M:%S')}] Screen recorder STOPPED recording! (Duration limit reached)")
                is_recording = False
        
        # Provide ongoing feedback when idle or recording
        if not is_recording:
            # Display remaining time until the next potential internal start trigger
            sys.stdout.write(f"\r[{time.strftime('%H:%M:%S')}] Monitoring... (Next internal start check in ~{20 - (int(current_time) % 20)}s)   ")
            sys.stdout.flush()
        else:
            # Display remaining recording time
            sys.stdout.write(f"\r[{time.strftime('%H:%M:%S')}] RECORDING! (Time left: {int(SIMULATED_RECORDING_DURATION - (current_time - recording_start_time))}s)   ")
            sys.stdout.flush()

        time.sleep(MONITOR_INTERVAL)

except KeyboardInterrupt:
    print("\nSimulation interrupted by user.")
finally:
    # Clean up any remaining trigger files on exit
    if os.path.exists(START_TRIGGER_FILE):
        os.remove(START_TRIGGER_FILE)
    if os.path.exists(STOP_TRIGGER_FILE):
        os.remove(STOP_TRIGGER_FILE)
    print("Cleanup complete. Goodbye!")
