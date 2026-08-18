# 这是一个示例 Python 脚本。

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
#student_id,name,study_hours,attendance,homework_score,midterm_score,sleep_hours,final_score

"""
This dictionary 
"""

def check_line(info_list: list) -> bool:

    errors = []

    check_columns(info_list, errors)

    if errors:
        info_list.append(errors)
        failed_list.append(info_list)
        return False


    check_id(info_list, errors)
    check_name(info_list, errors)
    check_study_hours(info_list, errors)
    check_attendance_score(info_list, errors)
    check_homework_score(info_list, errors)
    check_midterm_score(info_list, errors)
    check_sleep_hours(info_list,errors)
    check_final_scores(info_list,errors)


    if errors:
        info_list.append(errors)
        failed_list.append(info_list)
        return False
    else:
        return True


def check_columns(info_list: list[str], errors: list[str]) -> None:
    length = len(info_list)
    if length < 8:
        errors.append(f"There are too less information in this line. We expect get 8 information, but only find {length}.")
    elif length > 8:
        errors.append(f"There are too many information in this line. We expect get 8 information, but find {length}")
    return

def check_id(info_list: list, errors: list[str]) -> None:
    student_id = info_list[0]
    if not student_id:
        errors.append(f"This student id is: {student_id},this id number is empty.")
        return

    if student_id.isdigit():
        if len(student_id) == 4 and int(student_id)>0:
            return

    errors.append(f"This student id is: {student_id}, the id numbers should be 4 digits.")

def check_name(info_list: list[str], errors: list[str])-> None:
    name = info_list[1]

    if not name.strip():
        errors.append(f"Your name is: {name},the name is empty.")

    if any(char.isdigit() for char in name):
        errors.append(f"Your name is: {name},there is some numbers in name.")

    if len(name) >= 100:
        errors.append(f"Your name is: {name},the name is longer than 100 letters. Please check it.")

    return


def check_study_hours(info_list: list[str], errors: list[str]) ->None :
    """
    :param info_list:
    :param errors:
    :return: None

    This function is can check the integrity of hours data. It will be used to check
    study hours and sleep hours of student information
    """
    study_hours_str = info_list[2]
    check_number(study_hours_str, "study_hours", 24, 0, False, errors)

    return


def check_number(number_str: str, number_type: str, max: int, min: int, is_int: bool, errors:list[str]) -> None:
    try:
        number = float(number_str.strip())
    except:
        errors.append(f"The {number_type} is: {number_str}, it should be a number.")
        return

    if is_int:
        if (number % 1) == 0:
            number = int(number)
        else:
            errors.append(f"The {number_type} is: {number}, we can't convert it to a interger.")

    if number < min:
        errors.append(f"The {number_type} is: {number}, it should not be smaller than {min}.")
    elif number > max:
        errors.append(f"The {number_type} is: {number}, it should not be greater than {max}.")

#modifing
def check_attendance_score(info_list: list[str], errors: list[str]) ->None:
    attendance_score_str = info_list[3]
    check_number(attendance_score_str, "attendance_score", 100, 0, True, errors)

    return


#errors.append(f"The  is: {}, it should be a positive number.")
def check_homework_score(info_list: list[str], errors: list[str]) ->None:
    homework_score_str = info_list[4]
    check_number(homework_score_str, "homework_score", 100, 0, True, errors)
    return

def check_midterm_score(info_list: list[str], errors: list[str]) ->None:
    midterm_score_str = info_list[5]
    check_number(midterm_score_str, "midterm_score", 100, 0, True, errors)
    return

def check_sleep_hours(info_list: list[str], errors: list[str]) ->None:
    sleep_hours_str = info_list[6]
    check_number(sleep_hours_str, "sleep_horus", 24, 0, False, errors)
    return

def check_final_scores(info_list: list[str], errors: list[str]) -> None:
    final_score_str = info_list[7]
    check_number(final_score_str, "final_score", 100, 0, False, errors)
    return

    """
    if id.isdigit() and len(id) == 4:
        digital_id = int(id)
        if type(digital_id) == int and digital_id > 0:
            return 0

    return 2
    """

def print_failed_line(failed_line: list[str]) -> None:
    pass

def count_infos(line: list) -> int:
    """
    it will count how many of information a line has.
    :param line:
    :return:
    """
    num = 0
    for info in line:
        if type(info) == str:
            num += 1
    return num


def print_errors_info(failed_list: list[list[str]]) -> None:

    nums_of_failed_line = len(failed_list)
    line_infos = ["student_id",
                  "name",
                  "study_hours",
                  "attendance",
                  "homework_score",
                  "mideterm_score",
                  "sleep_hours",
                  "final_score"
                  ]

    print(f"\n{nums_of_failed_line} line were not added successfully\n")

    for list_index, failed_line in enumerate(failed_list):

        nums_of_infos = count_infos(failed_line)

        errors = failed_line[-1]

        print(f"Failed line {list_index+1} ->", end=' ')
        #print(failed_line)
        for i in range(nums_of_infos):
            print(f"{line_infos[i]}: {failed_line[i]}, ", end = '')


        print()
        for e_index, error in enumerate(errors):
            print(f"\t Error{e_index+1}: {error}")
        print()


    print()


def create_dict(info_list: list) -> dict:

    student_dict = {
        "student_id": None,
        "name": None,
        "study_hours": None,
        "attendance": None,
        "homework_score": None,
        "midterm_score": None,
        "sleep_hours": None,
        "final_score": None
    }

    student_dict["student_id"] = int(info_list[0])
    student_dict["name"] = info_list[1]
    student_dict["study_hours"] = float(info_list[2])
    student_dict["attendance"] = int(info_list[3])
    student_dict["homework_score"] = info_list[4]
    student_dict["midterm_score"] = info_list[5]
    student_dict["sleep_hours"] = info_list[6]
    student_dict["final_score"] = info_list[7]

    return student_dict


with open("students.csv", "r") as file:
    """
    data = file.read()
    print(data)
    """

    # This is a list compose of students, each student is a dictionary
    students = []
    # This is the number that how many lines are failed to be added
    failed_to_add = 0
    # this will show the lines that were not added successfuly
    failed_list = []

    #data = file.readline()
    #data = file.readline().strip().split(",")

    file.readline()

    for line in file:

        #my_dict = create_dict(line.strip().split(","))
        info_list = []
        info_list = line.strip().split(",")
        #Check if the current line has the right information to make a dictionary
        #if it does, make it. If it is not, record the content and add it to the
        #list and count it.
        if check_line(info_list):
            current_dict = create_dict(info_list)
            students.append(current_dict)
        else:
            failed_to_add += 1

        #print(f"whole line is: {line}")
        #These two lines are shows the data

        #print("\n", type(info_list))
        #print(f"Infos are: {info_list}\n")
    #print(f"first student is {student_dict}")

    for student in students:
        print(student)


    #to print the errors

    #new version


    print_errors_info(failed_list)

    #old version
"""
    for index, info_list in enumerate(failed_list):
        print(f"{index}", end = "")
        info_length = len(info_list)
        if info_length <= 8:
            for i in range(info_length - 1):
                print(info_list[i], end="")
                print("\n")
        else:
            error_length = len(info_list)-8
            for i in range(8):
                print(info_list[i], end="")
            for i in range(error_length):
                print(info_list[7+error_length])

        print("\n")        
"""

"""
    for line in file:
        print(line)
"""
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
