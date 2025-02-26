from telethon import TelegramClient, events

# Telegram API ma'lumotlarini kiriting
API_ID = "25503582"
API_HASH = "9bc607b4792e8276afa98b757b62e11e"

# Userbotni ishga tushiramiz
client = TelegramClient("userbot", API_ID, API_HASH)

# Savollarga javob beruvchi funksiya
responses = {
    "salom": "Assalomualaykum! Sizga qanday yordam bera olaman?",
    "qalesiz": "Yaxshi, rahmat! Sizda qanday yangiliklar?",
    "ismingiz nima": "Men oddiy Telegram userbotman.",
    "rahmat": "Arzimaydi! Yana savollaringiz bo‘lsa, bemalol so‘rang.",
    "bot": "### 🤖 Telegram bot – biznesingizni avtomatlashtiring! \n\nSizga **zamonaviy, aqlli va samarali** Telegram bot kerakmi? Biz har qanday murakkablikdagi botlarni yaratamiz! \n\n🔹 **Savdo va xizmatlar** – mijozlaringiz bilan 24/7 aloqa. \n🔹 **Avtomatlashtirilgan buyurtmalar** – ortiqcha vaqt sarflash shart emas! \n🔹 **To‘lov tizimlari bilan integratsiya** – Payme, Click, PayPal va boshqalar. \n🔹 **CRM tizimlari bilan bog‘lash** – biznesingizni aniq boshqarish uchun. \n🔹 **Sun’iy intellekt qo‘llab-quvvatlovi** – mijozlarga tez va aniq javoblar. \n🔹 **Maxsus buyurtmalar** – biznesingizga mos keladigan individual yechimlar. \n\n✅ **Tez, ishonchli va professional xizmat!** \n\n📲 **Buyurtma berish:** [**roobotmee.uz**](https://roobotmee.uz) \n☎️ **Bog‘lanish:** +998 XX XXX XX XX ",
    "web": "### 🌍 Veb-sayt – biznesingizning internetdagi yuzi! \n\nSizning biznesingizga **zamonaviy, tezkor va jozibali** veb-sayt kerakmi? Biz buni mukammal darajada yaratamiz! \n\n🔹 **Korporativ saytlar** – kompaniyangizni mijozlarga taqdim etish uchun. \n🔹 **Shaxsiy bloglar** – o‘z fikrlaringizni butun dunyo bilan baham ko‘ring. \n🔹 **Xizmatlar sayti** – mijozlar sizning xizmatlaringizni onlayn buyurtma qilsin. \n🔹 **Portfolio saytlar** – ishlaringizni eng chiroyli tarzda namoyish qiling. \n🔹 **E-commerce (Onlayn do‘konlar)** – internet orqali savdo qilish uchun mukammal yechim. \n🔹 **Mobilga moslashgan dizayn** – har qanday qurilmada mukammal ko‘rinish. \n🔹 **SEO optimizatsiya** – Google va boshqa qidiruv tizimlarida yuqori o‘rinlar. \n\n✅ **Sifatli, tezkor va ishonchli xizmat!** \n\n📲 **Buyurtma berish:** [**roobotmee.uz**](https://roobotmee.uz) \n☎️ **Bog‘lanish:** +998 XX XXX XX XX ",
    "bormi": "Uning yashil ko‘zlari bahorning ilk maysalaridek sokin va beg‘ubor. Har safar ularga boqganingda, go‘yo tabiatning eng so‘lim burchagida adashib qolasan – yam-yashil o‘rmonlar, quyuq daraxtlar orasidan o‘tib, sirli daryo bo‘yiga yetib borganingni his qilasan. U ko‘zlar o‘z ichida sir yashirgan, ammo shu sirning o‘ziga tortuvchi sehriga qarshi turish imkonsiz.\n\nUning go‘zalligi esa tabiatning eng mukammal ijodidan yaratilgandek. Unga qaragan odam shunchaki hayrat bilan to‘xtab qoladi – xuddi qoshidagi quyosh botayotgan manzarani ko‘rib, yuragi bir lahzaga urib turib qolgandek. Uning jilmayishi esa eng yorqin tong nuriday, qachon qarama qalbingni isitadi. Harakatlari nozik, ovozi esa bahor shabadasi kabi mayin.\n\nUnga bir qaragan inson uni unutolmaydi. Chunki bunday go‘zallikni ko‘rib, xayol uzib ketishning iloji yo‘q… 💛"
}

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text.lower()
    
    for question, answer in responses.items():
        if question.lower() in text:
            await event.reply(answer)
            break

print("Userbot ishga tushdi...")
client.start()
client.run_until_disconnected()
