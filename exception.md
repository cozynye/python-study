예외 처리
=====

##1. 기본 형태
````
try :
    ...
except [오류 사항 [as 오류 메시지 변수]] :
    ...
finally:
    ...
````
* try 구문 안에 오류 발생 가능성이 있는 코드를 사용<br/>
만약 try 구문 안에 들어 있는 코드에서 예외가 발생하면 그 즉시 except 구문으로 코드 흐름이 점프
* except 구문에는 예외가 발생했을 때 예외 처리를 할 수 있는 코드가 있다
* finally 구문은 try 구문 수행 도중 예외 발생 여부와 상관없이 항상 실행(리소스 해제를 위해 많이 사용)<br/>
리소스 해제가 필요 없는 경우에는 finally 구문을 생략할 수 있다
  
## 2. 예제
````
try :
    a = [1, 2]
    print(a[3])
    4 / 0
except Exception as e:
    print(e)
finally: print('무조건 실행')

>>list index out of range
무조건 실행

* 파이썬에서는 10을 0으로 나눌 수 없기 때문에 예외를 발생
변수 e를 통해 오류 내용을 확인 할 수 있다
````
## 3. 여러 개의 예외 처리
````
try :
    a=10
    b='zero'
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
    
>> unsupported operand type(s) for /: 'int' and 'str'
정수형(int) 10을 문자열 'zero'로 나눌 수 없기 때문에 TypeError 예외가 발

* 0으로 바꿔 실행하면 
division by zero 
````


## 4. 리소스를 사용할 때 예외 처리를 하는 방법

````
pickle - 파이썬 객체를 파일로 저장하고 메모리로 읽어올 수 있도록 모와주는 모듈

import pickle

f=open('setting.txt', 'wb')     # open() 함수를 이용해 setting.txt. 파일을 바이너리 쓰기(wb) 모드로 파일을 읽을 수 있는 파일 객체를 반환
                                # 기존 setting.txt 파일이 있다면 기존 내용을 덮어씀
try :
    setting=[{'title' : 'python program'}, {'author': 'kei'}]
    pickle.dump(setting, f)     #dump() 함수를 이용해 리스트 객체 setting의 내용을 파일 객체 f에 저장
except Exception as e:
    print(e)
finally:
    f.close()
````

## 5. 예외 만들기
- 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해 예외를 만들어서 사용
- 파이썬 내장 클래스인 Exception 클래스를 상하여 만들 수 있다

````
class MyError(Exception):
    pass

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

say_nick('테스트트')

>>테스트트


say_nick('바보')

Traceback (most recent call last):
  File "/Users/cozy/Python/Python/test", line 10, in <module>
    say_nick('바보')
  File "/Users/cozy/Python/Python/test", line 6, in say_nick
    raise MyError()
__main__.MyError
````

````
class MyError(Exception):
    pass

def say_nick(nick):
    if nick=='바보':
        raise MyError()
    print(nick)

try:
    say_nick('테스트')
    say_nick('바보')
except MyError :
    print('허용되지 않은 별명')
    
>>테스트
허용되지 않은 별명
````