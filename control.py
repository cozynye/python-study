# 기본 if문 구조 ->바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기를 해주어야 한다(다른 언어와의 차이점)
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     ...
# else:
#     수행할 문장A
#     수행할 문장B
#     ...

a=int(input())
if a==1 :
    print('일입니다')
# print('이건 안될걸')
else :
    print('1이 아니다')

# elif : 다양한 조건을 판단하는 함수이며, 조건, 개수 제한 없이 사용할수 있다.
# pass : if문에 아무런 결과 값도 실행하지 않게하는 역할을 한다.

a = int(input())
if a ==1:
    print("일 입니다.")
elif a==3:
        print("삼 입니다.")
elif a==4:
        print("사 입니다.")
else:
        print("값이 없습니다.")

if a==1:
        pass
else:
        print("값이 없습니다.")


# while : 해당 조건이 참인 경우 반복해서 수행
# while < 조건문 >:
#         < 수행할 문장1 >
#         < 수행할 문장2 >
#         < 수행할 문장3 >
a=int(input())
while a<10 :
    a=a+1
    print(a)
    if(a==10) :
        print('종료')


b=10
while b<30 :

        b = b + 1
        if b%2==0 : continue
        print(b)
        if(b==25) : break


# for 변수 in 리스트(튜플, 문자열):
#     < 실행할 문장1 >
#     < 실행할 문장2 >

list=['apple', 'banana', 'candy', 'dog']
for i in list:
    print(i)

a = [90, 25, 67, 45, 80]
n = 0
for i in a:
    n = n + 1
    if i<60: continue
    print("%d번 수험생 합격입니다." % n)#포매팅 %d가 변수 n의 값으로 치환되어 출력


num=int(input())
gugu=[num*b for b in range(1,10)] #1부터 9까지
print(gugu)