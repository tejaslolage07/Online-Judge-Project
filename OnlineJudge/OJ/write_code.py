# 'r' - open file for reading
# 'w' - open file for writing
# 'x' - open file if it doesnt exist
# 'a' - open file for appending/adding
# 't' - open text file
# 'b' - open binary mode
# '+' - open file for read + write
from .database_fetch import latest_user_code, latest_compiler


def writeCpp(userid):
    f = open('/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/CppCoderunner/cpp.cpp', 'w')
    f.write(latest_user_code(userid))
    f.close()


def writeJava(userid):
    k = open('/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/java.java', 'w')
    k.write(latest_user_code(userid))
    k.close()


def writePython(userid):
    l = open('/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/PythonCoderunner/py.py', 'w')
    l.write(latest_user_code(userid))
    l.close()


def writeCode(userid):
    if latest_compiler(userid) == 'GNU G++ 17':
        writeCpp(userid)
    elif latest_compiler(userid) == 'Java':
        writeJava(userid)
    elif latest_compiler(userid) == 'Python 3':
        writePython(userid)


# f = open('OJ/cpp.cpp', 'a')
# f.write()
# print(content)

# f.close()
