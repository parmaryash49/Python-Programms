from student import student
# create instane of student
s=student()
s.setid(12)
s.setname('kamesh')
s.setaddress("shahpur")
s.setmarks(25)

print(f"student id is {s.getid()}")
print(f"student name is {s.getname()}")
print(f"student address is{s.getaddress()}")
print(f"student marks is{s.getmarks()}")