from pyrogram import Client, filters
import time

# Telegram API ma'lumotlarini shu yerga qo'ying
API_ID = "25503582"
API_HASH = "9bc607b4792e8276afa98b757b62e11e"
SESSION_NAME = "robotmee"
TARGET_GROUP_ID = -4678022853  # Yuborilishi kerak bo'lgan guruh ID'si

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

last_sent_time = 0
cooldown = 5  # Xabar yuborish orasidagi minimal vaqt (soniya)
message_counter = 0
message_limit = 10  # Har soatda yuboriladigan maksimal xabar
reset_time = time.time() + 3600  # Bir soatlik vaqt chegarasi

@app.on_message(filters.text & ~filters.me & filters.group)
def forward_bor_messages(client, message):
	global last_sent_time, message_counter, reset_time
	text = message.text.lower()
	current_time = time.time()
	
	# Har soatda limitni qayta tiklash
	if current_time >= reset_time:
		message_counter = 0
		reset_time = current_time + 3600
	

	if  "bor" in text and message_counter < message_limit:
		if current_time - last_sent_time >= cooldown:
			sender = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
			group = f"[{message.chat.title}](https://t.me/{message.chat.username})" if message.chat.username else f"Guruh ({message.chat.id})"
			forward_text = f"{sender} {group} da yozdi:\n{message.text}"
			forward_text = f" 🚕 Yangi buyurma ✅ \n 👤 Yuboruvchi {sender} \n\n👥 Guruxidan  {group}  \n\n 📄 Buyurma \n\n {message.text}"
			client.send_message(TARGET_GROUP_ID, forward_text)
			
			# Shaxsiy xabar yuborish
			client.send_message(message.from_user.id, "Taxi kerakmidi  \n +998950051545 Telefon qiling olamiz ")
			
			last_sent_time = current_time
			message_counter += 1
	
app.run()
