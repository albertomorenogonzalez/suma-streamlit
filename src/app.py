import streamlit as st

st.title('Suma tres números')

st.write('## Usando `st.number_input`')

n1 = st.number_input('Primer Sumando:', step=1)
n2 = st.number_input('Segundo Sumando:', step=1)
n3 = st.number_input('Tercer Sumando:', step=1)

st.write('La suma de los tres números es', n1 + n2 + n3)

st.write('## Usando `st.slider`')

st.divider()

n1 = st.slider('Primer Sumando:')
n2 = st.slider('Segundo Sumando:')
n3 = st.slider('Tercer Sumando:')

st.write('La suma de los tres números es', n1 + n2 + n3)