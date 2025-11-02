# ------------------------------------------------------------------------------------------
# CS50 Python
# Week 0
# Problem set 0
# ---------------------------------------------------
# Problem 2 : PLAYBACK SPEED
# Description: Takes a text input from the user and replace the white space between them with "..."
#---------------------------------------------------------------------------------------------


# --- Input Section ---
# Prompt input from the user
message = input("Enter the message: ")

# --- Processing Section ---
# Replace every space in the message with "..." to slow it down
message = message.replace(" ", "...")

# --- Output Section ---
# Display the modified (slowed) message
print("The slowed message:", message)

