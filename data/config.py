from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili

group_id = env.int("group_id") #malumotlar uchun gruppa nomi
errorgr_id = env.int("errorgr_id") #xato malumotlar uchun gruppa
senders = env.list("senders") #yuboruvchilar royxati
confirmatives = env.list("confirmatives") #tasdiqlovchilar ro'yxati

bot_name = env.str("bot_name") # botning nomi
bot_username = env.str("bot_username") # bot usernamesi