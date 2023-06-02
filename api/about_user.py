import logging

from api.models import SmartPoll, UserPollRelation

from .serializers import CustomUserSerializer

logger = logging.getLogger("api")


def save_user(username, line_id):
    data = {"username": username, "line_id": line_id}
    serializer = CustomUserSerializer(data=data)
    logger.info(serializer.is_valid())
    if serializer.is_valid():
        return serializer.save()
    else:
        logger.info(serializer.errors)
        print(serializer.errors)


def create_user_poll_relation(user, user_line_id=None):
    """
    新規ユーザの場合、UserPollRelation の create をする

    return
        ユーザと関係を持つ UserPollRelation の クエリセット
    """
    if user:
        objects = []
        for poll in SmartPoll.objects.all():
            obj = UserPollRelation.objects.create(user=user, smart_poll=poll)
            objects.append(obj)
        return objects
    elif user_line_id:
        return UserPollRelation.objects.filter(user__line_id=user_line_id)
