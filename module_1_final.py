grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_list_students = sorted(students)
average_grades = [sum(grade) / len(grade) for grade in grades]
round_average_grades = [round(num, 1) for num in average_grades]
dict_average_student_grades = dict(zip(sort_list_students, round_average_grades))

print(dict_average_student_grades)