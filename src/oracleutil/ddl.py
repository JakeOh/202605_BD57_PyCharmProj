import oracledb

from src.oracleutil.connection import user, password, dsn, port


def create_table(cursor):
    try:
        sql = 'create table dept_ex as select * from dept'
        cursor.execute(sql)
        # DDL의 실행 결과는 for-in 구문에서 반복할 결과가 없음.
        print('테이블 dept_ex 생성 성공')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    with oracledb.connect(user=user, password=password, dsn=dsn, port=port) as conn:
        with conn.cursor() as cursor:
            create_table(cursor)
