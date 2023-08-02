from api.bot_messages import (
    create_image_message_list,
    create_quick_reply_text_list,
    create_text_message_list,
)
from api.models import SmartPoll
from api.utils import judge_comment_from_temperature
from api.weather_base import WeatherApi

weather_api = WeatherApi()


def sky_photo():
    if smart_poll := SmartPoll.objects.filter(can_sky_photo=True).first():
        url = smart_poll.get_sky_photo()
        text_list = create_text_message_list("今日の空の写真です")
        image_list = create_image_message_list(url)
        text_list.extend(image_list)
        return text_list


def show_temperature():
    smart_poll = SmartPoll.objects.first()
    temperature = smart_poll.get_temperature()
    comment = judge_comment_from_temperature(temperature)
    text_list = create_text_message_list(f"今日の気温は{temperature}度です。{comment}")
    dialog = create_quick_reply_text_list("もっと知りたいですか？", [("はい", "気象の詳細を教えて"), ("いいえ", "結構です")])
    text_list.extend(dialog)
    return text_list


def show_weather_detail():
    title = "気象の詳細データです"
    temperature = weather_api.get_temperature()
    humidity = weather_api.get_humidity()
    pressure = weather_api.get_pressure()
    UV_level = weather_api.get_UV_level()

    data_text = f"気温: {temperature}度\n湿度: {humidity} %\n気圧: {pressure} hPa\nUV: Level {UV_level}"

    text_list = create_text_message_list(title, data_text)
    return text_list
