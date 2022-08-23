# 'r' - open file for reading
# 'w' - open file for writing
# 'x' - open file if it doesnt exist
# 'a' - open file for appending/adding
# 't' - open text file
# 'b' - open binary mode
# '+' - open file for read + write
from .database_fetch import latest_user_code


def writeCpp(userid):
    f = open('/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/cpp.cpp', 'w')
    f.write(latest_user_code(userid))
    f.close()


# f = open('OJ/cpp.cpp', 'a')
# f.write()
# print(content)

# f.close()
