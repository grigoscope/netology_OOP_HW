class Student:
    '''Student class.'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за домашнее задание: {self._average_rate(self.grades)} \n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
                f"Завершённые курсы: {', '.join(self.finished_courses)}\n")

    def __eq__(self, other):
        return isinstance(other, Lecturer) and self._average_rate(self.grades) == other._average_rate(other.grades)

    def __lt__(self, other):
        return isinstance(other, Lecturer) and self._average_rate(self.grades) < other._average_rate(other.grades)

    def __gt__(self, other):
        return isinstance(other, Lecturer) and self._average_rate(self.grades) > other._average_rate(self.grades)

    def __le__(self, other):
        return isinstance(other, Lecturer) and self._average_rate(self.grades) <= other._average_rate(self.grades)

    def __ge__(self, other):
        return isinstance(other, Lecturer) and self._average_rate(self.grades) >= other._average_rate(self.grades)

    def _average_rate(self, grades: dict):
        '''Average students's rate calculator function.'''
        sum_ = 0
        for course in grades:
            sum_ += sum(grades[course]) / len(grades[course])
        return round(sum_ / len(grades), 1)
    
    def rate_lecturer(self, lecturer, course, grade):
        '''Rate lecturer method'''
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            lecturer.grades[course] += [max(0, grade) if grade < 0 else min(10, grade)]
        else:
            return "Error"


class Mentor:
    '''Mentor class.'''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        '''Rate student's homework method in certain course.'''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Error"


class Lecturer(Mentor):
    '''Lecturer class.'''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 

    def __eq__(self, other):
        return isinstance(other, Student) and self._average_rate(self.grades) == other._average_rate(other.grades)

    def __lt__(self, other):
        return isinstance(other, Student) and self._average_rate(self.grades) < other._average_rate(other.grades)

    def __gt__(self, other):
        return isinstance(other, Student) and self._average_rate(self.grades) > other._average_rate(self.grades)

    def __le__(self, other):
        return isinstance(other, Student) and self._average_rate(self.grades) <= other._average_rate(self.grades)

    def __ge__(self, other):
        return isinstance(other, Student) and self._average_rate(self.grades) >= other._average_rate(self.grades)

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self._average_rate(self.grades)}\n')

    def _average_rate(self, grades: dict):
        '''Average lecturer's rate calculator function.'''
        sum_ = 0
        for course in grades:
            sum_ += sum(grades[course]) / len(grades[course])
        return round(sum_ / len(grades), 1)


class Reviewer(Mentor):
    '''Reviewer class.'''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")

    def rate_hw(self, student, course, grade):
        ''''Rate student's homework in certain course.'''
        return super().rate_hw(student, course, grade)


def students_average_rate(students : list, course):
    '''Average homework rate of every student of certain course.'''
    average_rate = 0

    for student in students:
        if isinstance(student, Student):
            courses_list = list(student.grades.keys())
            if course in courses_list:
                average_rate += sum(student.grades[course]) / len(student.grades[course])
            else:
                return f"Student {student.name} hasn't course {course}"
        else:
            return f"Error: object {student} isn't instance of class 'Student'" 
    
    return round(average_rate / len(students), 1)


def lectors_average_rate(lecturers : list, course):
    average_rate = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            course_list = list(lecturer.grades.keys())
            if course in course_list:
                average_rate += sum(lecturer.grades[course]) / len(lecturer.grades[course])
            else:
                return f"Lector {lecturer.name} hasn't course {course}"
        else:
            return f"Error: object {lecturer} isn't instance of class 'Lectorer'"
    return round(average_rate / len(lecturers), 1)


def eq_test(stud : Student, lect : Lecturer):
    '''Check if average mark of student and lecturer are equal.'''
    print(f"Average mark of student {stud.name} {stud.surname} " 
      f"and lecturer {lect.name} {lect.surname} are", \
      f"equal" if stud == lect else "not equal")


def lt_test(stud : Student, lect : Lecturer):
    '''Check if average mark of student less than average mark of lecturer.'''
    check_string = "less than" if stud < lect else "not less than"
    print(f"Average mark of student {stud.name} {stud.surname} {check_string} mark of lecturer {lect.name} {lect.surname}")


