def select_all(cursor):
    """dept_ex 테이블의 모든 레코드를 검색해서 출력"""
    try:
        sql = 'select * from dept_ex'
        cursor.execute(sql)
        for row in cursor:
            print(row)
    except Exception as e:
        print(e)


def select_by_dept_no(cursor, dept_no):
    """dept_ex 테이블에서 부서번호가 dept_no인 레코드를 검색하고 출력."""
    try:
        sql = 'select * from dept_ex where deptno = :dept_no'  # 부서번호가 일치하는 부서 검색 SQL 템플릿
        cursor.execute(sql, dept_no=dept_no)
        for row in cursor:
            print(row)
    except Exception as e:
        print(e)


def select_by_dept_name(cursor, dept_name):
    """dept_ex 테이블에서 부서이름(dname) 컬럼의 값이 (대/소문자 구분없이) dept_name을 포함하는 레코드를 검색해서 출력."""
    try:
        sql = 'select * from dept_ex where lower(dname) like lower(:dept_name)'
        keyword = f'%{dept_name}%'
        cursor.execute(sql, dept_name=keyword)
        for row in cursor:
            print(row)
    except Exception as e:
        print(e)
