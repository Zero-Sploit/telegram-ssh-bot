# Telegram-ssh-bot


###  This is a simple Telegram bot that monitors SSH login attempts on a server and sends an alert to a Telegram group when two failed login attempts are    detected. The alert message includes the IP address of the failed login attempt.
### Prerequisites

### Before using this bot, you must have the following installed:

    ``Python 3
    python-telebot library
    fail2ban or a similar tool that logs failed SSH login attempts to a file``

###    Setup

###    Clone this repository to your server:

### bash

``git clone https://github.com/Zero-Sploit/ssh-telegram-bot.git``

###    Install the required Python packages:

``pip install python-telegram-bot``

###    Create a Telegram bot and get the API token. Follow these instructions to create a bot and obtain the API token.
###    Create a Telegram group and add the bot to the group.
###    Configure fail2ban to log failed SSH login attempts to a file. The exact steps may vary depending on your operating system and configuration. For example, on Ubuntu, you can follow these instructions.
###    Edit the config.py file with the API token, group ID, and path to the log file. You can also customize the alert message if you like.
###    Run the bot with the following command:

``python bot.py``

###    Make sure the bot is running and check that it sends an alert message to the Telegram group when two failed login attempts are detected.
