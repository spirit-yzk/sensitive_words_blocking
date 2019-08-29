import dfa
# 创建一个dfa对象
dfa = DFA()

# 过滤实例
s1 = '日、你￥，妈,1,2#@3,ffsf妈 *卖 *批,'
s2 = dfa.filter_all(s1)
print(s1)
print(s2)
# 输出结果如下
# 日、你￥，妈,1,2#@3,ffsf妈 *卖 *批,
# ******,1,2#@3,ffsf妈 *卖 *批,

# 检查是否存在敏感词,存在返回True,不存在返回False,不改变字符串
dfa.exists(s1)

# 添加敏感词
s = 'sb'
dfa.add_new_word(s)

# 指定新的敏感词库
dfa.change_words(path)
