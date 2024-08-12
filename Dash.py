import streamlit as st
from pandas import read_csv

st.title('Dashborad automatic')

file = st.file_uploader(
    'Suba seu Arquivo Aqui ! ',
    type = ['csv']
)

if file:
    if file.type == 'txt/csv':
        df = read_csv(file)
        st.line_chart(df.set_index('mês'))
        st.bar_chart(df.set_index('mês'))
    else:
        st.error('Formato De Arquivo não Suportado ! ')
else:
    st.warning('Ainda não Tenho o Arquivo! ')
