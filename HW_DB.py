import func_lib
import pymysql
import time

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='engns0403@', db='test_project')
#db = pymysql.connect(host ="localhost",user ="root",password="123123",database='nj',charset='utf8')

loop = 1
cur = db.cursor()

func_lib.initial_screen()

while loop == 1:
    instruction = func_lib.instruct_input()
    if instruction == "help":
        func_lib.instruct_help()
        continue
    elif instruction == "menu":
        func_lib.instruct_menu()
        continue
    elif instruction == "menuAdd":
        func_lib.intstruct_menuAdd()
        continue
    elif instruction == "order": #주문하기
        func_lib.instruct_order()
        continue
    elif instruction == "sales":  #매출조회
        func_lib.instruct_sales()
        continue
    elif instruction == "table":
        func_lib.instruct_table()  #계산 및 테이블현환
        continue
    elif instruction == "storage":
        func_lib.instruct_storage()
        continue
    elif instruction == "exit":
        break

db.close()
print("프로그램 종료합니다.")