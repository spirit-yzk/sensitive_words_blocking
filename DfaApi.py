from flask import Flask
from dfa import DFA
import json
app = Flask(__name__)
dfa = DFA()


@app.route('/filter/<string>')
def text_filter(string):
    response_dict = dict()
    if dfa.exists(string) is False:
        response_dict['is_illegal'] = False
    else:
        response_dict['is_illegal'] = True
        string = dfa.filter_all(string)
    response_dict['string'] = string
    response = json.dumps(response_dict)
    return response


@app.route('/add/<string>')
def add_new_words(string):
    if string in dfa.ban_words_set:
        return '"'+string+'"已在敏感词文档中，添加失败'
    dfa.add_new_word(string)
    with open(dfa.path, 'a', encoding='utf-8-sig') as f:
        f.writelines('\n'+string)
    return '添加成功'


@app.route('/change/<path>')
def chang_text(path):
    try:
        dfa.change_words(path)
    except FileNotFoundError:
        return '文件"'+path+'"不存在'
    return '已将文件"'+path+'"作为敏感词库'


if __name__ == '__main__':
    app.debug = True
    port = 4567
    app.run('0.0.0.0', port)
