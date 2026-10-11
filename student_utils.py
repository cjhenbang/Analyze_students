
#Global constant
#gc1
valid_keys = ["student_id",
                  "name",
                  "study_hours",
                  "attendance",
                  "homework_score",
                  "midterm_score",
                  "sleep_hours",
                  "final_score"
                  ]

def record_error(info_list: list[str], errors: list[str], error_records: list[dict]) -> None:
    record = {"info": None, "errors": None}

    record["info"] = info_list

    record["errors"] = errors

    error_records.append(record)

    return


def check_line(info_list: list, student_list: list[dict], error_records: list[dict]) -> bool:
    errors = []

    check_columns(info_list, errors)

    if errors:
        record_error(info_list, errors, error_records)
        return False

    check_id(info_list, errors, student_list)
    check_name(info_list, errors)
    check_study_hours(info_list, errors)
    check_attendance_score(info_list, errors)
    check_homework_score(info_list, errors)
    check_midterm_score(info_list, errors)
    check_sleep_hours(info_list, errors)
    check_final_scores(info_list, errors)

    if errors:
        record_error(info_list, errors, error_records)
        return False
    else:
        return True


def check_file(file_name: str) -> bool:
    """

    :param file_name:
    :return:False if any validations fails.
            True if all validations pass.

    Validations:
        1:A file with the specific name should exist.
        2.The file cannot be empty.csv
    """

    try:
        file = open(file_name, "r")
        file.close()
    except FileNotFoundError:
        print(f"There is not a file called '{file_name}', please check the file name you typed in.")
        return False
    except Exception as e:
        print("Something goes wrong, we will pull out the error information for you.")
        print(f"\t{e}")
        return False
    # try to do it!

    with open(file_name, "r") as file:
        content = file.read().strip()
        if not content:
            print(f"This file is empty.")
            return False

    return True


def check_columns(info_list: list, errors: list[str]) -> None:
    length = len(info_list)
    if length < 8:
        errors.append(
            f"There are too less information in this line. We expect get 8 information, but only find {length}.")
    elif length > 8:
        errors.append(f"There are too many information in this line. We expect get 8 information, but find {length}.")
    return


def check_id(info_list: list, errors: list[str], student_list: list[dict]) -> None:
    student_id = info_list[0]
    if not student_id:
        errors.append(f"This student id is: {student_id},this id number is empty.csv.")
        return

    # This line checks if the stutend id is consist of exact 4 numbers.
    # If the student id is made up of exact 4 numbers and positive, it will be fine.
    # Otherwise, a error messasge will be added to the list.
    if not student_id.isdigit() or len(student_id) != 4:
        errors.append(f"This student id is: {student_id}, the id numbers should be 4 digits, and bigger than 0.")
        return

    """
    This module is to check if current student who is going to be added into the student list has a replicate student_id
    with any previous student. If it does, current student will not be added into the list, and a error message will be
    added into the error message list.
    """
    for student in student_list:
        if student_id == student["student_id"]:
            errors.append(f"The student student_id {student_id} for has appeared, "
                          f"I will put our students of the same id for you."
                          f"\n\t\texist one: {student}"
                          f"\n\t\tCurrent one: {info_list}")


def check_name(info_list: list[str], errors: list[str]) -> None:
    name = info_list[1]

    if not name.strip():
        errors.append(f"Your name is: {name},the name is empty.csv.")

    if any(char.isdigit() for char in name):
        errors.append(f"Your name is: {name},there is some numbers in name.")

    if len(name) >= 100:
        errors.append(f"Your name is: {name},the name is longer than 100 letters. Please check it.")

    return


def check_study_hours(info_list: list[str], errors: list[str]) -> None:
    """
    :param info_list:
    :param errors:
    :return: None

    This function is can check the integrity of hours data. It will be used to checkc
    study hours and sleep hours of student information
    """
    study_hours_str = info_list[2]
    check_number(study_hours_str, "study_hours", 24, 0, False, errors)

    return


def check_number(number_str: str, number_type: str, max: int, min: int, is_int: bool, errors: list[str]) -> None:
    """
    This function checks if the number is valid.
    We check if all the below are satisfied:
    1. The number is in the valid range.
    2. The int value should pass in an integer, the float value will be fine whatever an ineteger or float passed in.
    :param number_str: the string of the number. We will convert it to int or float.
    :param number_type: The 'name' of the number. Such as 'scores', 'hours'....
    :param max: The biggest value this number can be.
    :param min: The smallest value this number can be.
    :param is_int: To claim if it is an int. Then we know to convert it to int or float.
    :param errors: The error list. If we find an error, we will add the error to this list.
    :return: None. If the number is good, it will be fine. If it has some problem, the error message will
        be appended to the errors[list].
    """
    try:
        number = float(number_str.strip())
    except ValueError:
        errors.append(f"The {number_type} is: {number_str}, it should be a number.")
        return

    if is_int:
        if (number % 1) == 0:
            number = int(number)
        else:
            errors.append(f"The {number_type} is: {number}, we can't convert it to a integer.")

    if number < min:
        errors.append(f"The {number_type} is: {number}, it should not be smaller than {min}.")
    elif number > max:
        errors.append(f"The {number_type} is: {number}, it should not be greater than {max}.")


# modifing
def check_attendance_score(info_list: list[str], errors: list[str]) -> None:
    """
    Check if the attendance score is valid, by pass the number and requirements into the function: Check_number.
    :helper function:
    :param info_list: The list of the total information line of a student.
    :param errors: the errors list.
    :return: None
    """
    attendance_score_str = info_list[3]
    check_number(attendance_score_str, "attendance_score", 100, 0, False, errors)

    return


