import os
import logging
from logging.handlers import RotatingFileHandler

# =====================================================================
# 👇👇👇 你的真实信息配置区域 👇👇👇
# =====================================================================

# 1. 机器人的 Token
TOKEN = "8363243145:AAGJq_h4XS6oh7AaqS03iwrPC0GOkhqoXXg"

# 2. 你的用户 ID
OWNER_ID = 1514265446

# 3. 仓库频道 ID
DB_CHANNEL = -1003608700446

# 4. 强制关注频道 ID
fs_id = -1002323971609

# 5. 强制关注群组 ID 
TG_GROUP_ID = -1001426717075
# =====================================================================
# 👆👆👆 配置结束 👆👆👆
# =====================================================================

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '8000'
MSG_EFFECT = 5046509860389126442
SHORT_URL = ""
SHORT_API = ""
SHORT_TUT = ""

# Bot Configuration
SESSION = "yato_zeabur_v1" # 我帮你改了个新名字，防止冲突

# API 配置
API_ID = 30704568
API_HASH = "52e56469e426ad12b0cea28480e3802d"
WORKERS = 5

# 数据库连接
DB_URI = "mongodb+srv://z0831r:zr19900831@cluster0.wmpdcus.mongodb.net/?appName=Cluster0"
DB_NAME = "yato"

# 强制关注配置
FSUBS = [[fs_id, False, 10], [TG_GROUP_ID, False, 10]]

# Auto Delete Timer (seconds)
AUTO_DEL = 300

# Admin IDs
ADMINS = [6497757690, 6103092779, 1514265446]

# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b>👋 你好!!, {first} ~ <blockquote>我是您的私人文件管家。\n直接发送文件给我，我会为您生成永久分享链接。\n\n⚠️ 注意：请勿上传违规内容。</blockquote></b>",
    "FSUB": "<b>🚨 身份验证 🚨\n\n检测到您尚未完全加入我们的社区。\n为了防止滥用，请点击下方按钮【加入官方群组】和【关注防封频道】。\n\n完成后请点击“刷新重试”获取文件。</b>",
    "ABOUT": "<b>›› 机器人名称: 文件存储机器人 \n <blockquote expandable>›› 更新频道: <a href='https://t.me/codeflix_bots'>点击查看</a> \n›› 主人: @ProYato\n›› 语言: <a href='https://docs.python.org/3/'>Python 3</a> \n›› 框架: <a href='https://docs.pyrogram.org/'>Pyrogram v2</a> \n›› 数据库: <a href='https://www.mongodb.com/docs/'>Mongo DB</a></b></blockquote>",
    "REPLY": "<b>收到！正在为您生成链接，请稍候...</b>",
    "SHORT_MSG": "<b>📊 嘿 {first}, \n\n‼️ 获取您的文件链接 ‼️\n\n ⌯ 链接已生成，请点击下方按钮打开..</b>",
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
