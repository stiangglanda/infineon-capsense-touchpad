import serial
import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

# Non-blocking serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0)
ser.reset_input_buffer()

last_x, last_y = None, None
buffer = ""

print("Listening for touchpad data...")

while True:
    # Read whatever is available
    data = ser.read(ser.in_waiting or 1)
    buffer += data.decode(errors="ignore")

    # Process complete lines
    while '\n' in buffer:
        line, buffer = buffer.split('\n', 1)
        line = line.strip()

        if not line:
            continue

        if line.startswith("T:"):
            coords = line[2:].split(",")
            if len(coords) < 2:
                continue

            try:
                x = int(coords[0])
                y = int(coords[1])
            except ValueError:
                continue

            if last_x is not None:
                dx = x - last_x
                dy = y - last_y
                speed = 1.5
                pyautogui.moveRel(-dx * speed, -dy * speed, duration=0)

            last_x, last_y = x, y

        elif line == "R":
            last_x, last_y = None, None