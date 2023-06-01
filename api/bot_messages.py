def create_text_message_list(*args):
    if args:
        message = [{"type": "text", "text": msg} for msg in args]
    return message
