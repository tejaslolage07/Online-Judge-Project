import sqlite3


def userCode(index):
    conn = None
    try:
        conn = sqlite3.connect(
            '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/db.sqlite3')
    except sqlite.Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_usersubmission")
    rows = cur.fetchall()
    code = rows[index][1]
    return code


def input_test_cases(problem_index):
    conn = None
    try:
        conn = sqlite3.connect(
            '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/db.sqlite3')
    except sqlite.Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    test_cases = rows[problem_index-1][1]
    return test_cases


def output_test_cases(problem_index):
    conn = None
    try:
        conn = sqlite3.connect(
            '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/db.sqlite3')
    except sqlite.Error as e:
        print(e)
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    test_cases = rows[problem_index-1][2]
    return test_cases
