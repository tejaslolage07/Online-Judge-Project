import os
import subprocess
import database_fetch


def doesFileExist(filePathAndName):
    return os.path.exists(filePathAndName)


def main():
    subprocess.run(
        ['cd', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/coderunner/'])
    subprocess.run(['g++', 'cpp.cpp'])
    if doesFileExist('./a.out'):
        test_case_input = database_fetch.input_test_cases(1)
        test_case_output = database_fetch.output_test_cases(1)
        result = subprocess.run(
            './a.out', capture_output=True, text=True, input=test_case_input).stdout
        if test_case_output == result:
            return 'Accepted'
        else:
            return 'Wrong answer'

    else:
        return 'Compilation error'


print(main())
