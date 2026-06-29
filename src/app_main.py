# import 모듈(패키지)
import src.myutil1.add  # src.myutil1.add 모듈(py 파일) 가져오기

# import 모듈 as 별명  --> 가져오는 이름이 너무 긴 경우, 간단히 사용하기 위해서.
import src.myutil1.add as add

# from 모듈(패키지) import (변수, 함수, 클래스, 서브모듈) 이름
from src.myutil1.subtract import minus  # subtract 모듈에서 minus 함수 이름을 가져오기
from src.myutil1 import subtract  # myutil1 모듈(패키지)에서 subtract (서브모듈) 이름을 가져오기.

# myutil2 모듈(패키지)을 가져오기
# import src.myutil2
import src.myutil2 as utils

# add 모듈(파일)에서 작성한 plus 함수를 호출.
result = src.myutil1.add.plus(10, 20)
print('plus 결과 =', result)

result = add.plus(1, 2)
print('plus =', result)

result = minus(10, 20)
print('minus 결과 =', result)

result = subtract.minus(1, 2)
print('minus =', result)

# myutil2.__init__.py 파일에서 import된 이름들을 바로 사용 가능.
# result = src.myutil2.multiply(2, 3)
result = utils.multiply(2, 3)
print('multiply =', result)

print('divide =', utils.divide(2, 3))
