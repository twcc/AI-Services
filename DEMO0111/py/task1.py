import subprocess
import os
from terminaltables import AsciiTable

try_info = dict()
task1 = dict()
num_gpu = [1,2]
num_batch = [32,64,128]
fake_row = []
table_data = [['#_GPU', '#_Batch','Img/Sec']]

p = os.getcwd()

for i in num_gpu:
    for j in num_batch:
        print('G{}B{}'.format(i,j))
        a = subprocess.check_output("python {}/benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --num_gpus={} --batch_size={} --model=resnet50 --variable_update=parameter_server".format(p,i,j),shell=True)
        b = a.decode("utf-8")
        c = b.split('\n')[-3]
        #task1['G{}B{}'.format(i,j)]=c 
        fake_row = [i,j,c]
        table_data.append(fake_row)
        

table = AsciiTable(table_data)
print (table.table)