def gt_test(stud : Student, lect : Lecturer):
    '''Check if average mark of student greater than average mark of lecturer.'''
    check_string = "greater than" if stud > lect else "not greater than"
    print(f"Average mark of student {stud.name} {stud.surname} {check_string} mark of lecturer {lect.name} {lect.surname}")

def le_test(stud : Student, lect : Lecturer):
    '''Check if average mark of student less or equal than average mark of lecturer.'''
    check_string = "less or equal" if stud <= lect else "not less or equal"
    print(f"Average mark of student {stud.name} {stud.surname} {check_string} mark of lecturer {lect.name} {lect.surname}")

def ge_test(stud : Student, lect : Lecturer):
    '''Check if average mark of student greater or equal than average mark of lecturer.'''
    check_string = "greater or equal than" if stud > lect else "not greater or equal than"
    print(f"Average mark of student {stud.name} {stud.surname} {check_string} mark of lecturer {lect.name} {lect.surname}")

# First student
stud_1 = Student("Ruoy", "Eman")
stud_1.courses_in_progress += ["Python", "Git"]
stud_1.finished_courses += ["Введение в программирование"]
stud_1.grades["Python"] = [10, 9.9, 9.8]
stud_1.grades["Git"] = [10, 9.9, 9.8]
stud_1.grades["Введение в программирование"] = [10, 9.9, 9.8]
print(stud_1)

# Second student
stud_2 = Student("Andrey", "Petrov")
stud_2.courses_in_progress += ["Python", "Git"]
stud_2.finished_courses += ["Введение в программирование"]
stud_2.grades["Python"] = [8.8, 9.0, 10]
stud_2.grades["Git"] = [10, 10, 9.5]
stud_2.grades["Введение в программирование"] = [10, 10, 9.1]
print(stud_2)

# First lecturer
lect_1 = Lecturer("Some", "Buddy")
lect_1.courses_attached += ["Python", "Git"]
stud_1.rate_lecturer(lect_1, "Python", 9.9)
stud_2.rate_lecturer(lect_1, "Git", 9.8)
print(lect_1)

# Second lecturer
lect_2 = Lecturer("Oleg", "Ershov")
lect_2.courses_attached += ["Python", "Git"]
stud_1.rate_lecturer(lect_2, "Python", 9.9)
stud_2.rate_lecturer(lect_2, "Git", 9.9)
print(lect_2)

# First reviewer
rev_1 = Reviewer("Elena", "Pavlova")
print(rev_1)

# Second reviewer
rev_2 = Reviewer("Igor", "Vikrorov")
print(rev_2)

# Comparsion methods test
eq_test(stud_1, lect_1)
eq_test(stud_2, lect_1)
eq_test(stud_1, lect_2)
eq_test(stud_2, lect_2)
print("\t")
lt_test(stud_1, lect_1)
lt_test(stud_2, lect_1)
lt_test(stud_1, lect_2)
lt_test(stud_2, lect_2)
print("\t")
gt_test(stud_1, lect_1)
gt_test(stud_2, lect_1)
gt_test(stud_1, lect_2)
gt_test(stud_2, lect_2)
print("\t")
le_test(stud_1, lect_1)
le_test(stud_2, lect_1)
le_test(stud_1, lect_2)
le_test(stud_2, lect_2)
print("\t")
ge_test(stud_1, lect_1)
ge_test(stud_2, lect_1)
ge_test(stud_1, lect_2)
ge_test(stud_2, lect_2)
print("\t")

# Average homework rate of every student of certain course
stud_list = [stud_1, stud_2]
print(f"Средняя оценка студентов по курсу 'Python': {students_average_rate(stud_list, "Python")}")
print(f"Средняя оценка студентов по курсу 'Git': {students_average_rate(stud_list, "Git")}")

# Average lecture rate of every lecturer of certain course
lect_list = [lect_1, lect_2]
print(f"Средняя оценка лекторов по курсу 'Python': {lectors_average_rate(lect_list, "Python")}")
print(f"Средняя оценка лекторов по курсу 'Git': {lectors_average_rate(lect_list, "Git")}")