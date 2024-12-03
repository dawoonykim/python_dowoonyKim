print('*** 자리배치도 ***')
customer = int(input('고객수 입력: '))
column = int(input('좌석행 수 입력: '))

if customer % column == 0:
    row = customer // column
else:
    row = (customer // column) + 1

for i in range(0, column):
  for j in range(1, row+1):
    seat = i * row + j
    if seat > customer:
      break
    print(seat, end=" ")
  print()