import streamlit as st
import random 

#STREAMLIT BASE CODE

st.set_page_config(page_title="Coumputer Guessing",page_icon="D:\Streamlit\Pages\zoro_logo.png")
st.title("Coumputer guessing a number")
st.header("Rules:")
st.write("1. Think a number from 1 to 100.")
st.write("2. Enter whether the guessed number is correct.")
st.write("3. If not, select whether the guessed number is greater than or less than the number you think.")

#SESSION_STATE

if "low" not in st.session_state:
    st.session_state.low=1
    st.session_state.high=100

st.session_state.guess_num=(st.session_state.high+st.session_state.low)//2

#BINARY SEARCH
st.header("Let's start")
st.subheader("Think a number between 1 to 100")
choice=st.selectbox(f"Is the number is {st.session_state.guess_num}",("Yes","Guess is greater than my number","Guess is less than my number"))
if choice=="Yes":
    select=st.button("select")
    if select:
        st.success(f"So the number is {st.session_state.guess_num}")
        st.snow()
        play_again=st.button("Play again")
        if play_again:
            st.rerun()
elif choice=="Guess is greater than my number":
    st.session_state.high=st.session_state.guess_num
    st.button("Select")
elif choice=="Guess is less than my number":
    st.session_state.low=st.session_state.guess_num
    st.button("Select")