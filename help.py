from nonebot import on_fullmatch
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, Event

bot = on_fullmatch(msg='help', rule=to_me(), priority=10)


@bot.handle()
async def bot_help(bot: Bot, event: Event):
    answer = '''某些命令需要艾特bot或者前面加上"冰淇淋"或者"/"
1.今日人品：输出jrrp/今日人品
2.AI(智障机器人聊天)
3.天气播报：xx天气
4.重复："/echo"+ 语句
5.疯狂星期四
6.猜单词：/wordle [-l --length <length>] [-d --dic <dic>] [--hint] [--stop] [word]
7.表情相加'''
    await bot.send(event=event, message=answer)
