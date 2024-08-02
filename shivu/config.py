class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7078181502"
    sudo_users = "5884969921", "6961287189"
    GROUP_ID = -1002009280180
    TOKEN = "7070617268:AAHIktRsnSY1coCeYh32MFwTrbCGAyfgg3w"
    mongo_url = "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/c9744c30554b46644a800.jpg", "https://telegra.ph/file/77fd10eeccd16912ccf5b.jpg"]
    SUPPORT_CHAT = "https://t.me/lolpagalokigc"
    UPDATE_CHAT = "https://t.me/mlohvdryj"
    BOT_USERNAME = "bulma_music_bot"
    CHARA_CHANNEL_ID = "-1002009280180"
    api_id = 23255238
    api_hash = "009e3d8c1bdc89d5387cdd8fd182ec15"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
