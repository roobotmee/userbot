# Userbot uchun qo'llanma

## Kirish
Ushbu userbot Telegram akkauntingiz orqali avtomatlashtirilgan xabarlar jo'natish, foydalanuvchi so'rovlariga javob berish va profil ismingizni dinamik tarzda yangilash imkonini beradi. U `Telethon` kutubxonasidan foydalanadi.

## Talablar
Userbotdan foydalanish uchun quyidagi talablar bajarilishi kerak:
- Python 3.7 yoki undan yuqori versiya
- `telethon` kutubxonasi (`pip install telethon`)
- Telegram API ma'lumotlari (`API_ID` va `API_HASH`)

## O'rnatish
1. Python va kerakli kutubxonalarni o'rnating:
   ```sh
   pip install telethon
   ```
2. Telegram API uchun [my.telegram.org](https://my.telegram.org/apps) sahifasidan `API_ID` va `API_HASH` oling.
3. `config.py` faylini yarating va quyidagilarni kiriting:
   ```python
   API_ID = "YOUR_API_ID"
   API_HASH = "YOUR_API_HASH"
   ```
4. `userbot.py` faylini yuklab oling va API ma'lumotlarini joylang.
5. Skriptni ishga tushiring:
   ```sh
   python userbot.py
   ```

## Asosiy Funksiyalar
### Profil ismini dinamik yangilash
- Har bir daqiqada bot profil ismini hozirgi vaqtga moslab o'zgartiradi.

### Xabarlarni avtomatik javoblash
- Foydalanuvchining yozgan so'zlari bo'yicha javob beradi.
- So'rovlar ro‘yxati `responses` lug‘atida keltirilgan.

### Buyruqlar
| Buyruq | Tavsif |
|--------|---------|
| `/start` | Bot ishga tushganligini tasdiqlovchi xabar yuboradi. |
| `/del` | So‘nggi xabarlarni o‘chirish uchun ishlatiladi. |

## Foydalanish
Botga quyidagi so‘zlardan biri yozilsa, avtomatik javob qaytariladi:

| Xabar       | Javob |
|-------------|---------------------------------------------------------------|
| salom       | Assalomualaykum! Sizga qanday yordam bera olaman? |
| qalesiz     | Yaxshi, rahmat! Sizda qanday yangiliklar? |
| ismingiz nima | Men oddiy Telegram userbotman. |
| bot         | Telegram botlar yaratish haqida ma'lumot beradi |
| web         | Veb-sayt yaratish haqida ma'lumot beradi |
| bormi       | Maxsus javob beradi |

## Muammolarni hal qilish
- Agar bot ishlamasa, `API_ID` va `API_HASH` ning to‘g‘ri ekanligini tekshiring.
- Internet ulanishi va `Telethon` kutubxonasi o‘rnatilganligini tekshiring.
- Agar `Too Many Requests` xatosi yuz bersa, biroz vaqt kutib, qayta urinib ko‘ring.

## Mualliflik Huquqi
Bu kod [Hayotbek Ismoilov](https://roobotmee.uz) tomonidan yozilgan va barcha huquqlar himoyalangan. Koddan foydalanish va tarqatish faqat muallif ruxsati bilan amalga oshirilishi mumkin.

## Aloqa
Agar savollaringiz bo‘lsa yoki yordam kerak bo‘lsa, quyidagi manzilga murojaat qiling:
📩 Email: kh.ismoiloff@gmail.com
📞 Telefon: +998 95 005 15 45
- Telegram: [@roobotmee](https://t.me/roobotmee)
- Veb-sayt: [roobotmee.uz](https://roobotmee.uz)

