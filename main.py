i = 10
while i < 100:
  a= str(i)
  left = int(a[1:])
  if i/7 == left:
    print(i)
  i = i + 1