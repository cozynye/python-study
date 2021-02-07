모듈
==========

## 1. 모듈 : 여러가지 함수나 클래스 등을 기능이나 목적별로 모아놓은 파일
- 모듈화된 기능은 재사용하기 쉽기 때문에 중복 코드 문제도 해결
- 모듈의 이름을 보고 해당 모듈의 기능을 유추할 수 있어야 좋은 모듈


## 예제

```
calc.py

def add(a,b) :  return a+b
def sub(a,b) : return a-b
def mul(a,b) : return a*b
def div(a,b) : return a/b
```


````
* 다른 경로에 있다면 import 할 때 경로를 지정 해줘야 한다(파일명 뒤 .py 붙이면 안된다)

>>> import calc
>>> calc.add(4,3)
7
>>> calc.sub(10,5)
5
````
<br/>




## 2. 모듈에서 불러올 함수를 직접 지정하는 방법(모듈 이름을 붙이지 않는다)
- 사용할 모듈 함수만 불러 오기 때문에 메모리나 불러오는 속도 면에서 장점이 있다
````
from 모듈명 import 함수명, 함수명, ...
````
* 모듈에서 모든 함수를 불러오는 방법
````
from 모듈명 import *
````


## 3. if __name__ == "__main__":
````
calc.py

def add(a,b) : return a+b
def sub(a,b) : return a-b
def mul(a,b) : return a*b
def div(a,b) : return a/b
print(add(5,8))
print(div(100,2))


>>> import calc
13
50.0


--> 모듈의 함수만 사용하려 하는데 결과값이 출력이 된다

````
````
def add(a,b) : return a+b
def sub(a,b) : return a-b
def mul(a,b) : return a*b
def div(a,b) : return a/b

if __name__== "__main__":
        print(add(5,8))
        print(div(100,2))
        
>>> import calc
>>>


if __name__ == "__main__"을 사용하면 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어 
if문 다음 문장이 수행된다. 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 
__name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.         
````

### `__name__` 변수란?

파이썬의 `__name__` 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 위처럼 직접 calc.py 파일을 실행할 경우 
calc.py의 `__name__` 변수에는 `__main__` 값이 저장된다. 하지만 파이썬 셸이나 다른 파이썬 모듈에서 calc를 import 
할 경우에는 calc.py의 `__name__` 변수에는 calc.py의 모듈 이름 값 calc가 저장된다.
````
calc.py

def add(a,b) : return a+b
def sub(a,b) : return a-b
def mul(a,b) : return a*b
def div(a,b) : return a/b

if __name__== "__main__":
        print(add(5,8))
        print(div(100,2))
        print(__name__)

print(__name__)

-----------------------------------------
(base) cozy@Cozy python % python calc.py
13
50.0
__main__
__main__
-----------------------------------------
>>> import calc
calc
-----------------------------------------
````


## 4. 모듈을 불러오는 또 다른 방법
###1. sys.path.append(모듈을 저장한 디렉터리) 사용하기
sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다. <br>
만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다. 
sys.path.append("/Users/cozy/python/python")


````
현재 위치는 python > mode
>>> import calc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'calc'
>>> import sys
>>> sys.path.append("/Users/cozy/python/python")
>>> import calc
calc
````

###2. PYTHONPATH 환경 변수 사용하기
````
C:\doit>set PYTHONPATH=C:\doit\mymod
C:\doit>python
>>> import mod2
>>> print(mod2.add(3,4))
7
````


