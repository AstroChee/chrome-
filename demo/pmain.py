# -*- encoding:utf-8 -*-
'''
from __future__ import print_function

import sys

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
'''
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import numpy



def zy(text):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    print('摘要：')
    for item in tr4s.get_key_sentences(num=1):
        return item.sentence


'''
print(zy("在6月1日外交部例行记者会上，有来自CNN"
         "的记者提问称：有美国官员和机构提到了外国"
         "势力对当前美国局势的影响，包括美国国家安"
         "全顾问奥布莱恩，他尤其提到了中国社交媒体"
         "上对美国局势幸灾乐祸的表达。还有人注意到"
         "了不少社交媒体将美国局势和香港局势的比较。"
         "还有一家社交媒体监测机构的 CEO表示，他们"
         "也看到了来自中国、俄罗斯和伊朗的社交媒体网"
         "络的很多账号在有关美国局势上极其活跃的状态"
         "他们也在进行进一步的观测。不知道您对这些说"
         "法有什么评论和回应？对此，发言人赵立坚在"
         "回应中表示，奥布莱恩等官员和美方有关的分"
         "析是毫无根据的。“中方不干涉别国内政，同时"
         "世界人民通过媒体看到了美国正在发生的一切，"
         "美国政客们还是管好自己的事情。”他说，中方"
         "是有是非观念的，我们从来反对一切形式的暴力"
         "违法行为，我们也希望美方应正视国内存在的种"
         "族歧视问题。“关于你提到的将美国抗议示威同"
         "香港抗议活动相提并论的问题”，赵立坚表示，"
         "这两者起因完全不同。在香港修例风波中，内外"
         "敌对势力肆无忌惮地进行各种分裂国家、颠覆政"
         "权、组织实施恐怖活动，“港独”和黑色暴力活"
         "动是严重危害国家安全的行为。而美国发生的抗"
         "议活动的起因，美国媒体已经报道的非常充分"
         "了。“恐怕很多人也想问同样的问题：为什么美"
         "方将香港的所谓“港独”和黑色暴力分子美化为"
         "英雄，而将美国国内抗议种族歧视的民众称之为"
         "暴徒？为什么美方对香港警察克制文明执法横"
         "加指责，却对国内抗议者威胁开枪射击，甚至"
         "动用国民警卫队？”赵立坚指出，美方的做法是"
         "最典型的“世界驰名双重标准”，这背后反映出"
         "的问题是值得人们深思和警惕的。"))
'''