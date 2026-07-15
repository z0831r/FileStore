from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.helper_func import check_subscription, is_user_subscribed

@Client.on_callback_query(filters.regex(r"^check_sub"))
async def refresh_check(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data
    
    # ------------------ 修复部分开始 ------------------
    # 之前的 split("_", 1) 会导致参数带上 'sub_' 前缀
    # 现在直接用 replace 把前缀替换为空，只保留真正的参数
    if "check_sub_" in data:
        payload = data.replace("check_sub_", "")
    else:
        payload = "none"
    # ------------------ 修复部分结束 ------------------

    # 2. 再次检查订阅状态
    statuses = await check_subscription(client, user_id)
    
    # 3. 判断是否已关注
    if is_user_subscribed(statuses):
        await callback_query.answer("✅ 验证成功！", show_alert=False)
        
        # A. 如果有有效的文件参数 (既不是空也不是 none)
        if payload and payload != "none":
            button = [[
                InlineKeyboardButton(
                    "📂 验证通过！点击这里获取文件", 
                    url=f"https://t.me/{client.me.username}?start={payload}"
                )
            ]]
            await callback_query.message.edit_text(
                text="✅ **验证成功！**\n\n请点击下方按钮获取您的文件。\n(机器人在繁忙时可能需要几秒钟响应)",
                reply_markup=InlineKeyboardMarkup(button)
            )
            
        # B. 如果只是普通的 /start 进来的（没有文件参数）
        else:
            await callback_query.message.delete()
            # 这种情况不发“获取文件”按钮，因为本来就没文件
            await client.send_message(
                user_id,
                "✅ **验证成功！**\n\n您现在可以正常使用机器人了。\n请重新点击原本的分享链接来获取资源。"
            )
            
    else:
        # 👇👇👇 就是这里！改成了双重验证的提示 👇👇👇
        await callback_query.answer("❌ 验证失败！请确保您已【加入群组】并【关注频道】后再试！", show_alert=True)
