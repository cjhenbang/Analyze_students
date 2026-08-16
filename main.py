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
#This is a list compose of students, each student is a dictionary
students = []
#This is the number that how many lines are failed to be added
failed_to_add = 0
#this will show the lines that were not added successfuly
failed_list = []

def check_line(info_list: list) -> bool:

    errors = []

    check_columns(info_list, errors)
    check_id(info_list, errors)
    check_name(info_list, errors)
    check_study_hours(info_list, errors)


    if errors:
        for error in errors:
            info_list.append(error)
        failed_list.append(info_list)
        return False
    else:
        return True


def check_columns(info_list: list[str], errors: list[str]) -> None:
    if len(info_list) != 8:
        errors.append("There are too many or less informations in the line.")
    return

def check_id(info_list: list[str], errors: list[str]) -> None:
    id = info_list[0]
    if not id:
        errors.append(f"This student id is:{id},this id number is empty.")
        return

    if id.isdigit():
        if len(id) == 4 and int(id)>0:
            return

    errors.append(f"This student id is:{id}, the id numbers should be 4 digits.")

def check_name(info_list: list[str], errors: list[str])-> None:
    name = info_list[1]

    if not name.strip():
        errors.append(f"Your name is:{name},the name is empty.\n")

    if any(char.isdigit() for char in name):
        errors.append(f"Your name is:{name},there is some numbers in name.\n")

    if len(name) >= 100:
        errors.append(f"Your name is:{name},the name is longer than 100 letters. Please check it.\n")

    return


def check_study_hours(info_list: list[str], errors: list[str]) ->None :
    """
    :param info_list:
    :param errors:
    :return: None

    This function is can check the integrity of hours data. It will be used to check
    study hours and sleep hours of student information
    """

    try:
        study_hours = float(info_list[2].strip())
    except:
        errors.append(f"The study_hours is:{info_list[2].strip()}, it should be a number")
        return

    if study_hours <= 0:
        errors.append(f"The study_hours is:{study_hours}, it should be a positive number.")
    elif study_hours >= 24:
        errors.append(f"The study_hours is:{study_hours}, it shouldn't be equal to or larger than 24.")

    return




def check_attendance(info_list: list[str], errors: list[str]) ->None:
    pass

def check_homework_score(info_list: list[str], errors: list[str]) ->None:
    pass

def check_midterm_score(info_list: list[str], errors: list[str]) ->None:
    pass

def check_sleep_hours(info_list: list[str], errors: list[str]) ->None:
    pass

def check_final_scores(info_list: list[str], errors: list[str]) -> None:
    pass


    """
    if id.isdigit() and len(id) == 4:
        digital_id = int(id)
        if type(digital_id) == int and digital_id > 0:
            return 0

    return 2
    """

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
    student_dict["attendance"] = info_list[3]
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
        print("\n", type(info_list))
        print(f"Infos are: {info_list}\n")
    #print(f"first student is {student_dict}")

    for student in students:
        print(student)

    print(f"\n{failed_to_add} line were not added successfully.")
    #print(f"There are the lines which are not added successfully {failed_list}")

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
    for line in file:
        print(line)
"""
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
