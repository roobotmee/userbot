from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime, timedelta, timezone
import asyncio

API_ID = "25503582"
API_HASH = "9bc607b4792e8276afa98b757b62e11e"

client = TelegramClient("userbot", API_ID, API_HASH)

async def update_nickname():
	while True:
		now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=0.55)  # 5 soat 1 minut qo‘shildi
		new_name = f" 𝐄𝐭𝐡𝐢𝐜𝐚𝐥 𝐑𝐨𝐨𝐁𝐨𝐭  | {now.strftime('%H:%M')} | "
		try:
			await client(UpdateProfileRequest(first_name=new_name))
			print(f"Nik yangilandi: {new_name}")
		except Exception as e:
			print(f"Xatolik: {e}")
		await asyncio.sleep(60)

responses = {
	"narx": " Narxlar buyutmani qiyinlik darajasidan kelib chiqib qoyiladi . Sizga nima kerakligi xaqida yozib qoldiring men keyinroq oqib javob beraman",
	"salom": "👋Assalomualaykum! Sizga qanday yordam bera olaman?",
	"Assalomu alaykum": " Vaalaykum assalom \n 👋 Assalomualaykum! Sizga qanday yordam bera olaman?",
	"Assalomualaykum": " Vaalaykum assalom \n 👋 Assalomualaykum! Sizga qanday yordam bera olaman?",
	"qalesiz": "Yaxshi, rahmat! O'zizda nima gap  🙃 ",
	"yaxshimisiz": "Yaxshi, rahmat! O'zizda nima gap  🙃 ",
	"qalisiz": "Yaxshi, rahmat! O'zizda nima gap 🙃 ",
	"nima gap": "Yaxshi, rahmat! Oziz qale  ",
	"hayotbek": "Hov",
	"ismiz": "Men xaqimda roobotmee.uz . Da oqishingiz mumkin ",
	"ism": "Men xaqimda roobotmee.uz . Da oqishingiz mumkin ",
	"alo": " Men xozir online emasman . Savolingiz bolsa yozib qoldiring ",
	"loyha": "Loyihalarim haqida bilmoqchi bolsangi mening porfolio saytim bilan tanishib chiqishingiz mumkin >> roobotmee.uz .",
	"rahmat": "Arzimaydi! Yana savollaringiz bo‘lsa, bemalol so‘rang.",
	"tel": "+99895 005 15 45 " ,
	"tel raqam": "+99895 005 15 45 " ,
	"tel nomer": "+99895 005 15 45 " ,
	"nomeriz": "+99895 005 15 45 " ,
	"nomerizni": "+99895 005 15 45 " ,
	"raqamiz" : "+99895 005 15 45 " ,
	"bot": "### 🤖 Telegram bot – biznesingizni avtomatlashtiring! \n\nSizga zamonaviy, aqlli va samarali Telegram bot kerakmi? Biz har qanday murakkablikdagi botlarni yaratamiz! \n\n🔹 Savdo va xizmatlar – mijozlaringiz bilan 24/7 aloqa. \n🔹 Avtomatlashtirilgan buyurtmalar – ortiqcha vaqt sarflash shart emas! \n🔹 To‘lov tizimlari bilan integratsiya – Payme, Click, PayPal va boshqalar. \n🔹 CRM tizimlari bilan bog‘lash – biznesingizni aniq boshqarish uchun. \n🔹 Sun’iy intellekt qo‘llab-quvvatlovi – mijozlarga tez va aniq javoblar. \n🔹 Maxsus buyurtmalar – biznesingizga mos keladigan individual yechimlar. \n\n✅ Tez, ishonchli va professional xizmat! \n\n📲 Buyurtma berish: roobotmee.uz \n☎️ Bog‘lanish: +998 95 005 15 45 ",
	"web": "### 🌍 Veb-sayt – biznesingizning internetdagi yuzi! \n\nSizning biznesingizga zamonaviy, tezkor va jozibali veb-sayt kerakmi? Biz buni mukammal darajada yaratamiz! \n\n🔹 Korporativ saytlar – kompaniyangizni mijozlarga taqdim etish uchun. \n🔹 Shaxsiy bloglar – o‘z fikrlaringizni butun dunyo bilan baham ko‘ring. \n🔹 Xizmatlar sayti – mijozlar sizning xizmatlaringizni onlayn buyurtma qilsin. \n🔹 Portfolio saytlar – ishlaringizni eng chiroyli tarzda namoyish qiling. \n🔹 E-commerce (Onlayn do‘konlar) – internet orqali savdo qilish uchun mukammal yechim. \n🔹 Mobilga moslashgan dizayn – har qanday qurilmada mukammal ko‘rinish. \n🔹 SEO optimizatsiya – Google va boshqa qidiruv tizimlarida yuqori o‘rinlar. \n\n✅ Sifatli, tezkor va ishonchli xizmat! \n\n📲 Buyurtma berish: roobotmee.uz \n☎️ Bog‘lanish: +998 95 005 15 45  ",
}

@client.on(events.NewMessage)
async def message_handler(event):
	if event.is_private:
		me = await client.get_me()  # Foydalanuvchi ma'lumotlarini olish
		if event.sender_id != me.id:  # Botga yozilgan xabarlarga javob bermaslik
			text = event.raw_text.lower()  # Kichik harflarga aylantiramiz
			
			# /del buyruqini aniqlash
			if text.startswith('/del'):
				# Xabarni o'chirish
				await client.delete_messages(event.chat_id, [event.id])
				return  # Funktsiyaning qolgan qismini o'tkazib yuborish
			
			for question, answer in responses.items():
				if text.strip() == question.lower():  # To‘liq mos kelish
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
