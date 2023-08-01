from django.db.models import Prefetch

from celery import shared_task

from api.bot_base import LineBotMSG
from api.bot_messages import create_text_message_list
from api.models import SmartPoll, UserPollRelation

line_message = LineBotMSG()


def get_weather_data_sentence(poll: SmartPoll, weather_data):
    temperature = weather_data.get("temperature")
    humidity = weather_data.get("humidity")
    uv_level = weather_data.get("UV")

    result = ""
    if poll.default_name == "ケイ":
        result = f"今日の気温は{temperature}度です、暑い..."
    if poll.default_name == "ユウ":
        result = f"今日の湿度は{humidity}%です!カラっから！"
    if poll.default_name == "ケイ":
        result = f"今日の紫外線は UVレベル{uv_level} です、お肌をお大事に！"

    return result


def get_weather_data():
    weather_data = {
        "temperature": 30,  # セ氏度
        "humidity": 60,  # % の値
        "UV": 4,  # level (1~5) の値
    }
    return weather_data


@shared_task
def wether_data_message():
    # 気象データの取得 (気温、湿度、UV)
    weather_data = get_weather_data()

    # ユーザとバディ登録の確認
    smart_polls = SmartPoll.objects.prefetch_related(
        Prefetch(
            "user_relation",
            queryset=UserPollRelation.objects.select_related("user").filter(is_buddy=True),
        )
    )

    for smart_poll in smart_polls:
        line_id_list = [
            buddy_relation.user.line_id for buddy_relation in smart_poll.user_relation.all()
        ]

        # マルチキャストメッセージの送信
        text = get_weather_data_sentence(smart_poll, weather_data)
        result = create_text_message_list(text)
        line_message.multi_cast_message(line_id_list, result)
