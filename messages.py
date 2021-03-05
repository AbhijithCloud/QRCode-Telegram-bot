#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

from info import Info

class Message:
    START_TEXT = """
Hello {}, I am a simple Link to QR code generator with QR code decode to link bot.

Made with love ❤️ by @FayasNoushad from India 🇮🇳. Contact <a href='https://telegram.me/FayasChat'>support group</a> for discussion.
"""

    HELP_USER = """
<b><u>Help and Informations</u></b>

- Send me a link I will generate the QR code of that link.
- Send me a QR code image I will decode that image and convert to link.

Made with love ❤️ by @FayasNoushad from India 🇮🇳. Contact <a href='https://telegram.me/FayasChat'>support group</a> for discussion.

"""
    ABOUT_TEXT = f"""
<b><u>Informations About Me</u></b>

- Name : <a href='https://telegram.me/{Info.BOT_USERNAME}'>{Info.BOT_NAME}</a>
- Channel : <a href='http://telegram.me/FayasNoushad'>Fayas</a>
- Support : <a href='http://telegram.me/FayasChat'> Fayas Chat</a>
- Projects : <a href='http://telegram.me/FNPROJECTS'>Fayas Projects</a>
- Language : <a href='https://www.python.org/'>Python3</a>
- Framework : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
- Server : <a href='https://{Info.SERVER_DOMAIN}/'>{Info.SERVER}</a>
- Credits : <a href='https://github.com/FayasNoushad/Telegraph-Uploader-Bot#credits'>Click Here</a>
- Source : <a href='https://github.com/FayasNoushad/Telegraph-Uploader-Bot'>Click Here</a>

Made with love ❤️ by @FayasNoushad from India 🇮🇳. Contact <a href='https://telegram.me/FayasChat'>support group</a> for discussion.
"""
    ERROR = "Something Wrong! Click help button for more... Contact <a href='https://telegram.me/FayasChat'>support group</a>."
    
