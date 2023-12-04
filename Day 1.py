###Part 1
h = open("a.txt")
l = [i.strip()for i in h.readlines()]
#print(l)
sum = 0
for i in l:
  num = ''
  for n in i:
    if n in '1234567890':
      num += n
  sum += int(num[0]+num[-1])
print(sum)

###Part 2
ll = ['zero','one','two','three','four','five','six','seven','eight','nine']
numbers = []
for i in l:
  i = list(i)
  newnum = []
  for n in range(len(i)):
    if i[n] in '1234567890':
      newnum.append(i[n])
    elif ''.join(i[n:n+3]) in ll: 
      newnum.append(ll.index(''.join(i[n:n+3])))
    elif ''.join(i[n:n+4]) in ll:
       newnum.append(ll.index(''.join(i[n:n+4])))
    elif ''.join(i[n:n+5]) in ll:
       newnum.append(ll.index(''.join(i[n:n+5])))
  numbers.append(newnum)
#print(sum([eval(f'{numba[i][0]}+{numba[i][-1]}')for i in range(len(numba))]))
sum = 0
for i in numbers:
  z = ''
  z += str(i[0])
  z+= str(i[-1])
  sum += int(z)
print(sum)
  

      
  
