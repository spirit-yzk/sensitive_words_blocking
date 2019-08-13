from dfa import DFA
import pytest
import random
import time
ban_words_set = set()
ban_words_list = list()
example100k = list()
dfa = DFA()


def test_get_words():
    with open('sensitive_words.txt', 'r', encoding='utf-8-sig') as f:
        for s in f:
            if s.find('\\r'):
                s = s.replace('\r', '')
            s = s.replace('\n', '')
            s = s.strip()
            if len(s) == 0:
                continue
            if str(s) and s not in ban_words_set:
                ban_words_set.add(s)
                ban_words_list.append(str(s))
        for _ in range(10000):
            example100k.append(str_generator())


def str_generator():
    str_test = str()
    for _ in range(random.randint(1, 200)):
        if random.random() < 0.1:
            str_test += random.choice(ban_words_list)
        else:
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xf9)
            val = f'{head:x}{body:x}'
            str_test += bytes.fromhex(val).decode('gb2312')
    # print(str_test)
    new_str = str()
    for x in str_test:
        new_str += x
        if random.random() < 0.5:
            new_str += ' '
    # print(new_str)
    return new_str


def test_filter_sentence():
    s = "打倒中共共产党，法轮功万岁，妈卖批也。。。。"
    assert dfa.filter_all(s), "打倒*，*万岁，*也。。。。"

    s = "我在马路边，捡到妈卖"
    assert dfa.filter_all(s), "我在马路边，捡到妈卖"


def test_exists():
    s = "打倒中共共产党，法轮功万岁，妈卖批也。。。。"
    assert dfa.exists(s) is True
    # print(dfa.exists(s))
    s = "今天天骑真好"
    # print(dfa.exists(s))
    assert dfa.exists(s) is False


def test_filter():
    start_time = time.time()
    for i in example100k:
        # print(i)
        i = dfa.filter_all(i)
        # print(i)
    end_time = time.time()
    print("filter的平均时间:", (end_time-start_time)/10000)
    test_str = '1腐# 败 中 国1打 倒 中 ￥？共1吗啡'
    print("原语句:", test_str, sep='')
    print('修改之后的语句:', dfa.filter_all(test_str), sep='')


if __name__ == '__main__':
    pytest.main(['-q', 'TestDFA.py'])
