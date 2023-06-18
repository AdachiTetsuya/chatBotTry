from api.models import UserPollRelation


def get_event_obj(text):
    event_obj = {"message": {"text": text}}
    return event_obj


def get_user_poll_relations(user):
    user_poll_relations = UserPollRelation.objects.filter(user=user)
    return user_poll_relations


# テストコード
# from api.test.test_data import get_event_obj, get_user_poll_relations
# from api.models import CustomUser
# from api.sequences.receive_message import receive_message_function

# user = CustomUser.objects.get(line_id="asdf")
# user_poll_relations = get_user_poll_relations(user)
# event_obj = get_event_obj("ユウのプロパティを変更します")
# receive_message_function(event_obj, user, user_poll_relations)
