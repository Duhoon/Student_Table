import pymysql
import time
import random
from prettytable import PrettyTable
from openpyxl import Workbook
from openpyxl import load_workbook

#db = pymysql.connect(host='localhost', port=3306, user='root', passwd='engns0403@', db='test_project')
db = pymysql.connect(host='localhost',  user='root', passwd='123123', db='nj2')
cur = db.cursor()
now = time.strftime('%Y%m%d', time.localtime())

#Mnum = 0


def initial_screen():
    print("\t\tST-POS시스템을 사용해주셔서 감사합니다.")
    print("-----------------------------")
    print("\n프롬프트에 다음 설명하는 것을 입력하세요.")
    print("menu       현재 매장에서 판매하는 메뉴 확인")
    print("menuAdd    메뉴 추가 기능")
    print("order      주문 입력 활성화")
    print("table      테이블 현황 파악 및 계산 기능")
    print("sales      데이터베이스에 있는 매출 카테고리별 출력")
    print("storage    재고관리 기능 실행")
    print("exit       프로그램 종료")
def instruct_input():
    instruction = input(">> ")
    return instruction

def instruct_menu():
    cur.execute("select * from menu")
    print("-----------------------------")
    table = PrettyTable()
    table.field_names = ["메뉴", " 가격 "]
    for row in cur.fetchall():
        table.add_row([row[1], row[2]])
    print(table)
    print("-----------------------------")

    stop = input("홈으로 가려면 아무버튼을 눌러주세요")
    if stop =='':
        initial_screen()
    else:
        initial_screen()

def intstruct_menuAdd():
    print("메뉴 추가하기")
    menuid = input("메뉴 id 를 입력하세요 (영어로 두글자 써주세요!)")
    menuname=input("메뉴 이름을 입력하세요")
    menuprice=int(input("가격을 입력하세요"))
    cur.execute("select mtName,mtQuantity from materials")
    table = PrettyTable()
    table.field_names = ["재료이름", " 수량 "]
    for row in cur.fetchall():
        table.add_row([row[0], row[1]])
    print(table)
    mt=input("들어가는 메뉴를 골라주세요")
    cur.execute("select mtID from materials where mtName = '"+str(mt)+"';")
    mtID = cur.fetchall()
    cur.execute("insert into menu values (\'" + str(menuid) + "\', \'" + str(menuname) + "\'," + str(menuprice) +",\'"+str(mtID[0][0])+"\')")

    print("메뉴 추가완료")

    stop = input("홈으로 가려면 아무버튼을 눌러주세요")
    if stop == '':
        initial_screen()
    else:
        initial_screen()

def instruct_order():
   stop = 'y'
   pay=0
   cur.execute("select sId from sales;")  # sid 조회
   num = random.randrange(0, 100)
   sID = cur.fetchall()
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

   stop2=input("테이블현황을 보려면 t 를 눌러주세요,홈으로 돌아가려면 h를 눌러주세요")
   if stop2=="t" :
       instruct_table()
   elif stop2 =='h':
       initial_screen()


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

    stop = input("계산하시겠습니까?y/n(메뉴 돌아가기는 n)")

    if stop == 'y':
        tablenum = int(input("\n\n몇번 테이블을 계산하시겠습니까?(1~5번)"))
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
            stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
            if stop == 'y':
                instruct_table()
            elif stop == 'h':
                initial_screen()

        else:
            print("빈테이블 입니다!")
    if stop =='n':
        initial_screen()


