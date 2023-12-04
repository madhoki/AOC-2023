import math
h = open('a.txt')
l = [i.strip()for i in h.readlines()]
badl = []
for i in range(len(l)):
  li = l[i]
  for m in range(15,21):
    for colour in ['blue','red','green']:
      if f'{m} {colour}' in li or '13 red' in li or '14 red' in li or '14 green' in li:
        badl.append(i+1)
print(sum([i for i in range(1,len(l)+1)])-sum(set(badl)))

prodlist = []
for i in range(len(l)):
  li = l[i].split()
  maxir = []
  maxig = []
  maxib = []
  for x in range(len(li)):
    if 'red' in li[x]:
      maxir.append(int(li[x-1]))
    if 'blue' in li[x]:
      maxib.append(int(li[x-1]))
    if 'green' in li[x]:
      maxig.append(int(li[x-1]))
  prodlist.append(math.prod([max(maxir),max(maxig),max(maxib)]))
print(sum(prodlist))
