def test():
    res1 = yield "你好"
    yield f"我说：{res1}"

g = test()
print(next(g))
# print(next(g)) 此时yield挂起就不会赋值给res1
print(g.send("天气不错")) #使用send可以将值传入


def my_generator():
    try:
        yield 1
        yield 2
        raise ValueError('This will not be raised')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
        yield 3  # 继续产生值


gen = my_generator()
print(next(gen))  # 输出: 1
gen.throw(ValueError, 'Manually thrown exception')
# 输出: Caught ValueError: Manually thrown exception
# 并返回下一个yield的值：3
