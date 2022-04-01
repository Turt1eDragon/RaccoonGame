from Dnconsole import Dnconsole
import time


class Player:
    @staticmethod
    def SwitchJob(account: str, pswd: str):
        print('  切换账号')
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 137, 85, 0)
        Dnconsole.touch(0, 973, 1626, 0)
        Dnconsole.touch(0, 793, 622, 0)
        time.sleep(10)
        Dnconsole.touch(0, 304, 1240, 0)
        Dnconsole.touch(0, 317, 820, 0)
        Dnconsole.input_text(0, account)
        Dnconsole.touch(0, 350, 1050, 0)
        Dnconsole.input_text(0, pswd)
        Dnconsole.touch(0, 530, 1250, 0)

    @staticmethod
    def EverydayJob(number: str):
        # 清除广告
        print('  清除广告')
        Player.removeAdv()
        # 领邮件
        print('  领邮件')
        Player.getMail()
        # 挂机奖励
        print('  挂机奖励')
        Player.afkReward()
        time.sleep(10)
        Player.afkReward()
        # 快速挂机
        print('  快速挂机')
        Player.fast_afkReward()
        # 挑战关卡
        print('  全国大赛')
        Player.dungeon()
        # 切换到街区
        print('  切换至街区')
        Player.switchDistrict()
        # 向上拖
        print('  上拉')
        Player.drag(False)
        # 抽奖
        print('  小卖部')
        Player.lottery()
        # 加入班级
        print('  进入班级')
        Player.myClass(number)
        # 向下拖
        print('  下拉')
        Player.drag(True)
        # 水浒快打
        print('  水浒快打')
        Player.shuihukuaida()
        # 街头对战
        print('  街头对战')
        Player.jietouduizhan()
        # 领奖励
        print('  奖励领取')
        Player.getEverydayJobReward()
        # 结束，退班
        print('  退出班级，清零')
        Dnconsole.touch(0, 100, 1836, 0)
        Dnconsole.touch(0, 100, 1836, 0)
        Dnconsole.touch(0, 100, 1836, 0)
        Dnconsole.touch(0, 100, 1836, 0)
        Dnconsole.touch(0, 100, 1836, 0)
        print('  退出班级，上拉')
        Player.drag(False)
        print('  退出班级，退出')
        Player.leaveClass()
        print(' 账号执行结束')

    @staticmethod
    def removeAdv():
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)

    @staticmethod
    def getMail():
        Dnconsole.touch(0, 992, 483, 0)
        Dnconsole.touch(0, 992, 656, 0)
        Dnconsole.touch(0, 772, 1670, 0)
        time.sleep(5)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 327, 1670, 0)
        Dnconsole.touch(0, 760, 1200, 0)
        Dnconsole.touch(0, 80, 1745, 0)

    @staticmethod
    def afkReward():
        # afk: away from keyboard
        Dnconsole.touch(0, 920, 1620, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)

    @staticmethod
    def fast_afkReward():
        Dnconsole.touch(0, 920, 1620, 0)
        Dnconsole.touch(0, 330, 1450, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)

    @staticmethod
    def dungeon():
        Dnconsole.touch(0, 550, 1650, 0)
        Dnconsole.touch(0, 542, 1720, 0)
        time.sleep(2)
        Dnconsole.touch(0, 550, 1836, 0)
        time.sleep(5)
        Dnconsole.touch(0, 50, 1430, 0)
        Dnconsole.touch(0, 240, 950, 0)

    @staticmethod
    def switchDistrict():
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 100, 1800, 0)

    @staticmethod
    def lottery():
        Dnconsole.touch(0, 276, 1537, 0)
        Dnconsole.touch(0, 300, 1370, 0)
        Dnconsole.touch(0, 875, 1830, 0)
        time.sleep(5)
        Dnconsole.touch(0, 60, 1840, 0)
        Dnconsole.touch(0, 60, 1840, 0)
        Dnconsole.touch(0, 60, 1840, 0)
        Dnconsole.touch(0, 60, 1840, 0)

    @staticmethod
    def myClass(number: str):
        Dnconsole.touch(0, 321, 1111, 0)
        Dnconsole.touch(0, 450, 280, 0)
        Dnconsole.input_text(0, '\b\b\b\b\b\b\b\b\b\b\b\b\b' + number)
        Dnconsole.touch(0, 1020, 1820, 0)
        Dnconsole.touch(0, 930, 280, 0)
        Dnconsole.touch(0, 470, 540, 0)
        Dnconsole.touch(0, 540, 1650, 0)
        time.sleep(5)
        Dnconsole.touch(0, 65, 1800, 0)
        Dnconsole.touch(0, 65, 1800, 0)
        # 水浒快打
        # Dnconsole.touch(0, 110, 330, 0)
        # Dnconsole.touch(0, 560, 1830, 0)
        # Dnconsole.touch(0, 130, 1250, 0)
        # Dnconsole.touch(0, 130, 1450, 0)
        # Dnconsole.touch(0, 550, 1836, 0)
        # time.sleep(60)
        # Dnconsole.touch(0, 550, 1700, 0)
        # Dnconsole.touch(0, 65, 1800, 0)
        # Dnconsole.touch(0, 65, 1800, 0)
        # Dnconsole.touch(0, 65, 1800, 0)
        # Dnconsole.touch(0, 65, 1800, 0)

    @staticmethod
    def shuihukuaida():
        Dnconsole.touch(0, 100, 1800, 0)
        Dnconsole.touch(0, 370, 980, 0)
        Dnconsole.touch(0, 460, 1825, 0)
        Dnconsole.touch(0, 540, 1300, 0)
        Dnconsole.touch(0, 550, 1130, 0)
        Dnconsole.touch(0, 550, 1836, 0)
        time.sleep(3)
        Dnconsole.touch(0, 50, 1430, 0)
        Dnconsole.touch(0, 240, 950, 0)
        Dnconsole.touch(0, 65, 1800, 0)
        Dnconsole.touch(0, 65, 1800, 0)

    @staticmethod
    def jietouduizhan():
        Dnconsole.touch(0, 780, 850, 0)
        Dnconsole.touch(0, 550, 1400, 0)
        Dnconsole.touch(0, 500, 1850, 0)
        Dnconsole.touch(0, 850, 720, 0)
        Dnconsole.touch(0, 550, 1836, 0)
        time.sleep(20)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 550, 1850, 0)
        Dnconsole.touch(0, 62, 1820, 0)
        Dnconsole.touch(0, 62, 1820, 0)
        Dnconsole.touch(0, 62, 1820, 0)

    @staticmethod
    def getEverydayJobReward():
        Dnconsole.touch(0, 1000, 375, 0)
        Dnconsole.touch(0, 920, 725, 0)
        Dnconsole.touch(0, 920, 725, 0)
        Dnconsole.touch(0, 920, 725, 0)
        Dnconsole.touch(0, 920, 725, 0)
        Dnconsole.touch(0, 920, 725, 0)
        Dnconsole.touch(0, 920, 725, 0)
        # Dnconsole.touch(0, 920, 725, 0)

        Dnconsole.touch(0, 350, 410, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 510, 410, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 666, 410, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 810, 410, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 970, 410, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 518, 1644, 0)
        Dnconsole.touch(0, 70, 1700, 0)

    @staticmethod
    def drag(direction: bool):
        if (direction):
            Dnconsole.swipe(0, (540, 1700), (540, 180), 0)
            Dnconsole.swipe(0, (540, 1700), (540, 180), 0)
        else:
            Dnconsole.swipe(0, (540, 180), (540, 1700), 0)
            Dnconsole.swipe(0, (540, 180), (540, 1700), 0)

    @staticmethod
    def leaveClass():
        Dnconsole.touch(0, 345, 1150, 0)
        time.sleep(1)
        Dnconsole.touch(0, 546, 685, 0)
        Dnconsole.touch(0, 1004, 178)
        Dnconsole.touch(0, 940, 350)
        Dnconsole.touch(0, 760, 1200, 0)
        Dnconsole.touch(0, 65, 1800, 0)
        Dnconsole.touch(0, 65, 1800, 0)
        Dnconsole.touch(0, 65, 1800, 0)
        Dnconsole.touch(0, 65, 1800, 0)
