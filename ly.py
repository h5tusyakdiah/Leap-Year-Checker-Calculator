import streamlit as st

st.markdown("<h3 style='text-align: center;'>Leap Year Checker Calculator </h3>", unsafe_allow_html=True)


year = st.number_input("Which year do you want to check? ",value =0,min_value=0)
hitung = st.button("Check")

if hitung:
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0:
                st.info(f"Leap Year")
            else:
                st.success(f"Not leap lear")
        else:
            st.info(f"Leap year")
    else:
        st.success(f"Not leap year")