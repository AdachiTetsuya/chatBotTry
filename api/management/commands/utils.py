from django.core.management.base import CommandError


def get_row_num(header_length, row_num):
    result = header_length + row_num
    return f"{result} 行目"


def is_all_empty_str_row(row):
    """空文字だけの行かどうか判定"""
    return all(elem == "" for elem in row)


def convert_problem_type_to_num(data):
    result = 0
    if data == "select":
        result = 1
    elif data == "text":
        result = 2
    elif data == "coding":
        result = 3
    else:
        raise CommandError("Problem_type = %s は存在しません" % data)
    return result


def convert_to_boolean(data):
    return bool(data)


def convert_coding_type_to_num(data):
    result = 0
    if data == "IOPair":
        result = 1
    elif data == "PerfectMatch":
        result = 2
    else:
        raise CommandError("Problem_coding_type = %s は存在しません" % data)
    return result


def convert_coding_lang_to_num(data):
    result = 0
    if data == "html":
        result = 1
    elif data == "css":
        result = 2
    elif data == "javascript":
        result = 3
    elif data == "python":
        result = 4
    else:
        raise CommandError("Problem_coding_type = %s は存在しません" % data)
    return result
