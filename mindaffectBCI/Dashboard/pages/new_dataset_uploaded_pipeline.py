import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from pp import pp

def app():

    dfs, column_names, columns_names2, columns_names2, path_list, time, mds = pp()

    perr = []
    perr_e = []
    se = []
    ste = []

    id = 4

    perr.append( dfs[id]['prob_err'] )
    perr_e.append (  dfs[id]['prob_err_est'] )
    se.append( dfs[id]['se'] )
    ste.append(dfs[id]['st'])

    new_perr = np.array(perr)
    new_perr_e = np.array(perr_e)
    new_se = np.array(se)
    new_st = np.array(ste)

    file = [path[2] for path in path_list]
    name = file[id]

    input = np.array([new_perr, new_perr_e, new_se, new_st]).reshape(4,30)

    source = pd.DataFrame(np.transpose(input), columns=['Perr', 'Perr_est', 'Se', 'St'])
    st.header(name)
    #line = alt.Chart(source).mark_line().encode(x='Int_len',  y='Score')
    #st.altair_chart(line)
 
    st.line_chart(source)

    perr = []
    perr_e = []
    se = []
    ste = []

    id = 13

    perr.append( dfs[id]['prob_err'] )
    perr_e.append (  dfs[id]['prob_err_est'] )
    se.append( dfs[id]['se'] )
    ste.append(dfs[id]['st'])

    new_perr = np.array(perr)
    new_perr_e = np.array(perr_e)
    new_se = np.array(se)
    new_st = np.array(ste)

    file = [path[2] for path in path_list]
    name = file[id]

    input = np.array([new_perr, new_perr_e, new_se, new_st]).reshape(4,30)

    source = pd.DataFrame(np.transpose(input), columns=['Perr', 'Perr_est', 'Se', 'St'])
    st.subheader(name)
    #line = alt.Chart(source).mark_line().encode(x='Int_len',  y='Score')
    #st.altair_chart(line)
 
    st.line_chart(source)
    


