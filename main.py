import pandas as pd
import streamlit as st

if __name__ == "__main__":
    st.set_page_config(page_title="Nunca nunca")
    st.title('Nunca nunca')
    df = pd.read_csv('bd.csv')

    n = st.number_input("Ingresa el número de fila que quieres ver", min_value=0, max_value=len(df), step=1
                        )
    if n!=0:
        st.balloons()
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown(f'<p class="big-font">{df.iloc[n-1,1]}</p>', unsafe_allow_html=True)
        # st.write(, style={'fontSize':'48pt'})
