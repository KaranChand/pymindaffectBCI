import csv
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

list_csv = glob.glob('csv/**/*.csv')

dfs = []

path_list = []

for path in list_csv:
    path_list.append(path.split(os.sep))

time = [path[1] for path in path_list]
file = [path[2] for path in path_list]

for i in (list_csv):
    df = pd.read_csv(i)
    dfs.append(df)

column_names = dfs[0].columns.tolist()
column_names2 = dfs[4].columns.tolist()

list_csv2 = glob.glob('csv/**/metadata.csv')

mds = []

for i in (list_csv2):
    md = pd.read_csv(i, index_col=False)
    mds.append(md)

column_names3 = mds[0].columns.tolist()

k_audc = []
l_audc = []
p_audc = []

s = dfs[0]['AUDC']
g = dfs[1]['AUDC']
f = dfs[18]['AUDC']

sha = []
cm_id = []
branch = []

for count, md in enumerate(mds):
    sha.append(md['sha'])
    branch.append(md['branch'])
    cm_id.append(count)

#for i in range(0, len(dfs), 18):
    #print(i)
    #print(dfs[i]['AUDC'])

j = 18

avg_k_audc = []
avg_l_audc = []
avg_p_audc = []


for i in range(0, len(dfs)):
    id_k = file.index('kaggle.csv')
    id_l = file.index('lowlands.csv')
    id_p = file.index('plos_one.csv')

for i in range(0, len(dfs), 18):
    avg_k_audc.append(dfs[id_k]['ave-AUDC'])
    avg_l_audc.append(dfs[id_l]['ave-AUDC'])
    avg_p_audc.append(dfs[id_p]['ave-AUDC'])

new_k_audc = np.array(avg_k_audc)
new_l_audc = np.array(avg_l_audc)
new_p_audc = np.array(avg_p_audc)

input = np.array([new_k_audc[:,0], new_l_audc[:,0], new_p_audc[:,0]])

print(input)

perr = []
perr_e = []
se = []
st = []

id = 4

perr.append( dfs[id]['prob_err'] )
perr_e.append (  dfs[id]['prob_err_est'] )
se.append( dfs[id]['se'] )
st.append(dfs[id]['st'])

new_perr = np.array(perr)
new_perr_e = np.array(perr_e)
new_se = np.array(se)
new_st = np.array(st)

file = [path[2] for path in path_list]
name = file[id]

input = np.array([new_perr, new_perr_e, new_se, new_st]).reshape(4,30)
#print(np.random.randn(20, 3))
f = np.transpose(input)
print(f)
print(f.shape)

#print(input)
#print(file)
#print(dfs[0])
#print(dfs['_LL_eng_02_20170818_tr_train_1_mat'])
#print(np.transpose(input))
#print(new_k_audc)
#print(np.transpose(input))

#print(len(dfs))
#print(dfs[0]['AUDC'])
#print(dfs[1]['AUDC'])
#print(dfs[3]['AUDC'])
#print(dfs[j]['AUDC'])
#print(dfs[19])
#print(dfs[21])

#print(mds[0]['branch'])
#print(sha)
#print(cm_id)
#print(branch)

#print(column_names3)
#print(dfs[0]['AUDC'])
#print(mds[0]['current_date_and_time'])
#print(column_names)
#print(column_names2)
#print(path_list)
#print(len(time))
#print(time)
#print(path_list)
#print(dfs[4].columns.tolist())


#file = column_names[0]
#clsfr = column_names[1]
#audc = column_names[2]
#ave_audc = column_names[3]
#bsl_audc = column_names[4]

#kaggle = dfs[0]
#lowlands = dfs[1]
#plos_one = dfs[2]

#k_audc = kaggle['AUDC']
#l_audc = lowlands['AUDC']
#p_audc = plos_one['AUDC']

#print(dfs[0]['AUDC'])

#source = pd.DataFrame([[20.500, 15.513, 50.667], [57.833, 23.077, 60.667],[46.000, 55.436, 70.333],[36.667, 60.256, 80.222],[55.000, 85.718, 90.456]],
                          #columns=['Kaggle', 'Plos_one', 'Lowlands'], index=pd.RangeIndex(5, name='Commit-ID'))

#print(source)

#source2 = source.reset_index().melt('Commit-ID', var_name='dataset', value_name=audc)

#print(source2)

#for i in range(len(dfs)):
    #print(dfs[i])

#print(dfs[0]["AUDC"])

#print(np.random.randn(20, 3))