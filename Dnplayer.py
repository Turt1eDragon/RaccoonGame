from Dnconsole import Dnconsole
import time


class Dnplayer:

    @staticmethod
    def chooseHero(index: int):
        x = 100
        y = 250
        Dnconsole.touch(0, x, y, 0)

    @staticmethod
    def leverUp():
        Dnconsole.touch(0, 450, 1370, 0)

    @staticmethod
    def cartoonJump():
        Dnconsole.touch(0, 800, 40, 0)

    @staticmethod
    def fightSure():
        Dnconsole.touch(0, 450, 1530, 0)

    @staticmethod
    def fightIn():
        Dnconsole.touch(0, 450, 1375, 0)

    @staticmethod
    def leftdownBack():
        Dnconsole.touch(0, 54, 1520, 0)

    @staticmethod
    def dungeon():
        Dnconsole.touch(0, 450, 1530, 0)

    @staticmethod
    def home():
        Dnconsole.touch(0, 325, 1530, 0)

    @staticmethod
    def hero():
        Dnconsole.touch(0, 630, 1500, 0)

    @staticmethod
    def Stub_server214():
        Dnconsole.touch(0, 570, 1000, 0)
        Dnconsole.touch(0, 630, 990, 0)

    @staticmethod
    def switchSeverPlayer():
        print("Switch player")
        Dnconsole.touch(0, 60, 60, 0)
        Dnconsole.touch(0, 795, 1356, 0)
        Dnconsole.touch(0, 250, 395, 0)
        Dnconsole.touch(0, 200, 650, 0)
        Dnconsole.touch(0, 640, 990, 0)

    @staticmethod
    def newPlayerJob():
        time.sleep(20)
        #跳过动画
        Dnconsole.touch(0, 845, 1450, 0)
        time.sleep(20)
        Dnconsole.swipe(0, (430, 850), (450, 1380), 0)
        time.sleep(10)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnplayer.fightIn()
        Dnconsole.touch(0, 280, 1050, 0)
        Dnconsole.touch(0, 100, 1050, 0)
        Dnplayer.fightSure()
        time.sleep(5)
        Dnconsole.touch(0, 360, 1350, 0)
        time.sleep(5)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnplayer.leftdownBack()
        #false
        time.sleep(5)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.swipe(0, (290, 695), (110, 594), 0)
        Dnconsole.touch(0, 115, 1060, 0)
        time.sleep(2)
        Dnconsole.touch(0, 450, 1500, 0)
        time.sleep(20)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 555, 1530, 0)
        Dnplayer.chooseHero(0)
        Dnplayer.fightIn()
        Dnconsole.touch(0, 770, 1370, 0)
        Dnplayer.leftdownBack()
        Dnplayer.home()
        Dnconsole.touch(0, 360, 1350, 0)
        Dnplayer.fightIn()
        time.sleep(3)
        Dnplayer.cartoonJump()
        Dnplayer.fightSure()
        time.sleep(5)
        Dnplayer.cartoonJump()
        time.sleep(10)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnplayer.fightIn()
        Dnplayer.fightIn()
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnplayer.cartoonJump()
        Dnplayer.fightIn()
        Dnconsole.touch(0, 360, 1350, 0)
        time.sleep(5)
        Dnconsole.touch(0, 455, 1260, 0)
        #true
        Dnplayer.fightSure()
        Dnconsole.touch(0, 820, 1200, 0)
        time.sleep(10)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnplayer.hero()
        Dnplayer.chooseHero(0)
        Dnplayer.leverUp()
        Dnconsole.touch(0, 650, 900, 0)
        Dnconsole.touch(0, 360, 1350, 0)
        Dnplayer.leftdownBack()
