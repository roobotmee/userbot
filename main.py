from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime, timedelta, timezone
import asyncio

API_ID = "20833513"
API_HASH = "dc124b69d34bd7dd19cd7539769d27ef"

client = TelegramClient("userbot", API_ID, API_HASH)

async def update_nickname():
    while True:
        now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=0.55)  
        new_name = f" ❮꯭❶꯭꯭꯭➣꯭ ᴢᴀʀɪғᴊᴏɴ ꯭꯭•꯭|꯭🖤  | {now.strftime('%H:%M')} "
        try:
            await client(UpdateProfileRequest(first_name=new_name))
            print(f"Nik yangilandi: {new_name}")
        except Exception as e:
            print(f"Xatolik: {e}")
        await asyncio.sleep(60)

responses = {
"Qalesz":  "yaxshi rahmat ozingiz yaxshimi?",
"qales":  "yaxshi rahmat",
"salom":  "salom yaxshimsz",
"Assalomu alaykum":  "valekum assalom qanday yordam kk?",
"assalomu alekum":  "valekum assalom nima yordam kk? ",
"qalesan":  "yaxshi rahmat ozin qalesan",
"qalesiz":  "rahmat yaxshiman tinchlikmi?",
"Nima gap":  "tincu ozinda nima yangiliklar",
"nima gap":  "tinch ozindachi?",
"qalesz zarifjon":  "yaxshi rahmat oziz yaxshimi?",
"Tinchmi":  "da tinch ozidachi?",
"qettasz":  "hozir band edim knroq yoza olasizmi?",
"qettas":  "hoz azginca ishlarim bor knro yozvorin",
"yaxshimisz":  "yaxshi rahmat oziz yaxshimi?",
"yaxshimisiz":  "yaxshi rahmat nima yordam kerak?",
"boshmisiz":  "yoq hozir ko'chada edim nima yordam kerak?",
}

@client.on(events.NewMessage)
async def message_handler(event):
    if event.is_private:
        me = await client.get_me()  
        if event.sender_id != me.id:  
            text = event.raw_text.lower()  
            

            if text.startswith('/del'):

                await client.delete_messages(event.chat_id, [event.id])
                return  
            
            for question, answer in responses.items():
                if text.strip() == question.lower():  
                    await event.reply(answer)
                    break

@client.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    if event.is_private:
        await event.reply("Bot ishga tushdi!")
        
        
@client.on(events.NewMessage(pattern="/del"))
async def delete_messages(event):
    if event.is_private:
        responses = []
        async for message in client.iter_messages(event.chat_id, from_user=None):
            responses.append(message)
            try:
                await client.delete_messages(event.chat_id, message.id, revoke=True)
            except Exception as e:
                print(f"Xabar o‘chirishda xatolik: {e}")
        for response in responses:
            try:
                await client.delete_messages(event.chat_id, response.id, revoke=True)
            except Exception as e:
                print(f"Error ! < / > ")
        await event.reply("")

print("Userbot ishga tushdi...")

with client:
    client.loop.create_task(update_nickname())
    client.run_until_disconnected()
