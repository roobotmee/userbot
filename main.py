from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime, timedelta
import asyncio

API_ID = "25503582"
API_HASH = "9bc607b4792e8276afa98b757b62e11e"

client = TelegramClient("userbot", API_ID, API_HASH)

async def update_nickname():
    while True:
        now = datetime.utcnow() + timedelta(hours=5, minutes=1)  # 5 soat 1 minut qo‘shildi
        new_name = f"𝐄𝐭𝐡𝐢𝐜𝐚𝐥 𝐑𝐨𝐨𝐁𝐨𝐭 |  {now.strftime('%H:%M') | }"
        try:
            await client(UpdateProfileRequest(first_name=new_name))
            print(f"Nik yangilandi: {new_name}")
        except Exception as e:
            print(f"Xatolik: {e}")
        await asyncio.sleep(60)

responses = {
    "narx": " Narxlar buyurtma qiyinlik darajasiga qarab belgilanadi. Sizga nima kerakligini yozib qoldiring, keyinroq javob beraman.",
    "salom": "👋Assalomu alaykum! Sizga qanday yordam bera olaman?",
    "Assalomu alaykum": "Vaalaykum assalom! 👋 Sizga qanday yordam bera olaman?",
    "qalesiz": "Yaxshi, rahmat! Sizda qanday yangiliklar? 🙂",
    "qalisiz": "Yaxshi, rahmat! Sizda qanday yangiliklar? 🙂",
    "ismiz": "Men haqimda roobotmee.uz saytida o'qishingiz mumkin.",
    "alo": "Men hozir online emasman. Savolingiz bo'lsa, yozib qoldiring.",
    "loyha": "Loyihalarim bilan tanishmoqchi bo'lsangiz, portfolio saytimga kiring: roobotmee.uz",
    "rahmat": "Arzimaydi! Yana savollaringiz bo‘lsa, bemalol so‘rang.",
    "bot": " 🤖 Telegram bot – biznesingizni avtomatlashtiring!...",
    "web": " 🌍 Veb-sayt – biznesingizning internetdagi yuzi!..."
}

@client.on(events.NewMessage)
async def message_handler(event):
    text = event.raw_text.lower()
    for question, answer in responses.items():
        if question in text:
            await event.reply(answer)
            break

@client.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    await event.reply("Bot ishga tushdi!")

print("Userbot ishga tushdi...")

with client:
    client.loop.create_task(update_nickname())
    client.run_until_disconnected()
