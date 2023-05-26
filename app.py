import streamlit as st
import pandas as pd

def main():
    st.title('Titulo :thinking_face:')
    st.write('Mensajito.')

    boton = st.button('Mensaje de apretar')

    st.write(boton)

    st.balloons()



def load_data():
    df = pd.read_csv('NLU_nation.csv')
    return df 


main()