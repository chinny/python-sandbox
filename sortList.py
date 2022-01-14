testfile =  """
'Jeff',1989,180
'Steph',1986,165
'Sage',2016,223
'Jada',2018,96
'Caia',2021,172
"""

list = testfile.splitlines()
list.pop(0)

newlist = []

for line in list:
    newlist.append(line.split(','))

newlist.sort(key=lambda x: int(x[2]))

for line in newlist:
    print(line)