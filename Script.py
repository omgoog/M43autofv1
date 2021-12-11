class script(object):
    START_TXT = """<b>Hello</b> {}
MY NAME IS <a href=https://t.me/{}>{}</a>, 

<i>Iam A Simple Auto Filter + Movie Search + Manual Filter Bot. I Can Provide Movies In Telegram Groups. You Can Search Movies Via Inline. I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group And Enjoy</i>

<b>Made With ❤ BY @DFF_UPDATE</b>"""
    HELP_TXT = """HEY {}
<b> Here is The My Commands.</b>

-> If you have 300000+ files and you want to add in this bot then contact admin.
-> If you have any problem then connect to admin.

<b>Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: @DFF_UPDATE ⚔️</b>"""
    ABOUT_TXT = """<b>✯ MY NAME:</b> {}
<b>💥 CREATER:</b> <a href=https://t.me/DFF_UPDATE>DFF UPDATES</a>
<b>💥 LIBRARY:</b> <code>PYROGRAM</code>
<b>💥 LANGUAGE:</b> <code>PYTHON 𝟹</code>
<b>💥 DATA BASE:</b> <code>MONGO DB</code>
<b>💥 BOT SERVER:</b> <code>HEROKU</code>
<b>💥 BUILD STATUS:</b> <code>v1.0.1 [ BETA ]</code></b>

<b>Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: @DFF_UPDATE ⚔️</b>
"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>how are you guys. any problem ? 😄</b>

<i>- JuniFer Lax is a open source project. 
- Source - If you want SOURCE CODE then talk to admin. 👍🏼</i>

      <a href='https://t.me/CVBHJOI_BOT'>🇦 🇩 🇲 🇮 🇳</a>

<b>Made With ❤ BY @DFF_UPDATE</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>

<b>© @DFF_UPDATE</b>
"""
    STATUS_TXT = """<b>★ Total Files:</b> <code>{}</code>
<b>★ Total Users:</b> <code>{}</code>
<b>★ Total Chats:</b> <code>{}</code>
<b>★ Used Storage:</b> <code>{}</code> 𝙼𝚒𝙱
<b>★ Free Storage:</b> <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
