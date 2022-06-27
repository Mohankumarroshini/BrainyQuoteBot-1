from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜɪɪ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ sᴇᴀʀᴄʜ ǫᴜᴏᴛᴇs ᴏɴ ᴅɪғғᴇʀᴇɴᴛ ᴛᴏᴘɪᴄs ᴀɴᴅ ɢʀᴇᴀᴛ ᴘᴇᴏᴘʟᴇ ᴀɴʏ ᴛɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ. ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴘʀᴇss 'ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ' ʙᴇʟᴏᴡ.

ʙʏ @TamilBots [🤖](https://telegra.ph/file/ce4fa9c519495a18ac6ab.jpg)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ sᴇᴀʀᴄʜ ᴀ ǫᴜᴏᴛᴇ ✨", switch_inline_query_current_chat="")],
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ sᴇᴀʀᴄʜ ᴀ ǫᴜᴏᴛᴇ ✨", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("ғᴏʀ ᴍᴏʀᴇ ʙᴏᴛs ♥", url="https://t.me/Tamilbots")],
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🎨", url="https://t.me/tamilsupport")],
    ]

    # Help Message
    HELP = """
**✨ Inline Mode ✨**
 
**1) Search Quotes**
Just pass the topic/name on which you wanna search quotes.
Example : `@QuoteProRoBot Albert Einstein`

**2) Quote of the Day**
To get 'Quote of the Day' pass `#q` or `#qod`. You will get that for 5 different topics.
Example : `@QuoteProRoBot #qod`

**3) Random Quote**
To get a single random quote pass `#r` or `#random`.
Example : `@QuoteProRoBot #random`

**4) A Single Quote**
By default, when you will use 1st option, you will get 20-30 quotes. But if you want only 1 random quote of that topic, use `#1` in end.
Example : `@QuoteProRoBot Sushant Singh Rajput #1`

More features in development. Keep track by joining @TamilBots.
    """

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ @TamilBots ᴡʜɪᴄʜ ᴘʀᴏᴠɪᴅᴇs ǫᴜᴏᴛᴇs ғʀᴏᴍ brainyquotes.com ᴜsɪɴɢ ᴘʏᴛʜᴏɴ.

ᴅᴇᴠ : [Click Here](https://github.com/StarkBotsIndustries/BrainyQuoteBot)

ғʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)

sᴜᴘᴘᴏʀᴛ : [ᴛᴀᴍɪʟ sᴜᴘᴘᴏʀᴛ](https://t.me/tamilsupport)

ᴜᴘᴅᴀᴛᴇs : [ᴛᴀᴍɪʟʙᴏᴛs](https://t.me/tamilbots)

"""










    
