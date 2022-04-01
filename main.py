from Dnconsole import Dnconsole
from Player import Player
from AccountReader import CSVDealer
from datetime import datetime
import time
import easygui


def openGame():
    Dnconsole.invokeapp(0, "com.changyou.xhxshz")


def PlayerJob(account: str, pswd: str, classId: str):
    Player.SwitchJob(account, pswd)
    time.sleep(15)
    Player.EverydayJob(classId)
    return


def gameStub(classId: str, exeNum: int):
    Today = str(datetime.today().date())
    TodayList = [int(i) for i in str(datetime.today().date()).split('-')]
    accounts = CSVDealer.read()
    index = 0
    column = 0
    for account in accounts:
        excuteDay = [int(i) for i in account[2].split('/')] if account[2] != '' else [0,0,0]
        if excuteDay[0] != TodayList[0] | excuteDay[1] != TodayList[1] | excuteDay[2] != TodayList[2]:
            print('执行账号: '+account[0]+'  密码: '+account[1]+'  上次执行时间: '+account[2])
            PlayerJob(account[0], account[1], classId)
            account[2] = Today
            index += 1
            print('剩余执行数量: ' + str(exeNum-index))
            print()
            accounts[column] = account
            CSVDealer.write(accounts)
            if index >= exeNum:
                print('执行结束，没有多余账号继续执行')
                break
        column += 1


def GUI():
    msg = "小浣熊自动脚本"
    title = "小浣熊自动脚本v1.0"
    names = ['班级编号', '执行数量']
    values = []
    values = easygui.multenterbox(msg, title, names)
    if not values[0].isdigit():
        easygui.msgbox("班级编号需要为数字", ok_button='确定')
        exit(0)
    else:
        if not values[1].isdigit():
            easygui.msgbox("执行数量需要为数字", ok_button='确定')
            exit(0)
    return values


def EXIT():
    exit_choice = easygui.buttonbox('脚本运行中', title='小浣熊自动脚本v1.0', choices=['退出运行'], default_choice='退出运行')
    if exit_choice == '退出运行':
        exit(0)


if __name__ == '__main__':
    print('----------小浣熊自动执行脚本----------\n')
    print('--------------神游联盟--------------')
    str_classId = input('请输入班级编号：')
    str_num = input('请输入执行数量：')

    input("是否开始进行任务？")

    print("start job")
    openGame()
    print('等待运行...60s...剩余60s')
    time.sleep(30)  # 等待启动
    print('等待运行...60s...剩余30s')
    time.sleep(30)
    gameStub(str_classId, int(str_num))

    print("quit job")
    Dnconsole.quit(0)  # 退出模拟器
    input('按任意键结束程序...')


