import oracledb

from src.oracleutil.connection import USER, PASSWORD, DSN, PORT


def create_table(cursor):
    try:
        sql = 'create table dept_ex as select * from dept'
        cursor.execute(sql)
        # DDL의 실행 결과는 for-in 구문에서 반복할 결과가 없음.
        print('테이블 dept_ex 생성 성공')
    except Exception as e:
        print(e)


def drop_table(cursor):
    try:
        sql = 'drop table dept_ex'
        cursor.execute(sql)
        print('테이블 dept_ex 삭제 성공')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    with oracledb.connect(user=USER, password=PASSWORD, dsn=DSN, port=PORT) as conn:
        with conn.cursor() as cursor:
            # dept_ex 테이블 생성
            # create_table(cursor)

            # dept_ex 테이블 삭제
            drop_table(cursor)
