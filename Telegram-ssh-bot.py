import telebot
import subprocess

# Replace with your Telegram bot token and chat ID
TOKEN = '<TELEGRAM-TOKEN-HERE>'
CHAT_ID = '<CHAT-ID-HERE>'

# Create a Telegram bot object
bot = telebot.TeleBot(TOKEN)

# Monitor the system logs for SSH login failures
p1 = subprocess.Popen(["tail", "-f", "/var/log/auth.log"], stdout=subprocess.PIPE)

# Track the number of failed login attempts
count = 0

# Send an alert for multiple failed login attempts
while True:
    line = p1.stdout.readline()
    if "Failed password" in line.decode("utf-8"):
        count += 1
        if count >= 2: #you can changes this for the desired amount of failed logins
            print("SSH Attack In Progress!")

            # Get the IP address of the attacker
            ip_address = line.decode("utf-8").split(" ")[10]

            # Set up the message text
            message_text = f"\nPossible SSH Attack Detected! {count} Failed Login Attempts From {ip_address}."

            # Send the message using the Telegram Bot API
            bot.send_message(CHAT_ID, message_text)

            print("Alert sent.")
            count = 0
    else:
        count = 0