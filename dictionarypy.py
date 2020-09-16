food={"yash":"bataka vada","kamesh":"bhajipav","milan":{"a":"dudh","b":"bapore","c":"rat"}}
print(food["yash"])
# food["roshni"]={"pakodi","mamva"}
d2=food.copy()
del food["milan"]
print(food)
print(d2)
d2.items()
print(d2.values())
d2.update({"yash":"kabab"})
print(d2)