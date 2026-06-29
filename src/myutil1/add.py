def plus(x, y):
    return x + y


# __name__: 모든 파이썬 모듈(py 파일)이 가지고 있는 특별한 이름의 변수.
# (1) 현재 파일을 실행(Ctrl+Shift+F10)할 때는 '__main__' 문자열이 할당됨.
# (2) 다른 파일에서 import될 때는 파일 (경로) 이름이 할당됨.
# (목적) 단독(메인)으로 실행되는 코드인 지, import되서 실행되는 코드인 지를 구분하기 위해서.
print(__name__)

if __name__ == '__main__':  # 현재 파일을 메인으로 실행하는 경우에
    result = plus(1, 2)
    print(result)
