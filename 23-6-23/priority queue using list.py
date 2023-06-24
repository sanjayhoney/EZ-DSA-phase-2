#priority queue
'''jobs will be in a queue however priorities will be assigned
.as per the priority jobs will be alloted
task
1    2
2    4
3    3
4    1   '''
studg=[]
studg.append((1,"sha1"))
studg.append((4,"sha4"))
studg.sort(reverse=True)
print("yes")
print(studg)
studg.append((3,"sha3"))
studg.append((2,"sha2"))
studg.sort(reverse=True)
print("priority wise sorted")
print(studg)
print("original queue")
while studg:
    print(studg.pop())
