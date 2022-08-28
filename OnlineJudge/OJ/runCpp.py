import os
import subprocess
from subprocess import Popen, PIPE
from .database_fetch import problem_number, compiler, user_code, input_test_cases, output_test_cases
import docker


def doesFileExist(filePathAndName):
    return os.path.exists(filePathAndName)


def dockerCppMain(problem_index):
    client = docker.from_env()
    test_case_input = input_test_cases(problem_index)
    test_case_output = output_test_cases(problem_index)

    try:
        # cont = client.containers.get('cpp-container')
        # cont_state = cont.attrs['state']
        # if cont_state['status'] != 'running':
        subprocess.run('docker start cpp-container', shell=True)
    except docker.errors.NotFound:
        subprocess.run('docker run -dt --name cpp-container gcc', shell=True)

    subprocess.run(
        ['docker', 'cp', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/CppCoderunner/cpp.cpp', 'cpp-container:/a.cpp'])
    compile = subprocess.run('docker exec cpp-container g++ -o out a.cpp',
                             shell=True, capture_output=True)
    if compile.returncode != 0:
        # if doesFileExist('cpp-container:/home/a.out'):
        return -1
    else:
        run = subprocess.run('docker exec -i cpp-container ./out',
                             input=test_case_input, capture_output=True, text=True, shell=True)
        subprocess.run(['docker', 'exec', 'rm', 'out'], shell=True)
        subprocess.run(['docker', 'exec', 'rm', 'a.cpp'], shell=True)
        if run.stdout == test_case_output:
            return 1
        elif run.stdout != test_case_output:
            return 0
        elif run.stderr != '':
            return -1


def cppMain(problem_index):

    # subprocess.run(['docker', 'run', '-it', 'gcc'])
    # containerID = subprocess.Popen(['docker', 'ps', '-q', '--latest'])
    # source_path = (containerID+':'+'/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/onlinejudge/oj/Cppcoderunner')
    # subprocess.Popen(['docker', 'cp', source_path, '/home/'])
    subprocess.run(
        ['g++', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/CppCoderunner/cpp.cpp', '-o', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/CppCoderunner/a.out'])
    if doesFileExist('/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/CppCoderunner/a.out'):
        test_case_input = input_test_cases(problem_index)
        test_case_output = output_test_cases(problem_index)
        result = subprocess.run(
            '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/CppCoderunner/a.out', capture_output=True, text=True, input=test_case_input).stdout
        subprocess.run(
            ['rm', '/Users/tejaslolage/Documents/Programming/Projects/OnlineJudgeProject/OnlineJudge/OJ/CppCoderunner/a.out'])
        if test_case_output == result:
            return 1
        else:
            return 0
    else:
        return -1
