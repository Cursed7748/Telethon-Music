import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6138316802:AAHCyoYE687S43UFgj8AhhCiOyqmYBQK4js)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIwBuxxPs689IP2IjRsoUnz_HNDJNwR8RaIyrRYlp0G9L3Q-KfCMgI9AwagYsu9MSQ9EHrh3Ri8rgU0CYo2YJe8Y1NHS8yiReOkkZaSdh38mbyRne4a0_QvmfNbiZr7_ft9u09xWKV4_AiTXlmRZR6vAd4ug-opU5TXT0Of86Hj7WPdZKNyFqSiL-RwoXk4C7J_ygVwmmef5bnaUTAh4Pxjmpc9PaZPUaIgAX3hj80Jcrj8lC4fWm0RqARChnpwCOmr-YHfFsHwax4QNMvO3a1H-SC0R1mxMGvDdf7NIUpXchk40gl8m3JKhVU0iA3RU1snEMdRLJGM-nFCklSYqqGsky-8=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/+kRwv17Zem1Q5Zjk1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "hacked_ocean") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
