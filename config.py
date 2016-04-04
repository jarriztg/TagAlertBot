import redis
import json
import telebot
from time import time, strftime

#############################################
#                                           #
#  CONFIGURATION                            #
#                                           #
#############################################

# This is where we store localized texts
replies_json = 'path/to/replies.json'

# Languages supported (TWO letters code for language)
l10n_folder = 'l10n/'
lang_list = ['en', 'it', 'de', 'es', 'ar']
setlang_list = "/en - English\n\
/it - Italian\n\
/de - Deutsch\n\
/es - Español\n\
/ar - \u0627\u0644\u0639\u0631\u0628\u064a\u0629 (Arabic)\n"

# Bot's owner info
bot_name = "TagAlertBot"
admin_id = 0000000
admin_mail = 'your@email.com'

# Tokens (get yours contacting @BotFather)
main_bot_token = "your_main_bot_token"
log_bot_token = "your_log_bot_token"
feedback_bot_token = "your_feedback_bot_token"
botan_token = 'your_botan_token' # Analytics with botan

# True = Skip messages arrived when bot were offline
skip_pending = False


#############################################     
#                                           #     
#  LOADING...                               #     
#                                           #     
#############################################     
    
db = redis.Redis("localhost", decode_responses=True, db=2)

replies = {}
for l in lang_list:
    with open(l10n_folder+l+'.json') as f:
        replies[l] = json.load(f)


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

for k in db.scan_iter():
    try:
        if db.hget(k, "enabled") == "True":
            enabled_users+= 1
        known_users+= 1
    except Exception:
        pass

# Main bot initializing...
bot = telebot.TeleBot(main_bot_token)
bot.skip_pending = skip_pending

# Log bot initializing...
log_bot = telebot.TeleBot(log_bot_token)
log_bot.send_message(admin_id, "[%s]\n@%s is starting." % (strftime("%Y-%m-%d %H:%M:%S"), bot_name))

# Feedback bot initializing
feedback_bot = telebot.TeleBot(feedback_bot_token)


