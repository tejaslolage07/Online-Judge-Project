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


def input_test_cases(problem_index):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    test_cases = rows[problem_index-1][1]
    return test_cases


def output_test_cases(problem_index):
    conn = sqlite3.connect(
        (BASE_DIR / 'db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    test_cases = rows[problem_index-1][2]
    return test_cases
