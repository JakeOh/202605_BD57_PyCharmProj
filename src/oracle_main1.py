import oracledb  # oracledb 모듈 가져오기


if __name__ == '__main__':
    print('oracledb 패키지 버전 =', oracledb.__version__)

    # Oracle 데이터베이스에 접속하기 위한 사용자 아이디
    user = 'scott'
    # Oracle에 접속하기 위한 비밀번호
    password = 'tiger'
    # Oracle 서버의 정보(호스트 이름 또는 IP/SID)
    dsn = 'localhost/xe'
    # Oracle 서버 포트 번호
    port = 1521

    # Oracle에 접속
    conn = oracledb.connect(user=user,
                            password=password,
                            dsn=dsn,
                            port=port)
    print('conn =', conn)

    # SQL 문장 실행, 결과 처리
    # 접속한 DB(오라클)에서 실행할 SQL 문장. (주의) 문장 끝에 세미콜론(;)을 사용하면 안됨!
    sql = 'select * from emp'

    # Cursor 객체(DB에 SQL 문장을 전송하고, 그 실행된 결과를 처리할 수 있는 객체) 생성.
    cursor = conn.cursor()
    print('cursor =', cursor)

    # Cursor 객체의 메서드를 사용해서 SQL 문장을 실행
    result = cursor.execute(sql)
    print('result =', result)  #> execute 메서드의 호출 결과는 Cursor 객체

    # Cursor 객체는 iterable --> for-in 반복문에서 사용.
    for row in result:
        print(row)  #> 테이블의 행에서 select된 컬럼 값들이 tuple로 만들어져 있음.

    # 사용했던 Cursor 객체를 닫음.
    cursor.close()
    print('Cursor 객체 해제 성공')

    # Oralce 접속 해제
    conn.close()
    print('Oracle 접속 해제 성공')
