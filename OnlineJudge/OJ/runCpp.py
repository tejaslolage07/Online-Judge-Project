import os
import docker
import subprocess
from subprocess import Popen, PIPE
from .base_directory import BASE_DIR
from .database_fetch import problem_number, compiler, user_code, input_test_cases, output_test_cases, number_of_testcases


def doesFileExist(filePathAndName):
    return os.path.exists(filePathAndName)


def dockerCppMain(problem_index):
#    client = docker.from_env()
#    test_case_input = input_test_cases(problem_index)
#    test_case_output = output_test_cases(problem_index)
    number_of_testcases_in_out = number_of_testcases(problem_index)

    try:
        # cont = client.containers.get('cpp-container')
        # cont_state = cont.attrs['state']
        # if cont_state['status'] != 'running':
        subprocess.run('docker start cpp-container', shell=True)
    except docker.errors.NotFound:
        subprocess.run("docker pull gcc", shell=True)
        subprocess.run('docker run -dt --name cpp-container gcc', shell=True)

    subprocess.run(
        ['docker', 'cp', (BASE_DIR / 'OJ/CppCoderunner/cpp.cpp'), 'cpp-container:/a.cpp'])
    compile = subprocess.run('docker exec cpp-container g++ -o out a.cpp',
                         shell=True, capture_output=True)
    check = 0
    if compile.returncode != 0:
        # if doesFileExist('cpp-container:/home/a.out'):
        return -1
    else:
#        run = subprocess.run('docker exec -i cpp-container ./out',
#                             input=test_case_input, capture_output=True, text=True, shell=True)
#        subprocess.run(['docker', 'exec', 'rm', 'out'], shell=True)
#        subprocess.run(['docker', 'exec', 'rm', 'a.cpp'], shell=True)
#        if run.stdout == test_case_output:
#            return 1
#        elif run.stdout != test_case_output:
#            return 0
#        elif run.stderr != '':
#            return -1
        for number_of_already_evaluated in range(0, number_of_testcases_in_out):
            test_case_input = input_test_cases(
                problem_index, number_of_already_evaluated)
            test_case_output = output_test_cases(
                problem_index, number_of_already_evaluated)

            run = subprocess.run('docker exec -i cpp-container ./out',
                                 input=test_case_input, capture_output=True, text=True, shell=True)
            if run.stdout == test_case_output:
                check = 1
            elif run.stderr != '':
                check = -1
                break
            elif run.stdout != test_case_output:
                check = 0
                break
        subprocess.run(['docker exec cpp-container rm out'], shell=True)
        subprocess.run(['docker exec cpp-container rm a.cpp'], shell=True)
        return check



def cppMain(problem_index):

    # subprocess.run(['docker', 'run', '-it', 'gcc'])
    # containerID = subprocess.Popen(['docker', 'ps', '-q', '--latest'])
    # source_path = (containerID+':'+'/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/onlinejudge/oj/Cppcoderunner')
    # subprocess.Popen(['docker', 'cp', source_path, '/home/'])
    subprocess.run(
        ['g++', (BASE_DIR / 'OJ/CppCoderunner/cpp.cpp'), '-o', (BASE_DIR / 'OJ/CppCoderunner/a.out')])
    if doesFileExist((BASE_DIR / 'OJ/CppCoderunner/a.out')):
        test_case_input = input_test_cases(problem_index)
        test_case_output = output_test_cases(problem_index)
        result = subprocess.run(
            (BASE_DIR / 'OJ/CppCoderunner/a.out'), capture_output=True, text=True, input=test_case_input).stdout
        subprocess.run(
            ['rm', (BASE_DIR / 'OJ/CppCoderunner/a.out')])
        if test_case_output == result:
            return 1
        else:
            return 0
    else:
        return -1
