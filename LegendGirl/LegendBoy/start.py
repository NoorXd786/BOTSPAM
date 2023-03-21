from pyrogram import Client, filters
from pyrogram.types import *

from LegendGirl.Config import *

from .. import sudos


async def start_cmd(Legend):
    x = await Legend.get_me()
    return [
        [
            InlineKeyboardButton(
                text="🥀 Developer 🥀", url="https://t.me/LegendBot_Owner"
            ),
            InlineKeyboardButton(
                text="✨ Support ✨", url="https://t.me/LegendBot_Group"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧸 Add me in your group 🧸",
                url=f"https://t.me/{x.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄️ Source Code ❄️",
                url="https://github.com/LEGEND-AI/BOTSPAM",
            ),
            InlineKeyboardButton(
                text="☁️ Updates ☁️", url="https://t.me/LegendBot_Update"
            ),
        ],
    ]


@Client.on_message(filters.user(sudos) & filters.command(["start"], prefixes=HANDLER))
async def start(Legend: Client, message: Message):
    if ".jpg" in START_PIC or ".png" in START_PIC:
        await Legend.send_photo(
            message.chat.id,
            START_PIC,
            caption=ALIVE_MESSAGE,
            reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
        )
    elif ".mp4" in START_PIC.lower():
        await Legend.send_video(
            message.chat.id,
            START_PIC,
            caption=ALIVE_MESSAGE,
            reply_markup=InlineKeyboardMarkup(await start_cmd(Legend)),
        )
    else:
        await Legend.send_message(message.chat_id, ALIVE_MESSAGE)
