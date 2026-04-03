import streamlit as st
from auth import create_user_table, register_user, login_user

# Page configuration
st.set_page_config(page_title="Login", layout="wide")

# ---- HIDE SIDEBAR (ADD THIS HERE) ----
st.markdown("""
<style>

/* Hide sidebar completely */
section[data-testid="stSidebar"] {display:none;}

/* Hide sidebar toggle button */
button[kind="header"] {display:none;}

/* Remove sidebar navigation */
div[data-testid="stSidebarNav"] {display:none;}
            


</style>
""", unsafe_allow_html=True)




create_user_table()

st.title(" Sign In / Sign Up")

menu = ["Sign In", "Sign Up"]

choice = st.selectbox("Select Option", menu)


# -------- SIGN UP --------

if choice == "Sign Up":

    st.subheader("Create Account")

    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Register"):

        if register_user(new_user, new_password):

            st.success("Account created successfully!")

        else:

            st.error("Username already exists")


# -------- SIGN IN --------

if choice == "Sign In":

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        result = login_user(username, password)

        if result:

            st.session_state["logged_in"] = True
            st.session_state["username"] = username

            st.success("Login Successful")

            st.switch_page("pages/streamlit_app.py")

        else:

            st.error("Invalid username or password")