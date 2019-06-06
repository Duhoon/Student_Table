import pymysql
import time
import random
from prettytable import PrettyTable

#db = pymysql.connect(host='localhost', port=3306, user='root', passwd='engns0403@', db='test_project')
db = pymysql.connect(host='localhost',  user='root', passwd='123123', db='nj2')
cur = db.cursor()
now = time.strftime('%Y%m%d', time.localtime())
#pay =0
#tablenum = 0
#num = 0
#menu = ''
#Mnum = 0


def initial_screen():
    print("\t\tST-POS시스템을 사용해주셔서 감사합니다.")
    print("--------------------------------------------------------")
    print("\t\t 메뉴 \t\t 계산 \t\t 매출 \t\t 고객")
    print("--------------------------------------------------------")
    print("프롬프트에 'help'를 치시면 사용 가능한 명령어를 확인하실 수 있습니다.")
def instruct_input():
    instruction = input(">> ")
    return instruction


def instruct_help():
    print("\n프롬프트에 다음 설명하는 것을 입력하세요.")
    print("menu       현재 매장에서 판매하는 메뉴 확인")
    print("casher     계산 시스템 활성화")
    print("sales      데이터베이스에 있는 매출을 출력")
    print("exit       프로그램 종료")

def instruct_allmenu():
    cur.execute("select * from menu")
    print("-----------------------------")
    print("\tmID\t메뉴이름\t\t가격")
    for row in cur.fetchall():
        print("\t", row[0], "\t", row[1], "\t", row[2])
    print("-----------------------------")

def instruct_order():
   stop = 'y'
   pay=0
   cur.execute("select sId from sales;")  # sid 조회
   num = random.randrange(0, 100)
   sID = cur.fetchall()
   print(sID);
   while num in sID:  # 중복될 경우
       num = random.randrange(0, 100)  # 다시 난수 생성
   # 여기다가 주문추가
   sID = num
   tablenum = int(input("\t테이블을 선택하세요(1~5번)"))

   while stop != 'n':


       menu = input("\t메뉴 : ")
       cur.execute("select price from menu where mnName = " + "\""+menu + "\"" + ";")
       items = cur.fetchall()
       cur.execute("select mnID from menu where mnName = " + "\"" + menu + "\"" + ";")
       menu_ID = cur.fetchall()
       Mnum = int(input("\t개수 : " ))


       pay = pay + (items[0][0] * Mnum)
       cur.execute("insert into sales values (" + str(num) + ", " + str(
           tablenum) + ", \'" + str(menu_ID[0][0]) + "\', " + str(Mnum) + ", " + str(now) + ", \'" + str('n') + "\')")
       stop = input("메뉴를 추가 하시겠습니까?(y or n) : ")


def instruct_table():
    stop = 'n'
    print("-----------------------------")
    print("\t\t1번테이블 ")
    pay1=0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=1 and complete = 'n' and menu.mnId=sales.mnId;"):
        table = PrettyTable()
        table.field_names= ["메뉴", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0],row[1]])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay1 = pay1 + (item[0][0] * row[1])

        print(table)
        print("총액:",pay1)

    else:
        print("빈테이블")
    print("-----------------------------")

    print("\t\t2번테이블")
    pay2=0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=2 and complete = 'n' and menu.mnId=sales.mnId;"):
        table = PrettyTable()
        table.field_names = ["메뉴", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0], row[1]])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay2 = pay2 + (item[0][0] * row[1])

        print(table)
        print("총액:", pay2)
    else:
        print("빈테이블")
    print("-----------------------------")
    print("\t\t3번테이블")
    pay3=0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=3 and complete = 'n' and menu.mnId=sales.mnId;"):
        table = PrettyTable()
        table.field_names = ["메뉴", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0], row[1]])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay3 = pay3 + (item[0][0] * row[1])

        print(table)
        print("총액:", pay3)
    else:
        print("빈테이블")
    print("-----------------------------")
    print("\t\t4번테이블")
    pay4 = 0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=4 and complete = 'n' and menu.mnId=sales.mnId;"):
        table = PrettyTable()
        table.field_names = ["메뉴", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0], row[1]])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay4 = pay4 + (item[0][0] * row[1])

        print(table)
        print("총액:", pay4)
    else:
        print("빈테이블")
    print("-----------------------------")
    print("\t\t5번테이블")
    pay5 = 0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=5 and complete = 'n' and menu.mnId=sales.mnId;"):
        table = PrettyTable()
        table.field_names = ["메뉴", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0], row[1]])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay5 = pay5 + (item[0][0] * row[1])

        print(table)
        print("총액:", pay5)
    else:
        print("빈테이블")

    stop = input("계산하시겠습니까?y/n(메뉴 돌아가기는 h)")

    if stop == 'y':
        tablenum = int(input("몇번 테이블을 계산하시겠습니까?(1~5번)"))
        if cur.execute("UPDATE sales SET complete='y' WHERE complete='n' and tableNum = " + str(tablenum )+ ";") :
            if tablenum == 1:
                print("총액:", pay1)
            elif tablenum ==2 :
                print("총액:",pay2)
            elif tablenum == 3:
                print("총액:", pay3)
            elif tablenum == 4:
                print("총액:",pay4)
            elif tablenum == 5:
                print("총액:", pay5)
            print("계산완료")

        else:
            print("빈테이블 입니다!")
    if stop =='n':
        instruct_table()
    if stop =='h':
        initial_screen()


def instruct_sales():
    print("일별 매출 : daily | 월별 매출 : monthly | 메뉴별 매출 : menu")
    print("날씨별 매출 : weather | 주문당 매출 : sales\n")
    clfy = input("확인하고 싶은 매출 카테고리 입력 : ")

    if clfy == "sales":
        cur.execute("select sDate, sID, mnName, sNum, price * sNum from sales, menu where sales.mnID = menu.mnID")
        print("------------------------------------------------------")
        print("\t날짜시간\t\t\t\t주문ID\t\t메뉴이름\t\t\t개수\t\t매출총합")
        for row in cur.fetchall():
            print("\t", row[0], "\t\t", row[1], "\t\t", row[2], "\t\t", row[3], "\t", row[4])
        print("------------------------------------------------------")

    elif clfy == "daily":
        cur.execute("select sDate, sNum, sumprice from dailySales")
        print("------------------------------------------------------")
        print("\t날짜시간\t\t\t\t개수\t\t매출총합")
        for row in cur.fetchall():
            print("\t", row[0], "\t\t", row[1], "\t\t", row[2])
        print("------------------------------------------------------")

    elif clfy == "monthly":
        print("서비스 준비 중입니다.")

    elif clfy == "menu":
        cur.execute("select mnName, sNum, sumprice from mnSales")
        print("------------------------------------------------------")
        print("\t메뉴이름\t팔린개수\t\t매출총합")
        for row in cur.fetchall():
            print("{:<10}".format(str(row[0])), "{:>10}".format(str(row[1])) )
        print("------------------------------------------------------")

    elif clfy == "wheather":
        print("서비스 준비 중입니다.")

#def instruct_storage():

    select= int(input("select number\n"
          "1.재고 조회"
          "2.재료 발주")}
    if select ==1 :
        cur.execute("select * from  ")

    cur.execute("select * from ")

    print("")


if __name__ == "__main__":
    print("이게 메인일 때 출력")
