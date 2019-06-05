import pymysql
import time
import random

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
    print("\t\t 메뉴 \t\t 계산 \t\t 매출 \t\t 고객 ")
    print("--------------------------------------------------------")

def instruct_input():
    instruction = input(">> ")
    return instruction


def instruct_help():
    print("\n프롬프트에 다음 설명하는 것을 입력하세요.")
    print("메뉴       현재 매장에서 판매하는 메뉴 확인")
    print("계산       계산 시스템 활성화")
    print("매출       데이터베이스에 있는 매출을 출력")
    print("고객       매장에 등록되어 있는 고객 정보 확인")
    print("종료       프로그램 종료")

def instruct_allmenu():
    cur.execute("select * from menu")
    print("-----------------------------")
    print("\tmID\t메뉴이름\t\t가격")
    for row in cur.fetchall():
        print("\t", row[0], "\t", row[1], "\t", row[2])
    print("-----------------------------")

def instruct_casher():
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
    tablenum = input("\t테이블을 선택하세요(1~5번)")

    while stop != 'n':


        menu = input("\t메뉴 : ")
        cur.execute("select price from menu where mnID = " + "\""+menu + "\"" + ";")

        items = cur.fetchall()
        Mnum = int(input("\t개수 : " ))

        pay = pay + (items[0][0] * Mnum)
        cur.execute("insert into sales values (" + str(num) + ", " + str(
            tablenum) + ", \'" + str(menu) + "\', " + str(Mnum) + ", " + str(now) + ", \'" + str('n') + "\')")
        stop = input("메뉴를 추가 하시겠습니까?(y or n) : ")
    print("\t결제금액 :", pay)
    print("\t계산 완료되었습니다.")
def instruct_table():
    stop = 'n'
    print("-----------------------------")
    print("\t\t\t\t1번테이블 \n")
    pay1=0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=1 and complete = 'n' and menu.mnId=sales.mnId;"):
        print("\t메뉴이름\t\t수량")

        for row in cur.fetchall():
            print("\t", row[0], "\t", row[1])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay1=pay1+(item[0][0]*row[1])
        print("총액:",pay1)
    else:
        print("빈테이블")
    print("-----------------------------")

    print("\t\t\t\t2번테이블 \n")
    pay2=0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=2 and complete = 'n' and menu.mnId=sales.mnId;"):
        print("\t메뉴이름\t\t수량")

        for row in cur.fetchall():
            print("\t", row[0], "\t", row[1])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay2=pay2+(item[0][0]*row[1])
        print("총액:",pay2)
    else:
        print("빈테이블")
    print("-----------------------------")
    print("\t\t\t\t3번테이블 \n")
    pay3=0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=3 and complete = 'n' and menu.mnId=sales.mnId;"):
        print("\t메뉴이름\t\t수량")

        for row in cur.fetchall():
            print("\t", row[0], "\t", row[1])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay3=pay3+(item[0][0]*row[1])
        print("총액:",pay3)
    else:
        print("빈테이블")
    print("-----------------------------")
    print("\t\t\t\t4번테이블 \n")
    pay4 = 0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=4 and complete = 'n' and menu.mnId=sales.mnId;"):
        print("\t메뉴이름\t\t수량")

        for row in cur.fetchall():
            print("\t", row[0], "\t", row[1])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay4 = pay4 + (item[0][0] * row[1])
        print("총액:", pay4)
    else:
        print("빈테이블")
    print("-----------------------------")
    print("\t\t\t\t5번테이블 \n")
    pay5 = 0
    if cur.execute("select mnName,sNum  from sales,menu where tableNum=5 and complete = 'n' and menu.mnId=sales.mnId;"):
        print("\t메뉴이름\t\t수량")

        for row in cur.fetchall():
            print("\t", row[0], "\t", row[1])
            cur.execute("select price from menu where mnName= \'" + str(row[0]) + "\';")
            item = cur.fetchall()
            pay5 = pay5 + (item[0][0] * row[1])
        print("총액:", pay5)
    else:
        print("빈테이블")

    stop = input("계산하시겠습니까?y/n(메뉴 돌아가기는 h)")
    if stop == 'y':
        print("계산완료")
        cur.execute("UPDATE sales SET complete='y' WHERE complete='n'")
    if stop =='n':
        instruct_table()
    if stop =='h':
        initial_screen()


def instruct_sales():
    cur.execute("select sID, tableNum, mnName, sDate,complete from sales, menu where sales.mnID = menu.mnID")
    print("------------------------------------------------------")
    print("\t메뉴이름\t개수\t\t지불수단\t\t날짜시간")
    for row in cur.fetchall():
        print("\t", row[0], "\t\t", row[1], "\t\t", row[2], "\t", row[3], "\t",row[4])
    print("------------------------------------------------------")

if __name__ == "__main__":
    print("이게 메인일 때 출력")
