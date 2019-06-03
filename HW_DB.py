import func_lib
import pymysql
import time

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='engns0403@', db='test_project')
loop = 1
cur = db.cursor()

func_lib.initial_screen()

while loop == 1:
    instruction = func_lib.instruct_input()
    if instruction == "help":
        func_lib.instruct_help()
        continue
    elif instruction == "메뉴":
        func_lib.instruct_allmenu()
        continue
    elif instruction == "계산":
        func_lib.instruct_casher()
        continue
    elif instruction == "매출":
        func_lib.instruct_sales()
        continue
    elif instruction == "종료":
        break

db.close()
print("프로그램 종료합니다.")