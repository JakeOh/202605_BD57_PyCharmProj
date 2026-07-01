def insert_dept(cursor, dept_no, dept_name, location):
    """dept_ex 테이블에 새로운 행(부서번호, 부서이름, 위치)을 추가."""
    try:
        sql = 'insert into dept_ex values (:dept_no, :dept_name, :location)'
        # cursor.execute(sql, dept_no=dept_no, dept_name=dept_name, location=location)
        cursor.execute(sql, {
            'dept_no': dept_no,
            'dept_name': dept_name,
            'location': location,
        })
        print(f'{cursor.rowcount}개 행 삽입됨.')
    except Exception as e:
        print(e)


def update_dept(cursor, dept_no, dept_name, location):
    """dept_ex 테이블에서 해당 부서번호(deptno)의 부서 이름(dname)과 위치(loc)를 업데이트."""
    try:
        sql = 'update dept_ex set dname = :dept_name, loc = :location where deptno = :dept_no'
        cursor.execute(sql, {
            'dept_no': dept_no,
            'dept_name': dept_name,
            'location': location,
        })
        print(f'{cursor.rowcount}개 행 업데이트됨.')
    except Exception as e:
        print(e)


def delete_dept(cursor, dept_no):
    """dept_ex 테이블에서 deptno가 일치하는 행을 삭제."""
    try:
        sql = 'delete from dept_ex where deptno = :dept_no'
        cursor.execute(sql, dept_no=dept_no)
        print(f'{cursor.rowcount}개 행 삭제됨.')
    except Exception as e:
        print(e)
