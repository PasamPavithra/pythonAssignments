lst = {1: [100, "AAA", 18000],
2: [101, "BBB", 50000],
3: [102, "CCC", 21000]}
print ("{:<5} {:<5} {:<5} {:<5}".format('Sno','id','Name','Salary'))
for k, i in lst.items():
    id, name, salary = i
    print ("{:<5} {:<5} {:<5} {:<5}".format(k, id, name, salary))
