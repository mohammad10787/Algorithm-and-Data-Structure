class Dic:
    pass



if __name__ == '__main__':
    # how to define a dictionary
    student = {'name': 'John', 'age': 25, 'course': ['Math', 'CompSci']}

    # how to add to that dictionary

    student['phone'] = '0913'
    student['name'] = 'Jane'

    print(student.get('phone', 'Not Found'))
    print(student.get('name', 'Not Found'))

    student.update({'name': 'Jane', 'age': 26, 'phone': '0912'})

    print(student.get('phone', 'Not Found'))
    print(student.get('age', 'Not Found'))

    print(student.keys())
    print(student.values())
    print(student.items())
    print(len(student))

    print("===================")
    for key, value in student.items():
        print(key)
        print(student[key])
        print(key, value)

    del student['age']

    print(student, student.pop('name'))


