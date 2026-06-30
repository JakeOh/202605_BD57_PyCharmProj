import oracledb


if __name__ == '__main__':
    user = 'scott'
    pw = 'tiger'
    dsn = 'localhost/xe'
    port = 1521

    with oracledb.connect(user=user, password=pw, dsn=dsn, port=port) as conn:
        with conn.cursor() as cursor:
            # 부서번호가 일치하는 레코드를 검색.
            sql = 'select * from dept where deptno = :dept_no'  # SQL 템플릿
            try:
                dept_no = int(input('부서번호 입력>>> '))
                # print('dept_no =', dept_no)

                # sql 템플릿에서 :dept_no 자리에 입력받은 dept_no를 삽입하고 SQL 문장을 실행.
                # 템플릿의 빈자리를 채우는 방법 (1): keyword argument를 사용.
                # cursor.execute(sql, dept_no=dept_no)
                # 템플릿의 빈자리를 채우는 방법 (2): dict를 사용.
                cursor.execute(sql, {'dept_no': dept_no})
                for row in cursor:
                    print(row)
            except Exception as e:
                print(e)
