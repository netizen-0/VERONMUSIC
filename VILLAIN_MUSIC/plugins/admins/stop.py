from pyrogram import filters
from pyrogram.types import Message

from VILLAIN_MUSIC import app
from VILLAIN_MUSIC.core.call import VILLAIN
from VILLAIN_MUSIC.utils.database import set_loop
from VILLAIN_MUSIC.utils.decorators import AdminRightsCheck
from VILLAIN_MUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"], prefixes=["/", "!", "."])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await VILLAIN.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention),
    )
