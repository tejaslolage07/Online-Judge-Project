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

    for number_of_already_evaluated in range(0, number_of_testcases_in_out):
        test_case_input = input_test_cases(problem_index, number_of_already_evaluated)
        test_case_output = output_test_cases(problem_index, number_of_already_evaluated)

        run = subprocess.run('docker exec -i python-container python3 a.py',
                            shell=True, capture_output=True, text=True, input=test_case_input)
        print("run =", run)
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

