from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.helper_func import check_subscription, is_user_subscribed

@Client.on_callback_query(filters.regex(r"^check_sub"))
async def refresh_check(client, callback_query):
    # 1. 获取用户ID和按钮里的参数
    user_id = callback_query.from_user.id
    data = callback_query.data
    
    # 解析参数 (check_sub_123 -> payload = 123)
    if "_" in data:
        _, payload = data.split("_", 1)
    else:
        payload = "none"

    # 2. 再次检查订阅状态
    statuses = await check_subscription(client, user_id)
    
    # 3. 判断是否已关注
    if is_user_subscribed(statuses):
        # A. 关注成功！
        await callback_query.answer("✅ 验证成功！", show_alert=False)
        
        # B. 如果有文件参数，生成一个跳转按钮
        if payload and payload != "none":
            button = [[
                InlineKeyboardButton(
                    "📂 验证通过！点击这里获取文件", 
                    url=f"https://t.me/{client.username}?start={payload}"
                )
            ]]
            # 修改原消息，给出一个直接跳转的链接
            # 这样用户点一下就能利用 start.py 的逻辑拿到文件了
            await callback_query.message.edit_text(
                text="✅ **验证成功！**\n\n请点击下方按钮获取您的文件。\n(机器人在繁忙时可能需要几秒钟响应)",
                reply_markup=InlineKeyboardMarkup(button)
            )
        else:
            # 如果没有参数，直接删除提示
            await callback_query.message.delete()
            await callback_query.message.reply("✅ 验证成功！您可以正常使用机器人了。")
            
    else:
        # C. 还是没关注
        await callback_query.answer("❌ 您仍然没有关注频道，请关注后再试！", show_alert=True)