def instruct_sales():
    menutable = PrettyTable()
    menutable.field_names=["조회","명령어"]
    menutable.add_row(["날짜별 매출","daily"])
    menutable.add_row(["월별 매출","monthly"])
    menutable.add_row(["메뉴별 매출","menu"])
    menutable.add_row(["날씨별 매출","weather"])
    menutable.add_row(["주문건당 매출","sales"])
    menutable.add_row(["미세먼지 농도별 매출","dust"])
    print(menutable)
    clfy = input("확인하고 싶은 매출 카테고리 입력 : ")

    if clfy == "sales":
        cur.execute("select sDate, sID, mnName, sNum, price * sNum from sales, menu where sales.mnID = menu.mnID")
        table = PrettyTable()
        table.field_names = ["날짜", "주문ID", "메뉴이름", "개수", "매출총합"]
        for row in cur.fetchall():
            table.add_row([row[0], row[1], row[2], row[3], row[4]])
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_sales()
        elif stop =='h':
            initial_screen()

    elif clfy == "daily":
        cur.execute("select sDate, sNum, sumprice from dailySales")
        table = PrettyTable()
        table.field_names = ["날짜", "개수", "매출총합"]
        for row in cur.fetchall():
            table.add_row([row[0], row[1], row[2]])
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_sales()
        elif stop == 'h':
            initial_screen()

    elif clfy == "monthly":
        cur.execute("select sYear, sMonth, sNum, sumprice from monSales")
        table = PrettyTable()
        table.field_names = ["연도", "월", "판매량", "매출총합"]
        for row in cur.fetchall():
            table.add_row([row[0], row[1], row[2], row[3]])
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_sales()
        elif stop == 'h':
            initial_screen()


    elif clfy == "menu":
        cur.execute("select mnName, sNum, sumprice from mnSales")
        table = PrettyTable()
        table.field_names = ["메뉴이름" , "판매량", "매출총합"]
        for row in cur.fetchall():
            table.add_row([row[0],row[1],row[2]])
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_sales()
        elif stop == 'h':
            initial_screen()
    elif clfy == "weather":
        cur.execute("select state, mnName, sNum, sumprice from wtSales")
        table = PrettyTable()
        table.field_names = ["날씨", "메뉴이름", "판매량", "매출총합"]
        for row in cur.fetchall():
            table.add_row([row[0], row[1], row[2], row[3]])
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_sales()
        elif stop == 'h':
            initial_screen()



    elif clfy == "dust":
        cur.execute("select dust, mnName, sNum, sumprice from dtSales")
        table = PrettyTable()
        table.field_names = ["미세먼지 농도", "메뉴이름", "판매량", "매출총합"]
        for row in cur.fetchall():
            table.add_row([row[0], row[1], row[2], row[3]])
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_sales()
        elif stop == 'h':
            initial_screen()
def instruct_storage():

    select= int(input("사용할 기능을 숫자로 입력해주세요\n1.재고 조회\n2.재료 발주\n"))
    if select ==1 :
        cur.execute("select mtName,mtQuantity from materials")
        table = PrettyTable()
        table.field_names = ["재료이름", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0], row[1]])
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_storage()
        elif stop == 'h':
            initial_screen()
    if select ==2:
        mtName = input("추가할 재료를 입력하세요")
        print("\n")
        cur.execute("select mtName,mtQuantity from materials where mtName= "+"'"+str(mtName)+"' ;")

        table = PrettyTable()
        table.field_names = ["재료이름", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0], row[1]])
        print(table)
        mtNUM=input("추가할 수량을 써주세요")
        cur.execute("UPDATE materials SET mtQuantity = mtQuantity+"+str(mtNUM)+" WHERE mtName='"+str(mtName)+"' ;")
        cur.execute("select mtName,mtQuantity from materials")
        table = PrettyTable()
        table.field_names = ["재료이름", " 수량 "]
        for row in cur.fetchall():
            table.add_row([row[0], row[1]])
        print("추가후 재고수량")
        print(table)
        stop = input("계속하시려면 y 버튼을 눌러주세요. 홈으로가려면 h를 눌러주세요")
        if stop == 'y':
            instruct_storage()
        elif stop == 'h':
            initial_screen()
def instruct_exit():
    db.commit()
    print("종료")



if __name__ == "__main__":
    print("이게 메인일 때 출력")
