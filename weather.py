import json
from urllib.request import urlopen
from urllib.parse import urlencode
from nonebot.rule import to_me
from nonebot import on_endswith
from nonebot.adapters.onebot.v11 import Bot, Event

# 配置您申请的APPKey
appkey = "251518e073ef6c3c9504dd286c3f6a86"


# 根据城市查询天气
async def weather_request(appkey, m, message: str) -> str:
    message = message.strip("天气")
    url = "http://op.juhe.cn/onebox/weather/query"
    params = {
        "cityname": message,  # 要查询的城市，如：温州、上海、北京
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "",  # 返回数据的格式,xml或json，默认json

    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            # print(res["data"])
            # print(res)
            tmp = res['result']['data']['realtime']
            answer = f'{tmp["city_name"]}，{tmp["date"]} {tmp["time"]}，{tmp["weather"]["info"]}，{tmp["weather"]["temperature"]}℃，{tmp["wind"]["direct"]}，风力{tmp["wind"]["power"]}'
            print(answer)
            return answer
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
            return "%s:%s" % (res["error_code"], res["reason"])
    else:
        print("request api error")
        return "request api error"

bot = on_endswith(msg="天气", priority=99, rule=to_me())


@bot.handle()
async def bot_weather_request(bot: Bot, event: Event):
    if event.get_user_id() != event.self_id:
        answer = await weather_request(appkey, "GET", str(event.get_message()))
        await bot.send(event=event, message=answer)

#res['result']数据
# {
#     'data':
#     {
#         'realtime':
#         {
#             'city_code': '101020100',
#             'city_name': '上海',
#             'date': '2023-01-12',
#             'time': '16:00:00',
#             'week': '4',
#             'moon': '月',
#             'dataUptime': 1673511076,
#             'weather':  {
#                             'temperature': '17',
#                             'humidity': '88',
#                             'info': '多云',
#                             'img': '01'
#                         },
#             'wind': {'direct': '东风', 'power': '2级', 'offset': '', 'windspeed': ''}
#         },
#         'life':
#         {
#             'date': '2023-01-12', 'info':
#                 {
#                     'kongtiao': ['较少开启', '您将感到很舒适，一般不需要开启空调。'],
#                     'guomin': ['极不易发', '天气条件极不易诱发过敏，有降水，出行注意携带雨具。'],
#                     'shushidu': ['舒适', '白天不太热也不太冷，风力不大，相信您在这样的天气条件下，应会感到比较清爽和舒适。'],
#                     'chuanyi': ['较舒适', '建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。'],
#                     'diaoyu': ['不宜', '天气不好，不适合垂钓。'],
#                     'ganmao': ['易发', '天冷空气湿度大，易发生感冒，请注意适当增加衣服，加强 自我防护避免感冒。'],
#                     'ziwaixian': ['最弱', '属弱紫外线辐射天气，无需特别防护。若长期在户外，建议涂擦SPF在8-12之间的防晒护肤品。'],
#                     'xiche': ['不宜', '不宜洗车，未来24小时内有雨，如果在此期间洗车，雨水和路上的泥水可能会再次弄脏您的爱车。'],
#                     'yundong': ['较不宜', '有降水，推荐您在室内进行健身休闲运动；若坚持户外运动，须注意携带雨具并注意避雨防滑。'],
#                     'daisan': ['带伞', '有降水，请带上雨伞，如果你喜欢雨中漫步，享受大自然给予的温馨和快乐，在短时间外出可收起雨伞。']
#                 }
#         },
#         'weather':
#         [{
#             'date': '2023-01-12',
#             'info':
#             {
#                 'dawn': ['1', '多云', '11', '东南风', '微风', '17:09'],
#                 'day': ['7', '小雨', '18', '东南风', '微风', '06:54', '出门记得带伞，行走驾驶做好防滑准备'],
#                 'night': ['7', '小雨', '13', '南风', '微风', '17:10', '出门记得带伞，行走驾驶做好防滑准备']
#             },
#                 'week': '四', 'nongli': '十二月廿一'
#         },
#         {
#             'date': '2023-01-13', 'info': {'dawn': ['7', '小雨', '13', '南风', '微风', '17:10'], 'day': ['8', '中雨', '16', '东北风', '微风', '06:54', '出门记得带伞，行走驾驶 做好防滑准备'], 'night': ['7', '小雨', '11', '东北风', '微风', '17:11', '出门记得带伞，行走驾驶做好防滑准备']}, 'week': '五', 'nongli': '十二月廿二'}, {'date': '2023-01-14', 'info': {'dawn': ['7', '小雨', '11', '东北风', '微风', '17:11'], 'day': ['7', '小雨', '12', '北风', '微风', '06:54'], 'night': [
#     '7', '小雨', '4', '北风', '微风', '17:12']}, 'week': '六', 'nongli': '十二月廿三'}, {'date': '2023-01-15', 'info': {'dawn': ['7', '小雨', '4', '北风', '微风', '17:12'], 'day': ['7', '小雨', '4', '北风', '微风', '06:54'], 'night': ['6', '雨夹雪', '0', '西北风', '微风', '17:13']}, 'week': '日', 'nongli': '十二月廿四'}, {'date': '2023-01-16', 'info': {'dawn': ['6', '雨夹雪', '0', '西北风', '微风', '17:13'], 'day': ['1', '多云', '4', '北风', '微风', '06:54'], 'night': ['0', '晴', '-1', '西北风', '微风', '17:14']}, 'week': '一', 'nongli': '十二月廿五'}], 'f3h': {'temperature': [{'jg': '20230112140000', 'jb': '17'}, {'jg': '20230112170000', 'jb': '14'}, {'jg': '20230112200000', 'jb': '14'}, {'jg': '20230112230000', 'jb': '13'}, {'jg': '20230113020000', 'jb': '13'}, {'jg': '20230113050000', 'jb': '13'}, {'jg': '20230113080000', 'jb': '16'}, {'jg': '20230113110000', 'jb': '16'}, {'jg': '20230113140000', 'jb': '15'}], 'precipitation': [{'jg': '20230112140000', 'jf': '0.5'}, {'jg': '20230112170000', 'jf': '0.5'}, {'jg': '20230112200000', 'jf': '0.5'}, {'jg': '20230112230000', 'jf': 3}, {'jg': '20230113020000', 'jf': 3}, {'jg': '20230113050000', 'jf': 3}, {'jg': '20230113080000', 'jf': 3}, {'jg': '20230113110000', 'jf': '7.5'}, {'jg': '20230113140000', 'jf': '0'}]}, 'pm25': {'pm25': {'level': 1, 'quality': '优', 'des': '空气很棒，快出门呼吸新鲜空气吧。', 'curPm': '25', 'pm25': '15', 'pm10': '17', 'pub_time': 1673506800, 'city_code': '101020100'}, 'cityName': '上海', 'key': '上海', 'dateTime': '2023年01月12日15时'}, 'jingqu': '', 'jingqutq': '', 'date': None, 'isForeign': 0, 'partner': {'title_word': ' 全国', 'show_url': 'tianqi.so.com', 'base_url': 'http://tianqi.so.com/weather/101020100'}}}
