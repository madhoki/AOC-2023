h = open('a.txt')
l = [i.strip().split()[2:] for i in h.readlines()]
#Part 1
winlist = []
for i in range(len(l)):
  count = 0.5
  barrier = l[i].index('|')
  winners = sorted(l[i][0:barrier])
  numbers = sorted(l[i][barrier:])
  for x in numbers:
    if x in winners:
      count *= 2
  if count != 0.5:
    winlist.append(count)
  else:
    winlist.append(0)
  
print(sum(winlist))

#Part 2 - cardreturns function is small adaptation of part 1

def cardreturns(card):
  count = 0
  barrier = card.index('|')
  winners = sorted(card[0:barrier])
  numbers = sorted(card[barrier:])
  for x in numbers:
    if x in winners:
      count += 1
  return count
returns = []
for i in l:
  returns.append(cardreturns(i))


def compute_numcards(returns):
  numcards = [1 for i in returns]
  for i in range(len(returns)):
    multiplier = numcards[i]
    for n in range(i+1,i+returns[i]+1):
      numcards[n]+=multiplier
  return sum(numcards)

print(compute_numcards(returns))
