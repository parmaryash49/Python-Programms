from teacher import Teacher
#create instance
t=Teacher()
t.setid(10)
t.setname("yash")
t.setaddress('shahpur darwaja bahar')
t.setsalary(22222.50)

print('id=',t.getid())
print('name=',t.getname())
print('address=',t.getaddress())
print('salary=',t.getsalary())

