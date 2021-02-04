파이썬 엑셀 파일 읽고 쓰기
========================

## 1. 엑셀 파일 읽기

- 엑셀 파일 읽기
````
import openpyxl

#data_only=Ture로 해줘야 수식이 아닌 값으로 받아온다.
load_wb=openpyxl.load_workbook("C:\Users\nye\PycharmProjects\chatbot\test.xlsx", data_only=True)

#시트이름 불러오기
load_ws=load_wb['2020']

#셀 주소로 값 출력
print(load_ws['F4'].value)

#셀 좌표로 값 출력
print(load_ws.cell(6,4).value)
````

- 지정한 셀 값 출력
````
print('\n-----지정한 셀 출력-----')
get_cells = load_ws['A1':'D2']
for row in get_cells:
        for cell in row:
            print(cell.value)
````

- 모든 행 단위로 출력
````
print('\n-----모든 행 단위로 출력-----')
for row in load_ws.rows:
    print(row)
````
![img.png](img.png)

- 모든 열 단위로 출력
````
print('\n-----모든 열 단위로 출력-----')
for column in load_ws.columns:
    print(column)
````

![img_1.png](img_1.png)

- 모든 행과 열 출력

print('\n-----모든 행과 열 출력-----')
all_values = []
for row in load_ws.rows:
    row_value = []
    for cell in row:
        row_value.append(cell.value)
    all_values.append(row_value)
print(all_values)


## 2. 엑셀 파일 쓰기