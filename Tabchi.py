from pyrogram import Client
api_id = 7342495
api_hash = "f80518afa684bb78505a955040936c77"

#with Client("my_account", api_id, api_hash) as app:
#    app.send_message("me", "Greetings from **Pyrogram**!")

from pyrogram import Client

app = Client("my_account", api_id, api_hash)

@app.on_message()
def my_handler(client, message):
    message.reply_text(message.text)


app.run()