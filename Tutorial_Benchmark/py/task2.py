import subprocess
import os
from terminaltables import AsciiTable

try_info = dict()
task1 = dict()
num_gpu = [1,2,4,8]
num_batch = [32]
fake_row = []
table_data = [['#_GPU', '#_Batch','Img/Sec']]

p = os.getcwd()

for i in num_gpu:
    print('G{}B32'.format(i))
    print(i)
    a = subprocess.check_output("/usr/local/mpi/bin/mpirun -np {} -H localhost:{} python {}/horovod/examples/tensorflow_synthetic_benchmark.py".format(i,i,p),shell=True)
    b = a.decode("utf-8")
    c = b.split('\n')[-2]
    task1['G{}B32'.format(i)]=c 
    fake_row = [i,'32',c]
    table_data.append(fake_row)
      

table = AsciiTable(table_data)
print (table.table)

