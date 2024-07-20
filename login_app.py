import streamlit as st

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.username = username
            st.session_state.logged_in = True
            st.session_state.is_admin = True  # Set admin privilege
            st.success("Login successful! Redirecting to dashboard...")
            st.experimental_rerun()
        elif username == "user" and password == "user123":
            st.session_state.username = username
            st.session_state.logged_in = True
            st.session_state.is_admin = False  # Set user privilege
            st.success("Login successful! Redirecting to dashboard...")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    login_page()
