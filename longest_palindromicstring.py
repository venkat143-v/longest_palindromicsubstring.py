n=input()
m=''
for i in range(len(n)):
  for j in range(i):
    b=n[j:i]
    if b==b[::-1]:
      if len(m)<len(b):
        m=b
print(m)
