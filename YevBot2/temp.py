from json import dumps,loads
dic = {}
dic["cmd"] = "print me"
dic["123"] = 14
fred = dumps(dic)
#open("dic test",'w')
#open.write(fred)
print fred
