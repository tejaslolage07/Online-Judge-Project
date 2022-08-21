# 'r' - open file for reading
# 'w' - open file for writing
# 'x' - open file if it doesnt exist
# 'a' - open file for appending/adding
# 't' - open text file
# 'b' - open binary mode
# '+' - open file for read + write

def writeCpp(code):
    f = open('OJ/cpp.cpp', 'w')
    f.write(code)
    f.close()

# f = open('OJ/cpp.cpp', 'a')
# f.write()
# print(content)

# f.close()

