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


def show_main_menu():
    print('\n' + '-' * 50)
    print('[0]종료 [1]테이블 생성 [2]테이블 삭제')
    print('-' * 50)
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
                    print('TODO: 테이블 생성')
                elif menu == 2:
                    print('TODO: 테이블 삭제')

    print('>>>>> 프로그램 종료 >>>>>')


if __name__ == '__main__':
    main()
