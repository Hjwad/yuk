from telegraph import upload_file
from pyrogram import filters
from Auput import app
from pyrogram.types import InputMediaPhoto
from Auput.utils.bk import command


@app.on_message(
    filters.command(["tg","تليجراف"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("Make a link...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' Your Telegraph {url}')
