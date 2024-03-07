import streamlit as st

dict1={'shamikakadam@gmail.com':456,'divyashelke@gmail.com':123,'ishamathkar@gmail.com':789}

email=st.text_input('Enter email:')
pass1=st.number_input('Enter password:')
btn=st.button('Login')

if btn:
    if email in dict1:
        if pass1==dict1[email]:
            st.snow()
            st.success('SUCCESSFULLY LOGGED IN!', icon="✅")

        else:
            
            st.success('FAILED', icon="❌")



