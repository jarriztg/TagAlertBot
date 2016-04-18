import redis
import json
import telebot
from time import time, strftime

#############################################
#                                           #
#  CONFIGURATION                            #
#                                           #
#############################################

# Multi language settings
# http://transifex.com/zaphodias/tagalertbot/
l10n_folder = 'l10n/' # Folder with json files
lang_list = ['en'] # Two letters code ONLY!
setlang_list = "/en - English\n\
Coming soon:\n\
it - Italian\n\
ar - \u0627\u0644\u0639\u0631\u0628\u064a\u0629 (Arabic)\n\
es - Español\n\
pt - Português\n\
bp - Português do Brasil\n\
de - Deutsch\n"

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
