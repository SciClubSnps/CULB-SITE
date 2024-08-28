import tkinter as tk
import serial
import time

def send_message():
    message = message_entry.get()
    if message:
        arduino.write((message + '\n').encode())  # Send the message followed by a newline
        output_label.config(text=f"Sent: {message}")
        message_entry.delete(0, tk.END)

# Initialize the serial connection (adjust COM port and baud rate if necessary)
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)  # Replace 'COM3' with your Arduino's port

# Set up the GUI
root = tk.Tk()
root.title("Message Sender")

# Label
tk.Label(root, text="Enter your message:").pack(pady=10)

# Entry field
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="")
output_label.pack(pady=5)

# Start the GUI loop
root.mainloop()

# Close the serial connection when the GUI window is closed
arduino.close()
