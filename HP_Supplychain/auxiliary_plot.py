import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import pickle
import seaborn as sns
import matplotlib.pyplot as plt


#plot planning graphic
def plot_planning_graphic(start_date, end_date,x, dictionary_plots, num_prod):
    sns.set_theme(style="darkgrid")
    i_t = dictionary_plots[num_prod][0]
    s_t = dictionary_plots[num_prod][1]
    qt  = dictionary_plots[num_prod][2]
    
    sd = dt.datetime.combine(start_date, dt.time(0, 0))
    ed = dt.datetime.combine(end_date, dt.time(0, 0))
    index_ini = np.searchsorted(x, sd, side = 'right')
    index_end = np.searchsorted(x, ed, side = 'left')

    i_t = i_t[index_ini:index_end]
    s_t = s_t[index_ini:index_end]
    qt = qt[index_ini:index_end]
    x2 = x[index_ini:index_end]

    sns.lineplot(x = x2, y = i_t, label='Inventory')
    sns.lineplot(x = x2, y = s_t, label='Sales')
    ax = sns.lineplot(x = x2, y = qt, label='Planning')
    plt.tick_params(axis='x', labelrotation=60)
    ax.set(xlabel='Date', ylabel='Units')
    plt.legend(title='Inventory planning', loc='upper left')
    st.pyplot(plt)

    return x2, i_t, s_t, qt


def download_data_plot(x, i_t, s_t, qt):
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv',
    )
