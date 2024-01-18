# 사전에다가 키워드 및 정보 저장 하는 법.

job = dict(Newton= 1642,Hubble=1879,King=1998)
print("add new catalog : new , search : no ")
d=input()

if d == 'no' :
    print(job.keys())
    print("Please insert same with Keyword")
    d=input()
    if d in job.keys() :
        c=job['{0}'.format(d)]
        print(c)

    
    else:
        print("We can't find it!")
else :
    print("Please insert name")
    name=input()
    print("Please inser years")
    years = input()
    job['{0}'.format(name)] = years
    
    print(job.keys())
    print(job.items())


