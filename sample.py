# -*- coding: utf-8 -*-
from snownlp import SnowNLP
def onQQMessage(bot, contact, member, content):
    dict = {'reed':'丽姐',
        'Tinybody':'法医',
        '飘の迷茫':'群主',
        '后圣域传说':'港基',
        '阿兹纳布尔kke':'吴医生',
        '雪千夜的天国':'内裤子',
        'stormzhou':'Master'}

    if content == 'foo':
        bot.SendTo(contact, 'bar')
    else:
        s = SnowNLP(content)
        if '不开心' not in content and '很高兴' not in content:          
           if str(member.nick) in dict.keys():
                if s.sentiments >= 0.85:
                     bot.SendTo(contact, dict[str(member.nick)] + '看起来很高兴，发个红包吧！')
                elif s.sentiments <= 0.08:
                    bot.SendTo(contact, dict[str(member.nick)] + '好像不开心，摸摸头')
                else:
                    print ('a')
           else:      
               if s.sentiments >= 0.85:
                    bot.SendTo(contact, str(member.nick) + '看起来很高兴，发个红包吧！')
               elif s.sentiments <= 0.08:
                   bot.SendTo(contact, str(member.nick) + '好像不开心，摸摸头')
