from .serializers import CustomUserSerializer


def save_user(username, line_id):
    data = {username: username, line_id: line_id}
    serializer = CustomUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        pass
