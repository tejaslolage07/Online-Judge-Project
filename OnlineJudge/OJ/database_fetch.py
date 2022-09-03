import sqlite3
from .base_directory import BASE_DIR


def user_code(index):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_usersubmission")
    rows = cur.fetchall()
    code = rows[index-2][1]
    return code


def latest_user_code(userid):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_usersubmission")
    rows = cur.fetchall()
    rowLen = len(rows)
    for i in range(rowLen-1, 0, -1):
        if rows[i][5] == userid:
            return rows[i][1]
            break


def compiler(index):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_usersubmission")
    rows = cur.fetchall()
    compiler = rows[index][4]
    return compiler


def latest_compiler(userid):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_usersubmission")
    rows = cur.fetchall()
    rowLen = len(rows)
    for i in range(rowLen-1, 0, -1):
        if rows[i][5] == userid:
            return rows[i][4]
            break


def problem_number(index):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_usersubmission")
    rows = cur.fetchall()
    problem_number = rows[index][3]
    return problem_number


def number_of_testcases(problem_index):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    rowLen = len(rows)
    number = 0
    for i in range (0, rowLen-1):
            if rows[i][3] == problem_index:
                number += 1
    return number



# These functions of input_test_cases() and output_test_cases() are very unoptimised (O(n^2)). This can become a problem if
# testcases for a particular problem exceeds 10^3 and so on. For reducing the complexity, the database could be better structured 
# to have separate models/containers for each problem, thus making it easier to traverse through the testcases. The other way could 
# be to optimise the functions itself to include a pointer algorithm which can track which testcase has been evaluated till now and 
# proceed further, not needing to go through the entire database after each evaluation (O(n)). 

# The higher complexity is accepted for a fact that it decreases the effort and increases accessibility with allowing us to simply 
# write new testcases for a particular problem without caring about the order in which any question's testcase is added.


def input_test_cases(problem_index, number_of_already_evaluated):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    rowLen = len(rows)
    for i in range(0, rowLen-1):
        if number_of_already_evaluated == 0:
            if rows[i][3] == problem_index:
                test_case = rows[i][1]
                return test_case
        else:
            if rows[i][3] == problem_index:
                number_of_already_evaluated -= 1


#def output_test_cases(problem_index):
#    conn = sqlite3.connect(
#        (BASE_DIR / 'db.sqlite3'))
#    cur = conn.cursor()
#    cur.execute("SELECT * FROM OJ_testcase")
#    rows = cur.fetchall()
#    test_cases = rows[problem_index-1][2]
#    return test_cases


def output_test_cases(problem_index, number_of_already_evaluated):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    rowLen = len(rows)
    for i in range(0, rowLen-1):
        if number_of_already_evaluated == 0:
            if rows[i][3] == problem_index:
                test_case = rows[i][2]
                return test_case
        else:
            if rows[i][3] == problem_index:
                number_of_already_evaluated -= 1
