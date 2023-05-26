import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('Titulo :thinking_face:')
    st.write('Mensajito.')

    boton = st.button('Mensaje de apretar')

    st.write(boton)

    df = load_data()
    st.write(df)

    st.markdown('---')
    st.table(df)

    plot_serie_tiempo(df, "Uso de agua no relacionado con la tierra en Chile")
    plot_serie_tiempo(df, "Non Land Water Use in Chile")

  


def plot_serie_tiempo(df: pd.DataFrame, title: str) -> None:
    fig1 = px.line(df, x='Years', y='NLU', title=title, labels={'Years':'Años', 'NLU' : 'Uso de agua [m³/s]'})
    # cambiai eje x
    # titulo
    #blabla
    st.plotly_chart(fig1)


#@decoradores
@st.cache_data #le dice a streamlit que solo lo lea la primera vez y despu{es lo guarde en memoria}
def load_data():
    df = pd.read_csv('NLU_nation.csv')
    return df 


main()
