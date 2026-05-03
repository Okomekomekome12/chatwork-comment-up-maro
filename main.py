import time
import chatwork
import threading as td

print("初期化中")
time.sleep(300) # 初期化用

API_TOKEN = "4776bacb2f286251d40a56af3aaa9baa"
first_room_id = 435850950
second_room_id = 435850954
third_room_id = 435850957
forth_room_id = 435850959
fifth_room_id = 435850960
sixth_room_id = 435850962
seventh_room_id = 435850968
eighth_room_id = 435850968

cw1 = chatwork.setup(first_room_id,API_TOKEN)
cw2 = chatwork.setup(second_room_id,API_TOKEN)
cw3 = chatwork.setup(third_room_id,API_TOKEN)
cw4 = chatwork.setup(forth_room_id,API_TOKEN)
cw5 = chatwork.setup(fifth_room_id,API_TOKEN)
cw6 = chatwork.setup(sixth_room_id,API_TOKEN)
cw7 = chatwork.setup(seventh_room_id,API_TOKEN)
cw8 = chatwork.setup(eighth_room_id,API_TOKEN)

def first_room():
    while True:
        cw1.messagesend("うおw")
        time.sleep(5)
def second_room():
    while True:
        cw2.messagesend("うおw")
        time.sleep(5.2)
def third_room():
    while True:
        cw3.messagesend("うおw")
        time.sleep(5.3)
def forth_room():
    while True:
        cw4.messagesend("うおw")
        time.sleep(5.4)
def fifth_room():
    while True:
        cw5.messagesend("うおw")
        time.sleep(5.5)
def sixth_room():
    while True:
        cw6.messagesend("うおw")
        time.sleep(5.6)
def seventh_room():
    while True:
        cw7.messagesend("うおw")
        time.sleep(5.7)
def eighth_room():
    while True:
        cw8.messagesend("うおw")
        time.sleep(5.8)

thread1 = td.Thread(target=first_room)
thread2 = td.Thread(target=second_room)
thread3 = td.Thread(target=third_room)
thread4 = td.Thread(target=forth_room)
thread5 = td.Thread(target=fifth_room)
thread6 = td.Thread(target=sixth_room)
thread7 = td.Thread(target=seventh_room)
thread8 = td.Thread(target=eighth_room)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
