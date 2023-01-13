import json
import requests
from nonebot.rule import to_me
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Event

app_id = "67f21c45863dc2c6fb609caa77ab64d1"
OwnThink_url = "https://api.ownthink.com/bot"
user_id = "gz6kSdkq"


async def get_bot_message(text: str):
    try:
        data = {
            "spoken": text,
            "appid": app_id,
            "userid": user_id
        }
        sess = requests.post(
            f'https://api.ownthink.com/bot?spoken={text}', data=data)
        # print(sess.text)
        # print(1111)
        # print(type(sess.text))
        answer = sess.text
        answer = json.loads(answer)  # answer类型是字典
        print(answer['data']['info']['text'])
        return answer['data']['info']['text']
    except KeyError:
        return "这个问题好头疼啊，问点别的叭"


bot = on_message(priority=100, rule=to_me())


@bot.handle()
async def bot_chat(bot: Bot, event: Event):
    if event.get_user_id() != event.self_id:
        if str(event.get_message()) == '':
            chat_message = await get_bot_message('你是谁')
        else:
            chat_message = await get_bot_message(str(event.get_message()))
        await bot.send(event=event, message=chat_message)
