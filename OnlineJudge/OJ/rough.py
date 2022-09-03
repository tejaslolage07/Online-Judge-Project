import sqlite3
conn = sqlite3.connect(('/home/ubuntu/Online-Judge-Project/OnlineJudge/db.sqlite3'))
cur = conn.cursor()
cur.execute("SELECT * FROM OJ_testcase")
rows = cur.fetchall()
# for i in range(len(rows)):
#     print(rows[i])


def number_of_testcases(problem_index):
    conn = sqlite3.connect(
        ('/home/ubuntu/Online-Judge-Project/OnlineJudge/db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    rowLen = len(rows)
    number = 0
    for i in range (0, rowLen):
            if rows[i][3] == problem_index:
                number += 1
    return number

# print(number_of_testcases(4))

def output_test_cases(problem_index, number_of_already_evaluated):
    conn = sqlite3.connect(
        ('/home/ubuntu/Online-Judge-Project/OnlineJudge/db.sqlite3'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM OJ_testcase")
    rows = cur.fetchall()
    rowLen = len(rows)
    for i in range(0, rowLen):
        if number_of_already_evaluated == 0:
            if rows[i][3] == problem_index:
                return rows[i][2]
                break
        else:
            if rows[i][3] == problem_index:
                number_of_already_evaluated -= 1
                continue


print(output_test_cases(4, number_of_testcases(4)-1))
