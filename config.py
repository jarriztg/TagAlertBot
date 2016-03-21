import json
import telebot
from time import time, strftime

#############################################
#                                           #
#  CONFIGURATION                            #
#                                           #
#############################################

# Logging to file (for debug purpose)
enable_debug_log = False
logpath = '/your_log_folder/'
logname = 'your_log_file.log'

# This is where we store users informations
users_json = '/path/to/users.json'

# Bot's owner info
admin_id = 0000000
admin_mail = 'your@email.com'

# Tokens (get yours contacting @BotFather)
main_bot_token = "your_main_bot_token"
log_bot_token = "your_log_bot_token"
feedback_bot_token = "your_feedback_bot_token"

# True = Skip messages arrived when bot were offline
skip_pending = False


#############################################     
#                                           #     
#  OPENING JSON FILES                       #     
#                                           #     
#############################################     
    
with open(users_json) as jsf:    
    users = json.load(jsf)


#############################################
#                                           #
#  STARTING THE BOT(s)                      #
#                                           #
#############################################

# Statistics:
global known_users
known_users = 0
global enabled_users
enabled_users = 0

for r in users:
    if users[r]['enabled'] == 1:
        enabled_users+= 1
    known_users+= 1

# Main bot initializing...
bot = telebot.TeleBot(main_bot_token)
bot.skip_pending = skip_pending

# Log bot initializing...
log_bot = telebot.TeleBot(log_bot_token)
log_bot.send_message(admin_id, "[%s]\n@TagAlertBot is starting." % strftime("%Y-%m-%d %H:%M:%S"))

# Feedback bot initializing
feedback_bot = telebot.TeleBot(feedback_bot_token)


