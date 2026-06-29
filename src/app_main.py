# import 모듈
import src.myutil1.add  # src.myutil1.add 모듈(py 파일) 가져오기

# from 모듈 import (변수, 함수, 클래스) 이름
from src.myutil1.subtract import minus  # subtract 모듈에서 minus 함수 이름을 가져오기

# add 모듈(파일)에서 작성한 plus 함수를 호출.
result = src.myutil1.add.plus(10, 20)
print('plus 결과 =', result)

# 임포트한 minus 함수를 호출.
result = minus(10, 20)
print('minus 결과 =', result)
