import jieba


def cut(sentence):
    return list(jieba.cut(sentence))


if __name__ == '__main__':
    print(cut('今天天气真好！'))
