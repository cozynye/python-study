# 파이썬 함수의 구조
# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# 함수는 시스템에 내장되어 있는 내장 함수, 사용자가 만든 사용자 정의 함수, 라이브러리 형태로 모듈화시킨 외장 함

def gugu(a):        #a는 매개변수 : 함수에 입력으로 전달된 값을 받는 변수
    if(a>1 and a<10) : t=[a*b for b in range(1,10)]
    else : t='범위를 넘어 섰습니다'
    return t
print(gugu(2))      #2는 인수 : 함수를 호출할 때 전달하는 입력값

# 여러개의 입력값을 받는 함수
# def 함수이름(*매개변수):
#     <수행할 문장>
#     ...

def many_add(*num):     #매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 주
    sum=0
    for i in num :
        sum=sum+i
    return sum

print(many_add(1,2,3,))



def add_mul(choice, *num) :
    if choice=='add':
        result=0
        for i in num:
            result=result+i
    elif choice=='mul':
        result=1
        for i in num:
            result=result*i
    else: result='오류'
    return result
print(add_mul('add', 1,2,3,4,5,6,7,8,9,10,))
print(add_mul('mul', 1,2,3,4,5,6,7,8,9,10,))
print(add_mul('mul'))       #인수와 매개변수의 수가 일치하지 않아도 함수 실행
#print(add_mul())            #인수가 없으면 오류
print(add_mul('??'))


#함수의 결과값은 1개이다
def add_and_mul(a,b):
     return a+b, a*b

print(add_and_mul(3,5))     # 튜플로 결과 값을 갖게됨

result1,result2=add_and_mul(3,5)    #튜플로 된 값을 분리
print(result1)
print(result2)



#매개 변수에 초깃값 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself('홍길동',27)
say_myself('영심이',24,False)
say_myself('고길동',30, True)

#초기화시키고 싶은 매개변수를 항상 뒤쪽에 놓는 것을 잊지 말자. IndentationError: unexpected indent
# def say_myself(name, man=True, old):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
#
# say_myself('김길',27)


#함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a +1
    return a

a = vartest(a)
print('return1',a)
a = vartest(a)
print('return2',a)
a = vartest(a)
print('return3',a)

# 2. global 명령어 사용하기
a = 10
def vartest():
    global a    # 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻(좋은 방법은 아니다)
    a = a+1

vartest()
print('global1',a)
vartest()
print('global2',a)
vartest()
print('global3',a)

#lambda
add=lambda a,b:a+b
print(add(3,5))
print(add)
# 내장함수

# format()

# enumerate() - 순서가 있는 자료형(리스트,튜플 문자열) 입력하면 인덱스를 포함한 요솟값을 반환

num=(10,20,30,40,50)
for i in num :
    print(i)

print(enumerate(num))
for i in enumerate(num) :
    print(i)
for i,v in enumerate(num) :
    print('index:%d value:%d' %(i,v))

# str() - 입력으로 들어온 데이터를 문자열 객체로 반환

print(type(20))
print(type(str(20)))
a=[1,2,3]
print(str(a))   # 리스트 [1,2,3]을 -> '[1,2,3]' 으로 변환하여 반환

# join() - 리스트의 요소들을 지정한 구분자로 구분해 문자열로 반환(리스트 내 요소들을 문자열로 합칠 때 많이 사용)
# split() - 문자열을 특정 구분자를 기준으로 분리해 리스트로 반환

v=['cat', 'dog','monkey','tiger']
v1='/'.join(v)
print(v1)
print(type(v1))

v2=v1.split('/')
print(v2)
print(type(v2))

# id() - 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 반환

print(id('str'))

# find() - 특정 문자열을 찾기 위해 사용 / 그 문자열의 시작 위치를 반환하고 찾지 못하면 -1을 반환
str='hello'
print(str.find('l'))
print(str.find('a'))

# strip() - 주어진 문자열 양쪽 끝의 공백을 제거

str='  hello my name is gildong  '
print(str)
print(str.strip())


# filter() - 개별 요소를 반복적으로 셀 수 있는 객체(iterable object)를 입력받아 각 요소를 함수로 수행한 후 결과가 True인것만 묶어서 반환

def func(num) :
    list=[]
    for i in num:
        if(i%2==0) : list.append(i)
        else : pass
    return list
number=(1,2,3,4,5,6,7,8,9,10)
print(func(number))

def ev(num) :
    return num%2==0 #짝수면 true 반환


print(filter(ev,number))
print(list(filter(ev,number)))      #list() -> 인자로 들어온 데이터(객체)를 리스트로 반환

# lambda - 함수를 생성할 때 사용 - 익명 함수

def t2(num):
    return num*2
t=lambda x: x*2

print(t2(10))
print(t(10))

print(list(filter(lambda num :num%2==0, number)))

# map - 개별 요소를 반복적으로 셀 수 있는 객체를 입력받아 각 요소를 함수로 수행한 후 결과를 묶어서 반환

number=[1,2,3,4,5,6]
print(list(map(lambda x:x**3, number)))


