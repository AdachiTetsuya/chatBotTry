from api.models import CustomUser, UserPollRelation


def get_event_obj(text):
    event_obj = {"message": {"text": text}}
    return event_obj


def get_user_poll_relations(user_name):
    user = CustomUser.objects.get(username=user_name)
    user_poll_relations = UserPollRelation.objects.filter(user=user)
    return user_poll_relations
