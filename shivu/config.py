class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = int(getenv("7078181502"))
    SUDO_USERS = getenv("5884969921", "6961287189")
    GROUP_ID = int(getenv(-1002009280180))
    TOKEN = getenv("7070617268:AAHIktRsnSY1coCeYh32MFwTrbCGAyfgg3w")
    MONGO_DB_URI = getenv("mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority")
    PHOTO_URL = getenv("https://telegra.ph/file/c9744c30554b46644a800.jpg", "https://telegra.ph/file/77fd10eeccd16912ccf5b.jpg")
    SUPPORT_CHAT = getenv("https://t.me/lolpagalokigc")
    UPDATE_CHAT = getenv("https://t.me/mlohvdryj")
    BOT_USERNAME = getenv("bulma_music_bot")
    CHARA_CHANNEL_ID = getenv("-1002009280180")
    API_ID = int(getenv(23255238))
    API_HASH = getenv("009e3d8c1bdc89d5387cdd8fd182ec15")

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
