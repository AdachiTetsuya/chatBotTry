from api.models import UserPollCommentCount, UserPollRelation

RAISE_LEVEL_COUNT_WEIGHT = 2


def update_continuous_day(comment_count: UserPollCommentCount):
    from datetime import datetime, timedelta

    today = datetime.today()
    yesterday = today - timedelta(days=1)
    previous_comment_time = comment_count.updated_at

    prev_date = previous_comment_time.day
    if prev_date == today.date:
        pass

    elif prev_date == yesterday.date:
        comment_count.increment_continuous_day_in_level()

    else:
        comment_count.continuous_day_in_level = 0


def update_count_value(comment_count: UserPollCommentCount):
    # カウント値のインクリメント
    update_continuous_day(comment_count)
    comment_count.increment_comment_total()
    comment_count.increment_comment_count_in_level()


def update_level(pre_level, poll: UserPollRelation, comment_count: UserPollCommentCount):
    # レベルの更新判定ロジック
    if comment_count.count_in_level >= pre_level * RAISE_LEVEL_COUNT_WEIGHT:
        if poll.relationship_level <= 2:
            poll.increment_relationship_level()

        elif poll.relationship_level == 3:
            if comment_count.continuous_day_in_level >= 1:
                poll.increment_relationship_level()

        elif poll.relationship_level == 4:
            if comment_count.continuous_day_in_level >= 4:
                poll.increment_relationship_level()


def compare_two_level(pre_level, poll: UserPollRelation, comment_count: UserPollCommentCount):
    # レベルの更新検出, カウント値のリセット
    now_level = poll.relationship_level
    if pre_level != now_level:
        comment_count.count_in_level = 0
        comment_count.continuous_day_in_level = 0


def update_comment_count_and_relationship_level(poll: UserPollRelation):
    pre_level = poll.relationship_level

    instance = UserPollCommentCount.objects.get(user_poll_relation=poll)

    # カウント値のインクリメント
    update_count_value(instance)

    # レベルの更新判定、更新
    update_level(pre_level, poll, instance)

    # レベルの更新検出
    compare_two_level(pre_level, poll, instance)

    # 保存
    instance.save()
    poll.save()
