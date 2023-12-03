import os
import pathlib

from source.Clause import Clause
from source.KB import KnowledgeBase
from source.PL_Resolution import PL_Resolution

current_dir = pathlib.Path(__file__).parent.resolve()
input_dir = current_dir.joinpath('INPUT')
output_dir = current_dir.joinpath('OUTPUT')

input_file_list = os.listdir(input_dir)
num_input_file = len(input_file_list)

for i in range(num_input_file):
    input_filename = 'input_' + str(i) + '.txt'
    input_filedir = input_dir.joinpath(input_filename)
    with open(input_filedir, 'r') as fin:
        str_alpha = fin.readline()
        alpha = Clause.convert_str_to_clause(str_alpha)

        number_clauses = int(fin.readline())

        string_clause_list = fin.readlines()
        KB = KnowledgeBase.convert_str_list_to_KB(string_clause_list)
    fin.close()

    clause_list, entails_result = PL_Resolution(KB, alpha)

    output_filename = 'output_' + str(i) + '.txt'
    output_filedir = output_dir.joinpath(output_filename)
    with open(output_filedir, 'w') as fout:
        for clause_of_step in clause_list:
            fout.write('{}\n'.format(len(clause_of_step)))

            for clause in clause_of_step:
                fout.write('{}\n'.format(clause))

        if entails_result:
            fout.write('YES')
        else:
            fout.write('NO')
    fout.close()
