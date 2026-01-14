import os
import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '8000'
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

MSG_EFFECT = 5046509860389126442

SHORT_URL = ""
SHORT_API = ""
SHORT_TUT = ""

# Bot Configuration
SESSION = "yato"
TOKEN = os.environ.get("TG_BOT_TOKEN", "")
API_ID = int(os.environ.get("APP_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
WORKERS = 5

DB_URI = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "yato")

fs_id = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FSUBS = [[fs_id, True, 10]] if fs_id != 0 else []
# Database Channel (Primary)
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "0"))# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [6497757690, 6103092779]
# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b>👋 你好!!, {first} ~ <blockquote>我是您的私人文件管家。\n直接发送文件给我，我会为您生成永久分享链接。\n\n⚠️ 注意：请勿上传违规内容。</blockquote></b>",
    "FSUB": "<b>🚨 需关注频道 🚨\n\n检测到您尚未关注我们的频道。\n为了防止滥用，请点击下方按钮关注，然后点击“刷新重试”获取文件。</b>",
    "ABOUT": "<b>›› 机器人名称: 文件存储机器人 \n <blockquote expandable>›› 更新频道: <a href='https://t.me/codeflix_bots'>点击查看</a> \n›› 主人: @ProYato\n›› 语言: <a href='https://docs.python.org/3/'>Python 3</a> \n›› 框架: <a href='https://docs.pyrogram.org/'>Pyrogram v2</a> \n›› 数据库: <a href='https://www.mongodb.com/docs/'>Mongo DB</a></b></blockquote>",
    "REPLY": "<b>收到！正在为您生成链接，请稍候...</b>",
    "SHORT_MSG": "<b>📊 嘿 {first}, \n\n‼️ 获取您的文件链接 ‼️\n\n ⌯ 链接已生成，请点击下方按钮打开..</b>",
    # ⚠️ 必须填入有效链接！这里使用了一张绝对能用的测试图，先让机器人活过来
    "START_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}
def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
