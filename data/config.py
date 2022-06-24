# from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
CHANNELS = ["@IT_memes_eng"]    

import os
BOT_TOKEN=str(os.environ.get("BOT_TOKEN"))
ADMINS=[]
ADMINS.append(os.environ.get("ADMINS"))
IP=str(os.environ.get("ip"))

#bla bla bla