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
3. `userbot.py` faylini yuklab oling va API ma'lumotlarini joylang.
4. Skriptni ishga tushiring:
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

## Muammolarni hal qilish
- Agar bot ishlamasa, `API_ID` va `API_HASH` ning to‘g‘ri ekanligini tekshiring.
- Internet ulanishi va `Telethon` kutubxonasi o‘rnatilganligini tekshiring.
- Agar `Too Many Requests` xatosi yuz bersa, biroz vaqt kutib, qayta urinib ko‘ring.

## Aloqa
Qo‘shimcha savollar va muammolar uchun:
- Telegram: [@roobotmee](https://t.me/roobotmee)
- Veb-sayt: [roobotmee.uz](https://roobotmee.uz)

