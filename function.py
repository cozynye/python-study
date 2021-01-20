# 파이썬 함수의 구조
# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...

def gugu(a):        #a는 매개변수 : 함수에 입력으로 전달된 값을 받는 변수
    if(a>1 and a<10) : t=[a*b for b in range(1,10)]
    else : t='범위를 넘어 섰습니다'
    return t
print(gugu(2))      #2는 인수 : 함수를 호출할 때 전달하는 입력값

# 여러개의 입력값을 받는 함수
# def 함수이름(*매개변수):
#     <수행할 문장>
#     ...

def many_add(*num):
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

# 키워드 파라미터 kwargs :**kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는
# 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장
# def print_kwargs(**kwargs):
#     print(kwargs)

#튜플로
def myFunc(**kwargs):
    for item in kwargs.items():
        print(item)

myFunc(x=100, y=200, z='b')

#리스트로
def test_kwargs(**kwargs):
    print(kwargs)

test_kwargs(a=10,b=20)


#함수의 결과값은 1개이다
def add_and_mul(a,b):
     return a+b, a*b

print(add_and_mul(3,5))     # 튜플로 결과 값을 갖게됨

result1,result2=add_and_mul(3,5)
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

#초기화시키고 싶은 매개변수를 항상 뒤쪽에 놓는 것을 잊지 말자.
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
print('return',a)

# 2. global 사용하기
a = 2
def vartest():
    global a
    a = a+1

vartest()
print('global',a)

#lambda
add=lambda a,b:a+b
print(add(3,5))