with open('info.txt','r',encoding='utf-8') as f,\
    open('young_people.txt','w',encoding='utf-8') as f1:
    for i in f:
        a = i.strip()
        name,age = a.split(',')
        if 18<=int(age):
            f1.write(i)