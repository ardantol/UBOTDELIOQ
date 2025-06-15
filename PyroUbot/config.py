import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "5756176889").split()))

API_ID = int(os.getenv("API_ID", "26472838"))

API_HASH = os.getenv("API_HASH", "89ef0aed3618a08c2a4960ee30013501")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8157249494:AAEo9qP0h0gQzzjusf6TgEGCfUPbN8kHmig")

OWNER_ID = int(os.getenv("OWNER_ID", "5756176889"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "MA2sUZ4HdAfBegL36HiG4BUG")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aortulsk:KxCX5EQdssavL4dm@cluster0.qsywpr2.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002340429336"))