# errors.append(f"The  is: {}, it should be a positive number.")
def check_homework_score(info_list: list[str], errors: list[str]) -> None:
    homework_score_str = info_list[4]
    check_number(homework_score_str, "homework_score", 100, 0, False, errors)
    return


def check_midterm_score(info_list: list[str], errors: list[str]) -> None:
    midterm_score_str = info_list[5]
    check_number(midterm_score_str, "midterm_score", 100, 0, False, errors)
    return


def check_sleep_hours(info_list: list[str], errors: list[str]) -> None:
    sleep_hours_str = info_list[6]
    check_number(sleep_hours_str, "sleep_horus", 24, 0, False, errors)
    return


def check_final_scores(info_list: list[str], errors: list[str]) -> None:

    final_score_str = info_list[7]
    check_number(final_score_str, "final_score", 100, 0, False, errors)
    return


def convert_info_to_string(info_list: list[str]) -> str:
    """
    This function
    :param info_list:
    :return:
    """
    line_keys = ["student_id",
                  "name",
                  "study_hours",
                  "attendance",
                  "homework_score",
                  "mideterm_score",
                  "sleep_hours",
                  "final_score"
                  ]

    length = len(info_list)

    result = ""

    for i in range(length):
        if i <= 7:
            result += f" <{line_keys[i]}>: {info_list[i]},"
        else:
            result += f"<unexpected_field>: {info_list[i]},"

    # delete the first space and the final ','
    result = result[1:-1]

    return result


def print_all_students(students: list) -> None:
    for student in students:
        print(student)

    return


def print_import_summary(students: list[dict], error_records: list[dict]) -> None:
    nums_of_error_records = len(error_records)
    num_lines = count_total_lines(students, error_records);
    num_failed = count_failed_lines(error_records);
    num_successed = count_valid_students(students);



    print()

    print("---Summary:")
    print(
        f"There were {num_lines} lines of student infos.\n{num_successed} lines were successfully added.{num_failed} line were not added successfully\n")

    for list_index, record in enumerate(error_records):
        error_number = list_index + 1
        print(f"{error_number}:{convert_info_to_string(record['info'])}")

        for e_index, error in enumerate(record["errors"]):
            e_number = e_index + 1
            print(f"\tError{e_number}:{error}")
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

    student_dict["student_id"] = info_list[0]
    student_dict["name"] = info_list[1]
    student_dict["study_hours"] = float(info_list[2])
    student_dict["attendance"] = float(info_list[3])
    student_dict["homework_score"] = float(info_list[4])
    student_dict["midterm_score"] = float(info_list[5])
    student_dict["sleep_hours"] = float(info_list[6])
    student_dict["final_score"] = float(info_list[7])

    return student_dict


# statistic part

def count_valid_students(students: list[dict]) -> int:
    # This function calculates how many of valid information of students are imported to the list of dictionary
    return len(students)


def count_failed_lines(failed_lines: list[str]) -> int:
    # This function calculates how many lines of information are failed importing to the list of dictionary
    return len(failed_lines)


def count_total_lines(student_lines: list[dict], failed_lines: list[str]) -> int:
    return len(student_lines) + len(failed_lines)


def calculate_average(student_list: list[dict], key: str) -> float:
    """

    :param student_lines:
    :param key:
    :return:
    """

    if key not in valid_keys[2:]:
        print(f"The key you want to search about is {key}."
              f"\n It is not a valid key. a valid key should be one of them: {valid_keys[2:]}")
        return -1

    if not student_list:
        print("We didn't find any valid student record.")
        return -1

    num_students = len(student_list)
    total = 0

    for student in student_list:
        total += student[key]

    average = total / num_students
    return average


def sort_dictionaries(students: list[dict], key: str) -> list[dict]:
    """
    This function sort dictionaries by a field of dictionaries. The key is set by user.
        The key should be one of the eight keys of the dictionary. Like 'final_score','student_id'.
        It doesn't change anything of the original list of dictionaries. This function will put
        the sorted list into a new variable.
    :param students: A list consist of many dictionaries, each one includes information of a student.
    :return: A new list of dictionaries sorted by the user_specified key.
            If the students parameters passed in is empty -> An empty list will be returned.
            If the key parameters passed in does not match any of the valid keys. -> An empty list will be retuened.
    """
    if not students:
        print("There is no student in this data. Please check.")
        return []

    if key not in valid_keys:
        print(f"The key you want to search about is {key}."
              f"\n It is not a valid key. a valid key should be one of them: {valid_keys}")
        return []

    sorted_students = sorted(students, key=lambda student:student[key])
    return sorted_students


def calculate_median(student_list: list[dict]) -> float:
    """
    This function will calculate the median of final scores of a group of students.
    First it checks if the list is empty. If it does, a error message will be printed.

    If the list includes at least one student, this function will calculate the median index
        based on the amount of student in the list in odd or even. Then call the sort_dictionaries
        to sort the students->list[student] based on their final score, from low to high. Then finally
        calculate the median.
    :param student_list: A list consist of many dictionaries, each one includes information of a student.
    :return: The calculated median.
    :helper function: sort_dictionaries
    """
    if not student_list:
        print(f"There is no student in this data. Please check.")
        return -1

    sorted_students = sort_dictionaries(student_list, "final_score")
    length = len(student_list)

    median_index = length // 2

    if length % 2 == 0:
        median_1 = sorted_students[median_index]["final_score"]
        median_2 = sorted_students[median_index - 1]["final_score"]
        result = (median_1 + median_2) / 2
    else:
        result = sorted_students[median_index]["final_score"]

    return result



def calculate_statistics():
    pass
