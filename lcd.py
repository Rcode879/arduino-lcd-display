from pyfirmata import Arduino, util, STRING_DATA

# Connect to your Arduino (adjust the port name as needed)
board = Arduino('COM3')

# Send a string to display on the LCD
def display_message(text):
    if text:
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))

# Example usage
display_message("Hello, Arduino!")

# Keep your script running
while True:
    pass
