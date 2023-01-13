import random
from datetime import date
from nonebot.plugin import on_fullmatch
from nonebot.adapters.onebot.v11 import Bot, Event  # 大佬说gocq不支持v12
from nonebot.adapters.onebot.v11.message import Message

jrrp = on_fullmatch(['jrrp', '今日人品'], priority=99, ignorecase=True)

day_dictionary = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
                  'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

# print(day_dictionary[date.today().strftime("%A")])
# print(date.today().strftime("%Y%m%d%A"))
# print(type(day_dictionary.get('s')))
# assert (day_dictionary.get('s'))


def display_luck(luck) -> str:
    if luck >= 90:
        return '大吉'
    elif luck >= 80:
        return '吉'
    elif luck >= 70:
        return '小吉'
    elif luck >= 60:
        return '末吉'
    elif luck >= 50:
        return '中平'
    elif luck >= 40:
        return '凶'
    else:
        return '大凶'


@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    try:
        rnd = random.Random()
        rnd.seed(int(date.today().strftime("%Y%m%d")) +
                 day_dictionary[date.today().strftime("%A")]+int(event.get_user_id()))
        luck = rnd.randint(0, 100)
        await jrrp.finish(Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{luck}/100，为“{display_luck(luck)}”'))
    except KeyError:
        await jrrp.finish(Message('键值不存在'))
