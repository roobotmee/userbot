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
        new_name = f"𝐄𝐭𝐡𝐢𝐜𝐚𝐥 𝐑𝐨𝐨𝐁𝐨𝐭 | {now.strftime('%H:%M')} | "
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
	"qalesiz": "Yaxshi, rahmat! Sizda qanday yangiliklar? 🙃 ",
	"qalisiz": "Yaxshi, rahmat! Sizda qanday yangiliklar?🙃 ",
	"ismiz": "Men xaqimda roobotmee.uz . Da oqishingiz mumkin ",
	"alo": " Men xozir online emasman . Savolingiz bolsa yozib qoldiring ",
	"loyha": "Loyihalarim haqida bilmoqchi bolsangi mening porfolio saytim bilan tanishib chiqishingiz mumkin >> roobotmee.uz .",
	"rahmat": "Arzimaydi! Yana savollaringiz bo‘lsa, bemalol so‘rang.",
	"bot": "### 🤖 Telegram bot – biznesingizni avtomatlashtiring! \n\nSizga zamonaviy, aqlli va samarali Telegram bot kerakmi? Biz har qanday murakkablikdagi botlarni yaratamiz! \n\n🔹 Savdo va xizmatlar – mijozlaringiz bilan 24/7 aloqa. \n🔹 Avtomatlashtirilgan buyurtmalar – ortiqcha vaqt sarflash shart emas! \n🔹 To‘lov tizimlari bilan integratsiya – Payme, Click, PayPal va boshqalar. \n🔹 CRM tizimlari bilan bog‘lash – biznesingizni aniq boshqarish uchun. \n🔹 Sun’iy intellekt qo‘llab-quvvatlovi – mijozlarga tez va aniq javoblar. \n🔹 Maxsus buyurtmalar – biznesingizga mos keladigan individual yechimlar. \n\n✅ Tez, ishonchli va professional xizmat! \n\n📲 Buyurtma berish: roobotmee.uz \n☎️ Bog‘lanish: +998 XX XXX XX XX ",
	"web": "### 🌍 Veb-sayt – biznesingizning internetdagi yuzi! \n\nSizning biznesingizga zamonaviy, tezkor va jozibali veb-sayt kerakmi? Biz buni mukammal darajada yaratamiz! \n\n🔹 Korporativ saytlar – kompaniyangizni mijozlarga taqdim etish uchun. \n🔹 Shaxsiy bloglar – o‘z fikrlaringizni butun dunyo bilan baham ko‘ring. \n🔹 Xizmatlar sayti – mijozlar sizning xizmatlaringizni onlayn buyurtma qilsin. \n🔹 Portfolio saytlar – ishlaringizni eng chiroyli tarzda namoyish qiling. \n🔹 E-commerce (Onlayn do‘konlar) – internet orqali savdo qilish uchun mukammal yechim. \n🔹 Mobilga moslashgan dizayn – har qanday qurilmada mukammal ko‘rinish. \n🔹 SEO optimizatsiya – Google va boshqa qidiruv tizimlarida yuqori o‘rinlar. \n\n✅ Sifatli, tezkor va ishonchli xizmat! \n\n📲 Buyurtma berish: roobotmee.uz \n☎️ Bog‘lanish: +998 XX XXX XX XX ",
	"rano": "Uning yashil ko‘zlari bahorning ilk maysalaridek sokin va beg‘ubor. Har safar ularga boqganingda, go‘yo tabiatning eng so‘lim burchagida adashib qolasan – yam-yashil o‘rmonlar, quyuq daraxtlar orasidan o‘tib, sirli daryo bo‘yiga yetib borganingni his qilasan. U ko‘zlar o‘z ichida sir yashirgan, ammo shu sirning o‘ziga tortuvchi sehriga qarshi turish imkonsiz.\n\nUning go‘zalligi esa tabiatning eng mukammal ijodidan yaratilgandek. Unga qaragan odam shunchaki hayrat bilan to‘xtab qoladi – xuddi qoshidagi quyosh botayotgan manzarani ko‘rib, yuragi bir lahzaga urib turib qolgandek. Uning jilmayishi esa eng yorqin tong nuriday, qachon qarama qalbingni isitadi. Harakatlari nozik, ovozi esa bahor shabadasi kabi mayin.\n\nUnga bir qaragan inson uni unutolmaydi. Chunki bunday go‘zallikni ko‘rib, xayol uzib ketishning iloji yo‘q… 💛",
	"ra'no": "Uning yashil ko‘zlari bahorning ilk maysalaridek sokin va beg‘ubor. Har safar ularga boqganingda, go‘yo tabiatning eng so‘lim burchagida adashib qolasan – yam-yashil o‘rmonlar, quyuq daraxtlar orasidan o‘tib, sirli daryo bo‘yiga yetib borganingni his qilasan. U ko‘zlar o‘z ichida sir yashirgan, ammo shu sirning o‘ziga tortuvchi sehriga qarshi turish imkonsiz.\n\nUning go‘zalligi esa tabiatning eng mukammal ijodidan yaratilgandek. Unga qaragan odam shunchaki hayrat bilan to‘xtab qoladi – xuddi qoshidagi quyosh botayotgan manzarani ko‘rib, yuragi bir lahzaga urib turib qolgandek. Uning jilmayishi esa eng yorqin tong nuriday, qachon qarama qalbingni isitadi. Harakatlari nozik, ovozi esa bahor shabadasi kabi mayin.\n\nUnga bir qaragan inson uni unutolmaydi. Chunki bunday go‘zallikni ko‘rib, xayol uzib ketishning iloji yo‘q… 💛"
}
}

@client.on(events.NewMessage)
async def message_handler(event):
    if event.is_private:  # Faqat shaxsiy xabarlarga javob berish
        text = event.raw_text.lower()
        for question, answer in responses.items():
            if question in text:
                await event.reply(answer)
                break

@client.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    if event.is_private:
        await event.reply("Bot ishga tushdi!")

print("Userbot ishga tushdi...")

with client:
    client.loop.create_task(update_nickname())
    client.run_until_disconnected()
