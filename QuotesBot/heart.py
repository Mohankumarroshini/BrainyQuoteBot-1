import random
import requests
from bs4 import BeautifulSoup
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from Data import Data


async def brainy_quotes(query):
    URL = "https://www.brainyquote.com/search_results?q="
    query = query.replace(" ", "+")
    response = requests.get(URL + query)
    soup = BeautifulSoup(response.text, 'lxml')
    result_divs = soup.find_all("div", attrs={"class": "grid-item qb clearfix bqQt"})
    quotes = {}
    for result_div in result_divs:
        soup = BeautifulSoup(str(result_div), 'lxml')
        contents = soup.find_all("a")
        quote = contents[0].text.replace("\n", "")
        author = contents[1].text
        id = result_div.attrs['id']
        quotes[id] = [quote, author]
    articles = []
    for value in quotes.values():
        author = value[1]
        quote = value[0]
        result = InlineQueryResultArticle(
            title=author,
            input_message_content=InputTextMessageContent("ıllıllı★ 𝐐𝐮𝐨𝐭𝐞𝐬 𝐁𝐨𝐭 ★ıllıllı \n\n" + quote + "\n\n~ " + author),
            url="https://t.me/tamilbots",
            description=quote,
            thumb_url="https://telegra.ph/file/ce4fa9c519495a18ac6ab.jpg",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✨ sᴇᴀʀᴄʜ ᴍᴏʀᴇ ǫᴜᴏᴛᴇs ✨", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("♥ ғᴏʀ ᴍᴏʀᴇ ʙᴏᴛs ♥", url="https://t.me/tamilbots")]
                ]
            ),
        )
        articles.append(result)
    random.shuffle(articles)
    if len(articles) == 0:
        articles.append(main)
    return articles

main = InlineQueryResultArticle(
            title="Quotes Bot",
            input_message_content=InputTextMessageContent(Data.HELP),
            url="https://t.me/tamilbots",
            description="Learn How to use me efficiently",
            thumb_url="https://telegra.ph/file/ce4fa9c519495a18ac6ab.jpg",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✨ sᴇᴀʀᴄʜ ǫᴜᴏᴛᴇs ✨", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("♥ ғᴏʀ ᴍᴏʀᴇ ʙᴏᴛs ♥", url="https://t.me/tamilbots")]
                ]
            ),
        )
