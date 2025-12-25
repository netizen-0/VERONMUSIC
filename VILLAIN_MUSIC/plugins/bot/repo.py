from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VILLAIN_MUSIC import app
from config import BOT_USERNAME
from VILLAIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @btw_Deva ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/Yaaro_kimehfill"),
          InlineKeyboardButton("?⃟≛⃝ 𝆺𝅥⃝🍃 𝗗꯭ᴇ꯭ᴠ꯭ᴀ꯭─꯭⃜❰⎯꯭⃜ 🌿•┼⃖‌ꭗ𓆪 ᴏꜰꜰ", url="https://t.me/medevu"),
          ],
               [
                InlineKeyboardButton("˹𝐁ᴏᴛᴢ 𝐄ᴍᴩɪʀᴇ⚡️˼", url=f"https://t.me/BotzEmpire"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/DEVA_MUSICBOT "),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/p1gcfd.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
