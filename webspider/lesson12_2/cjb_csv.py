import csv
# 设置表头
head = ['name','score','班级']
# 设置数据
#values = [('张三',98,'数据1班'),('李四',92,'数据2班'),('王五',56,'数据3班')]
values = [
        {'name':'zhang','score':95,'班级':'数据1班'},
        {'name':'zhang1','score':65,'班级':'数据2班'},
        {'name':'zhang2','score':15,'班级':'数据3班'},
]
# 保存成csv文件
# 换行符的设置 newline = '' 以空作为换行的符号
with open('成绩表.csv','w',newline = '\n',encoding = 'utf-8') as f:
    # write = csv.writer(f)
    # 字典数据转有写入函数（f,写明表头，分隔符）
    # 表头设置过程中要和字典的键是对应的
    write= csv.DictWriter(f,head,delimiter=';')
    # 先写表头
    write.writeheader()
    write.writerows(values)