import os
import subprocess
from subprocess import Popen, PIPE
from .database_fetch import problem_number, compiler, user_code, input_test_cases, output_test_cases


def doesFileExist(filePathAndName):
    return os.path.exists(filePathAndName)


def cppMain(problem_index):
    # process = Popen(
    #     ['cd', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ'])
    # subprocess.run()
    subprocess.run(
        ['g++', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/cpp.cpp', '-o', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/a.out'])
    if doesFileExist('/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/a.out'):
        test_case_input = input_test_cases(problem_index)
        test_case_output = output_test_cases(problem_index)
        result = subprocess.run(
            '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/a.out', capture_output=True, text=True, input=test_case_input).stdout
        subprocess.run(
            ['rm', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/a.out'])
        if test_case_output == result:
            return 1
        else:
            return 0
    else:
        return -1
