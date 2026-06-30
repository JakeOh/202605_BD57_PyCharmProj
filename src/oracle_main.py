import oracledb

import src.oracleutil as oracle


def input_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print('정수로만 입력가능합니다.')

    return number


def delete_dept_ex(cursor):
    dept_no = input_integer('삭제할 부서 번호>> ')
    oracle.delete_dept(cursor, dept_no)


def update_dept_ex(cursor):
    dept_no = input_integer('업데이트할 부서 번호>> ')
    dept_name = input('업데이트할 부서 이름>> ')
    dept_loc = input('업데이트할 부서 위치>> ')
    oracle.update_dept(cursor, dept_no, dept_name, dept_loc)


def insert_dept_ex(cursor):
    dept_no = input_integer('추가할 부서 번호>> ')
    dept_name = input('추가할 부서 이름>> ')
    dept_loc = input('추가할 부서 위치>> ')
    oracle.insert_dept(cursor, dept_no, dept_name, dept_loc)


def select_by_dept_name(cursor):
    dept_name = input('부서 이름 입력>> ')
    oracle.select_by_dept_name(cursor, dept_name)


def select_by_dept_no(cursor):
    dept_no = input_integer('부서 번호 입력>> ')
    oracle.select_by_dept_no(cursor, dept_no)


def show_main_menu():
    print('\n' + '-' * 80)
    print('[0]종료 [1]테이블 생성 [2]테이블 삭제 [3]전체검색 [4]번호로 검색 [5]이름으로 검색 [6]부서 추가 [7]업데이트 [8]삭제')
    print('-' * 80)
    menu = input_integer('메뉴 선택>> ')

    return menu


def main():
    # Oracle에 접속
    with oracledb.connect(user=oracle.user, password=oracle.password, dsn=oracle.dsn, port=oracle.port) as conn:
        # Cursor를 생성
        with conn.cursor() as cursor:
            run = True
            while run:
                menu = show_main_menu()
                if menu == 0:
                    run = False  # 무한 반복문을 종료하기 위해서
                elif menu == 1:
                    oracle.create_table(cursor)
                elif menu == 2:
                    oracle.drop_table(cursor)
                elif menu == 3:
                    oracle.select_all(cursor)
                elif menu == 4:
                    select_by_dept_no(cursor)
                elif menu == 5:
                    select_by_dept_name(cursor)
                elif menu == 6:
                    insert_dept_ex(cursor)
                    conn.commit()  # insert된 내용을 영구 저장.
                elif menu == 7:
                    update_dept_ex(cursor)
                    conn.commit()
                elif menu == 8:
                    delete_dept_ex(cursor)
                    conn.commit()
                else:
                    print('메뉴 번호를 확인하세요.')

    print('>>>>> 프로그램 종료 >>>>>')


if __name__ == '__main__':
    main()
