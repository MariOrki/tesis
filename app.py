import streamlit as st
import pandas as pd

def main():
    st.title('Titulo :thinking_face:')
    st.write('Mensajito.')

    boton = st.button('Mensaje de apretar')

    st.write(boton)

    df = load_data()
    st.write(df)

    st.markdown('---')
    st.table(df)




def load_data():
    df = pd.read_csv('NLU_nation.csv')
    return df 


main()