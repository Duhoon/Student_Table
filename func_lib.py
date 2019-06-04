import pymysql
import time
import random

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='engns0403@', db='test_project')
cur = db.cursor()
now2 = time.strftime('%Y%m%d%H%M%S', time.localtime())
now = time.strftime('%Y%m%d', time.localtime())

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
    pay = 0
    while stop != 'n':

        tablenum = input("\t테이블을 선택하세요(1~5번)")

        menu = input("\t메뉴 : ")
        cur.execute("select price from menu where mnID = " + "\""+menu + "\"" + ";")

        items = cur.fetchall()
        Mnum = int(input("\t개수 : " ))
        pay = pay + (items[0][0] * Mnum)
        payment = input("\t결제수단(money, card) : ")

        stop = input("계속하시겠습니까?(y or n) : ")

        cur.execute("select sId from sales;") #sid 조회
        num = random.randrange(0, 100)
        sID = cur.fetchall()
        print(sID);
        while num in sID:  # 중복될 경우
                num = random.randrange(0, 100)  # 다시 난수 생성
            #여기다가 주문추가
        sID = num

        cur.execute("insert into sales values (" + str(num) + ", " + str(
        tablenum) + ", \'" + str(menu)+ "\', " + str(pay) + ", " + str(Mnum) + ", " + str(now)+")")

    print("\t결제금액 :", pay)
    print("\t계산 완료되었습니다.")

def instruct_sales():
    cur.execute("select sID, tableNum, mnName, sDate from sales, menu where sales.mnID = menu.mnID")
    print("------------------------------------------------------")
    print("\t메뉴이름\t개수\t\t지불수단\t\t날짜시간")
    for row in cur.fetchall():
        print("\t" , row[0] , "\t\t" , row[1] , "\t\t" , row[2] , "\t" , row[3])
    print("------------------------------------------------------")

if __name__ == "__main__":
    print("이게 메인일 때 출력")
