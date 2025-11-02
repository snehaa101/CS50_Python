# ------------------------------------------------------------------------------------------
# CS50 Python
# Week 0
# Problem set 0
# ---------------------------------------------------
# Problem 3 : MAKING FACES
# Description: This program takes a message from the user and replaces
#              emoticons like ":)" and ":(" with their corresponding
#              emoji faces 🙂 and 🙁.
#---------------------------------------------------------------------------------------------

def main():
      # Takes input from user and print it with emojis

  # --- Input Section ---
  # Prompt input from the user
    message = input("Enter the message : ")

  # --- Processing Section ---
  # Call the convert function to replace emoticons with emoji
    converted_message = convert(message)

  # --- Output Section ---
  # Print the message with emojis
    print(converted_message)

# --- Helper Function ---
def convert(emojis):
    # Replace emoticon symbols with their corresponding emojis.

    # Parameters:
    #     emojis (str): The input message that may contain emoticons.

    # Returns:
    #     str: The message where ":)" becomes 🙂 and ":(" becomes 🙁.


    emojis = emojis.replace(":)", "🙂").replace(":(", "🙁")
    return emojis

# Calls the main() function
main()

