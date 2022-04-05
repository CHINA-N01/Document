from xpinyin import Pinyin
import re

# 实例拼音转换对象
p = Pinyin()
# 进行拼音转换
ret = p.get_pinyin(u"汉语拼音转换", tone_marks='marks')
ret1 = p.get_pinyin(u"汉语拼音转换", tone_marks='numbers')
print(ret + '\n' + ret1)
#text=re.sub('-','',ret1)
text=re.findall('[a-zA-z.]',ret1)
print(text)

# 得到转化后的结果
# hàn-yǔ-pīn-yīn-zhuǎn-huàn
# han4-yu3-pin1-yin1-zhuan3-huan4