# import array
from array import *
marks=array('i',[12,34,56,45,78,45,90,3])
for i in marks:
    print(i)
# print(marks[-1:-4:-1])
marks.append(45)
print(marks.count(45))
print(marks.tofile("yash.txt"))

print(marks)


