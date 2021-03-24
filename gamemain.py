#gamenain
import random,sys


class Chicke():
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.gold = 100
        self.day = 0
        self.飽食度 = 100
        self.乾淨度 = 100
        self.sex = random.choice(['公♂','母♀'])
    def printall(self):
        print('printall')
        print(self.name,'的第',self.day,'天')
        print(self.name)
        print(self.age)
        print(self.gold)
        print(self.飽食度)
        print(self.乾淨度)
    def over_one_day(self):
        self.day += 1
        self.age = self.day//10
        self.飽食度 -= random.choice([0, 0, 0, 1, 1, 2, 3])
        self.gold -= random.choice([0, 0, 0 ,1, 1, 2, 3])
    def add飽食度(self,much):
        if self.飽食度 + much <= 100:
            self.飽食度 = self.飽食度 + much
        else:
            self.飽食度 = 100
    def add乾淨度(self,much):
        if self.乾淨度 + much <= 100:
            self.乾淨度 = self.乾淨度 + much
        else:
            self.乾淨度 = 100
    def addgold(self,much):
        if self.gold + much <= 100:
            self.gold = self.gold + much
        else:
            self.gold = 100
    def dead(self):
        if self.飽食度 <= 0 or self.乾淨度 <= 0:
            sys.exit('你的小雞掛了,它存活了：'+str(self.day)+'天')
def ObjStatus(Obj):
    return [str(Obj.name)+' 的第 '+str(Obj.day)+' 天','性別: '+str(Obj.sex),'年齡: '+str(Obj.age),'飽食度: '+Square_Bar(Obj.飽食度)+str(Obj.飽食度)+'/100','乾淨度: '+Square_Bar(Obj.乾淨度)+str(Obj.乾淨度)+'/100','心情值: '+Square_Bar(Obj.gold)+str(Obj.gold)+'/100']
def Square_Bar(statu):
#▉==5 statu 是屬性
    Bar = '【'
    for i in range(statu//5):
        Bar += '▉'
    for i in range(20-(statu//5)):
        Bar += '▁'
    Bar += '】'
    if statu <= 20:
        Bar += '!!!'
    return Bar

