# 파이썬의 자료형에는 크게 나누면 '수치형(numbers)', '논리형(bool)', '순서형(sequence)', '매핑형(mapping)',이 있다.

# 수치형 - 정수(int), 더 큰 정수(long int), 소수(float), 복소수(complex)
number_int=123
print(type(number_int),number_int)

number_float=1.4
print(type(number_float),number_float)

number_complex=3+3j
print(type(number_complex),number_complex)

# 논리형
boolean_one=3<4
print(type(boolean_one),boolean_one)

boolean_two=11<10
print(type(boolean_two),boolean_two)

# 순서형 - 문자열(string), 리스트(list), 튜플(tuple) -> 사용자 정의 클래스
string='test'
print(type(string), string)

# 리스트는 [ ] 사용하지만, 튜플은 () 사용한다.
# 리스트는 변경이 가능하지만 문자열, 튜플은 요소 값 변경(수정, 삭제)이 안 된다.
# 튜플은 요소 뒤에 ,을 사용해야 하며 괄호를 생략해도 된다.
# 기타 사항

list=[10,'list',30,'bye']
print(type(list),list)

#리스트 요소 추가, 삽입, 삭제
list.append(8)
print(list)
list.insert(-1, 'last')
print(list)

delist=[10,20,30,40,50]
delist.pop()
print(delist)
c=delist.pop(2)
print(c)



tuple=(1,)
print(type(tuple),tuple)
tuple='test',2
print(type(tuple),tuple)
tuple=(1,2,3,4)
print(type(tuple),tuple)

tuples=(1,2,3,4,5)
new_tuples=tuples+(6,7)
print(new_tuples)


# 매핑형 - 딕셔너리(dictionary), 클래스 인스턴스, C확장형 등
dict={'one' : 1, 'two' : 'second', 'three' : 3}
print(type(dict), dict)
