import MeCab

# 分かち書きオブジェクト
tagger = MeCab.Tagger("")
tagger.parse("")


def wakati_text(text, select_conditions=["動詞", "形容詞", "名詞", "感動詞"]):
    # 分けてノードごとにする
    node = tagger.parseToNode(text)
    terms = []

    while node:
        # 単語
        term = node.surface

        # 品詞
        pos = node.feature.split(",")[0]

        # もし品詞が条件と一致してたら
        if pos in select_conditions:
            terms.append(term)

        node = node.next
    return terms
