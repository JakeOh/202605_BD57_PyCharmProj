import oracledb


if __name__ == '__main__':
    user = 'scott'
    password = 'tiger'
    dsn = 'localhost/xe'
    port = 1521

    # with-as 구문을 사용해서 close() 메서드가 자동으로 호출되도록.
    # Connection 객체 생성
    with oracledb.connect(user=user, password=password, dsn=dsn, port=port) as conn:
        # Cursor 객체 생성
        with conn.cursor() as cursor:
            sql = 'select * from dept'
            cursor.execute(sql)  # SQL 문장 실행
            for row in cursor:  # Cursor가 실행한 결과 처리
                print(row)