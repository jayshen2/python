grades = (87,99,60,75,78,83,99,65,100,96)
print(grades.index(99))

print(grades.count(99))

grades+=(66,77,88)
print(grades)

grades_up = sorted(grades)
print(grades_up)

grades_up.reverse()
print(grades_up[:5])

grades_up.reverse()
print(grades_up[:3])

grades_up.pop(3)
print(grades_up)

grades_up.pop(0)
grades_up.pop(-1)
print(sum(grades_up)/len(grades_up))