import os
import docker
import subprocess
from subprocess import Popen, PIPE
from .base_directory import BASE_DIR
from .database_fetch import problem_number, compiler, user_code, input_test_cases, output_test_cases, number_of_testcases


def doesFileExist(filePathAndName):
    return os.path.exists(filePathAndName)


def dockerPythonMain(problem_index):
    number_of_testcases_in_out = number_of_testcases(problem_index)


    try:
        subprocess.run('docker start python-container', shell=True)
    except:
        subprocess.run(
            'docker run -dt --name python-container python', shell=True)

    subprocess.run(
        ['docker', 'cp', (BASE_DIR / 'OJ/PythonCoderunner/py.py'), 'python-container:/a.py'])
#    run = subprocess.run('docker exec -i python-container python3 a.py',
#                         shell=True, capture_output=True, text=True, input=test_case_input)
#    # subprocess.run(['docker', 'exec', 'rm', 'a.py'])
#    if run.stdout == test_case_output:
#        return 1
#    elif (run.stdout != test_case_output and run.stderr == ''):
#        return 0
#    elif run.stderr != '':
#        return -1

    for number_of_already_evaluated in range(0, number_of_testcases_in_out):
        test_case_input = input_test_cases(problem_index, number_of_already_evaluated)
        test_case_output = output_test_cases(problem_index, number_of_already_evaluated)

        run = subprocess.run('docker exec -i python-container python3 a.py',
                            shell=True, capture_output=True, text=True, input=test_case_input)

        if run.stdout == test_case_output:
            check = 1
        elif run.stderr != '':
            check = -1
            break
        elif run.stdout != test_case_output:
            check = 0
            break
    subprocess.run(['docker exec python-container rm a.py'], shell=True)
    return check



def pythonMain(problem_index):

    test_case_input = input_test_cases(problem_index, 0)
    test_case_output = output_test_cases(problem_index, 0)
    result = subprocess.run(['python3', (BASE_DIR / 'OJ/PythonCoderunner/py.py')],
                            capture_output=True, text=True, input=test_case_input)
    answer = result.stdout
    error = result.stderr
    # result = subprocess.run(
    #     './a.out', capture_output=True, text=True, input=test_case_input).stdout
    if test_case_output == answer:
        return 1
    elif test_case_output != answer and error == '':
        return 0
    elif error != '':
        return -1
