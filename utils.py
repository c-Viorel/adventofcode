import os
import pathlib
import sys


def _split_line(line, delimiter):
    if delimiter == '':
        return list(line)
    elif delimiter is None:
        return [line]
    return line.split(delimiter)


def get_input(problem_file, test=False, delimiter=',', cast=int):
    problem_path = pathlib.Path(problem_file).resolve()
    problem_number = problem_path.stem
    test_prefix = '_test' if test else ''
    input_file_name = f'{problem_number}{test_prefix}.txt'

    with open(os.path.join(problem_path.parent, 'inputs', input_file_name), 'r') as f:
        lines = f.read().strip().split('\n')

    return [
        [cast(x) for x in _split_line(line, delimiter)]
        for line in lines
    ]
