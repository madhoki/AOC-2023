h  =  open('a.txt')  
import re
from collections import *
ll  =  [i.strip()for  i  in  h.readlines()]
l=['.'*len(ll[0])]
for  i  in  ll:
    l.append(f'.{i}..')
l.append('.'*len(ll[0]))
S=Counter()
def  check_for_nums(line0,line1,line2):
    global S
    nums  =  []
    iblong  =  0;ialong  =  0
    ibshort  =  0;iashort=0
    longi  =  [];shorti=[]
    longn=[];shortn=[]
    onenindexes  =  []

    for  i  in  range(100,1000):
        if  str(i)  in  line1:
            iblong  =  line1.index(str(i))
            ialong  =  iblong+2
            longi.append(iblong);longi.append(ialong);longi.append(ialong-1)
            longn.append(str(i))
    for  i  in  range(10,100):
        if  str(i)  in  line1:
            ibshort  =  line1.index(str(i))
            iashort  =  ibshort+1
            shorti.append(ibshort);shorti.append(iashort)
            shortn.append(str(i))

    for i in range(len(line1)):
        if line1[i].isdigit() and (i==0 or not line1[i-1].isdigit()) and (i==len(line1)-1 or not line1[i+1].isdigit()):
            onenindexes.append(i)

    newshort  =  []
    for  num  in  shortn:
        if  line1.index(num)  in  longi and 0:
            pass
        else:
            newshort.append(num)
    if  len(longn)  >  0:
        for  i  in  longn:
            for index in list([o.start() for o in re.finditer(str(i),line1)]):
                above  =  line0[index-1:index+4]
                below  =  line2[index-1:index+4]
                after  =  line1[index+3]
                before  =  line1[index-1]
                combstring  =  f'{above}{below}{after}{before}'
                gg=0
                for  char  in  combstring:
                    if char in "0123456789":
                        gg=1
                        break
                if gg:
                    continue
                for  char  in  combstring:
                    if  char  not  in  '.0123456789':
                        nums.append(i)
                        break
    if  len(shortn)  >  0:
        for  i  in  newshort:
            for index in list([o.start() for o in re.finditer(str(i),line1)]):
                above  =  line0[index-1:index+3]
                below  =  line2[index-1:index+3]
                after  =  line1[index+2]
                before  =  line1[index-1]
                combstring  =  f'{above}{below}{after}{before}'
                gg=0
                for  char  in  combstring:
                    if char in "0123456789":
                        gg=1
                        break
                if gg:
                    continue
                for char in combstring:
                    if  char  not  in  '.0123456789':
                        nums.append(i)
                        break
    #print(set(onenindexes))
    if  len(onenindexes)  >  0:
        for  index  in  set(onenindexes):
            above  =  line0[index-1:index+2]
            below  =  line2[index-1:index+2]
            after  =  line1[index+1]
            before  =  line1[index-1]
            combstring  =  f'{above}{below}{after}{before}'
            gg=0
            for  char  in  combstring:
                if char in "0123456789":
                    gg=1
                    break
            if gg:
                continue
            for  char  in  combstring:
                if  char  not  in  '.0123456789':
                    nums.append(line1[index])
                    break

    if  len(nums)  >  0:
        S+=(Counter(nums))
        return  sum([int(i)  for  i  in  (nums)])
    return  0
summ  =  0
for  i  in  range(1,len(l)-1):
    #print(i)
    summ  +=  check_for_nums(l[i-1],l[i],l[i+1])






print(summ)
