# 这是一个示例 Python 脚本。
import sys
import student_utils as su

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

"""
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

"""
# student_id,name,study_hours,attendance,homework_score,midterm_score,sleep_hours,final_score

"""
This dictionary 
"""

#Global constant


# Main program

#file_name = "tests_student_examples"
file_name = "students.csv"
#file_name = "mixed.csv"

if not su.check_file(file_name):
    sys.exit()

with open(file_name, "r") as file:
    """
    data = file.read()
    print(data)
    """

    # This is a list compose of students, each student is a dictionary
    students = []
    # This is the number that how many lines are failed to be added
    #total_lines = 0
    #num_of_validate_lines = 0
    #num_of_failed_line = 0
    # this will show the lines that were not added successfuly
    error_records = []

    # data = file.readline()
    # data = file.readline().strip().split(",")

    file.readline()

    for line in file:

        # my_dict = create_dict(line.strip().split(","))
        line_info = line.strip().split(",")
        # Check if the current line has the right information to make a dictionary
        # if it does, make it. If it is not, record the content and add it to the
        # list and count it.
        if su.check_line(line_info, students, error_records):
            current_dict = su.create_dict(line_info)
            students.append(current_dict)

    su.print_all_students(students)
    # to print the errors


    su.print_import_summary(students, error_records)

    #print statistics
    for student in su.sort_dictionaries(students, "final_score"):
        print(f"sorted by final_score: {student}")

    print(f"average: {su.calculate_average(students, 'attendance')}")
    print(f"The median is :{su.calculate_median(students)}")


"""
    for line in file:
        print(line)
"""
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
