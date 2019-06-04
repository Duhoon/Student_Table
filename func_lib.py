import pymysql
import time

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='engns0403@', db='test_project')
cur = db.cursor()
now = time.strftime('%Y%m%d%H%M%S', time.localtime())

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
        menu = input("\t메뉴 : ")
        cur.execute("select price from menu where mID = " + menu + ";")
        items = cur.fetchall()
        num = int(input("\t개수 : " ))
        pay = pay + (items[0][0] * num)
        payment = input("\t결제수단(money, card) : ")
        cur. execute("insert into sales value (" + str(menu) + ", " + str(num) + ", \'" +str(payment) + "\', " + str(now) + ")")
        stop = input("계속하시겠습니까?(y or n) : ")
    print("\t결제금액 :", pay)
    print("\t계산 완료되었습니다.")

def instruct_sales():
    cur.execute("select mName, num, payment, saleDate from sales, menu where sales.mID = menu.mID")
    print("------------------------------------------------------")
    print("\t메뉴이름\t개수\t\t지불수단\t\t날짜시간")
    for row in cur.fetchall():
        print("\t" , row[0] , "\t\t" , row[1] , "\t\t" , row[2] , "\t" , row[3])
    print("------------------------------------------------------")

if __name__ == "__main__":
    print("이게 메인일 때 출력")
