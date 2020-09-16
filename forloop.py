l=[["kamesh",1],["yash",3],["milan",5]]
# for i in range(len(l)):
#     print(l[i])
d={"yash":1,"kamesh":2}
for i,j in l:
    print(i,"and",j)
print(d)
for keys,value in d.items():
    print(keys,"and that",value)

stuff=["yash","milan",34,5,7,12,6]
for i in stuff:
    if str(i).isalpha() and str(i):
        print(i)