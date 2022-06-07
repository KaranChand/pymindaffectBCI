import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from pp import pp

def app():
    st.header("Performance tracking")

    # df = pd.DataFrame([[20.500, 15.513, 90.667], [57.833, 23.077, 34.667],[46.000, 32.436, 30.333],[36.667, 20.256, 25.222],[46.000, 28.718, 33.456]], columns=['kaggle', 'plos_one', 'lowlands'])
    # df.index.name = "Dataset-ID"
    # df.set_index([pd.Index([1, 2, 3, 4,5])])
    # data = df.reset_index().melt('Dataset-ID')
    # c = alt.Chart(data).mark_line().encode(
    #     x='Dataset-ID',
    #     y='value',
    #     color='variable'
    # )
    #test

    dfs, column_names, columns_names2, columns_names2, path_list, time, mds = pp()

    avg_k_audc = []
    avg_l_audc = []
    avg_p_audc = []

    for i in range(0, len(dfs), 18):
        avg_k_audc.append( dfs[i]['ave-AUDC'] )
        avg_l_audc.append (  dfs[i+1]['ave-AUDC'] )
        avg_p_audc.append( dfs[i+3]['ave-AUDC'] )

    new_k_audc = np.array(avg_k_audc)
    new_l_audc = np.array(avg_l_audc)
    new_p_audc = np.array(avg_p_audc)

    input = np.array([new_k_audc[:,0], new_l_audc[:,0], new_p_audc[:,0]])

    source = pd.DataFrame(np.transpose(input),
                          columns=['Kaggle', 'Lowlands', 'Plos_one'], index=pd.RangeIndex(1, len(avg_k_audc)+1, name='Commit-ID'))
    source = source.reset_index().melt('Commit-ID', var_name='dataset', value_name='avg-AUDC')
    line = alt.Chart(source).mark_line(interpolate='basis').encode(
        x='Commit-ID:Q',
        y='avg-AUDC:Q',
        color='dataset:N'
    ).properties(
    title='Average AUDC across commits'
)
    st.altair_chart(line, use_container_width=True)

    #source = source.reset_index().melt('Commit-ID', var_name='dataset', value_name='avg-AUDC')
    #line = alt.Chart(source).mark_line(interpolate='basis').encode(
    #   x='Commit-ID',
    #    y='avg-AUDC',
    #).properties(
    #title='Average AUDC across commits'
#)
    #st.altair_chart(line, use_container_width=True)
    # col1, col2 = st.columns(2)


    branch = []
    #time = []

    for i in mds:
        branch.append(i['branch'])
        #time.append(i['current_date_and_time'])

    sha = np.unique(np.array(time))

    col1, col2 = st.columns([2, 1])
    col1.write(pd.DataFrame({'Commit-ID': range(1, len(sha)+1),
        'SHA': sha
    }))
    # col1.write(pd.DataFrame({'Data source': ['Kaggle', 'Plos_one', 'Lowlands'],
    #     'Dataset name': ['mindaffectBCI_noisetag_bci_201029_1340_ganglion.txt','Perr_plos_one_supervised_...','LL_eng_02_20170818_tr_train_1.mat']
    # }))

    #unique_branches = np.unique(np.array(branch))

    #count_branch = []

    #for br in unique_branches:
        #count_branch.append(branch.count(br))
    
    # col1, col2 = st.columns(2)
    # chart_data = pd.DataFrame(
    #     np.array([[1, 2, 3], [4, 5, 6],[4, 5, 6]]),
    #     columns=['open_source', 'master', 'wip'])
    #
    # col1.line_chart(chart_data)
    # #col2.chart_data.
    #
    # col2.write(pd.DataFrame({
    #     'first column': [1, 2, 3, 4],
    #     'second column': [10, 20, 30, 40]
    # }))
    #
    # col3, col4 = st.columns(2)
    # chart_data2 = pd.DataFrame(
    #     np.array([[20.500, 15.513, 90.667], [57.833, 23.077, 34.667],[46.000, 32.436, 30.333],[36.667, 20.256, 25.222],[46.000, 28.718, 33.456]]),
    #     columns=['kaggle', 'plos_one', 'lowlands'])
    #
    # # col3.line_chart(chart_data2)
    #
    # line_chart = alt.Chart(chart_data2).mark_line(interpolate='basis').encode(
    # alt.X('x', title='Year'),
    # alt.Y('y', title='Amount in liters'),
    # color='category:N'
    # ).properties(
    # title='Sales of consumer goods'
    # )
    #
    # st.altair_chart(line_chart)
