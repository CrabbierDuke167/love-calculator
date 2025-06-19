import streamlit as st

st.title("💘LOVE CALCULATOR <3💘")

starting_messages = '''Welcome to my own hand made, CALCULATOR o\' LOVE

how to use it? - just input your name and the one's name whom you want to check :)

BREAK A LEG>>>'''

st.success(starting_messages)

user_name = st.text_input("Enter your name: ").lower().strip()
crush_name = st.text_input("Enter the name of that special person: ").lower().strip()

common = set(user_name) & set(crush_name)
common_digits = len(common)
total_digits = len(user_name) + len(crush_name)

love_score = (common_digits / total_digits) * 100 + common_digits * 7

if love_score < 50:
    message = ("Oops FRIEND-ZONED 😬")
elif love_score == 50:
    message = ("You might stand a chance , Fr👀")
elif 50 < love_score < 90:
    message = ("Trust The Process...❤️‍🔥")
elif love_score > 90:
    message = ("MADE FOR EACH OTHER <3❤️‍🔥")
else:
    st.error("An unexpected error occured, please restart <3")

output = (f"Your Love Score is - {love_score} ---{message}---")
st.subheader(output)

