import streamlit as st
import pandas as pd
import datetime as dt
from database import add_security,view_all_security,get_security,edit_security,drop_security,view_all_staff

def create_security():
    col1,col2=st.columns(2)

    with col1:
        sid=st.text_input("Security ID:")
        fname=st.text_input("First Name:")
        lname=st.text_input("Last Name:")
    with col2:
        phone=st.text_input("Phone Number:")
        doj=st.date_input("Date of joining:",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
        shift=st.selectbox("Shift:",["Day","Night"])
    
    if st.button("Add security"):
        add_security(sid, fname, lname, phone, doj, shift)
        st.success("Successfulyy added the security")

def show_security():
    result=view_all_security()
    df=pd.DataFrame(result,columns=["securityID","Fname","Lname","phone","doj","shift"],dtype=str)
    st.table(df)

def show_staff():
    result = view_all_staff()
    df = pd.DataFrame(result, columns=["Fname", "Lname", "phone", "shift","serviceID", "type"], dtype=str)
    st.table(df)

def update_security():
    result=view_all_security()
    df=pd.DataFrame(result,columns=["securityID","Fname","Lname","phone","doj","shift"],dtype=str)
    with st.expander("Current securities:"):
        st.table(df)


    list_security=[i for i in df['securityID']]
    selected_security=st.selectbox("Select a security to edit:",list_security)
    selected_result=get_security(selected_security)

    if selected_result:
        sid=selected_result[0][0]
        fn=selected_result[0][1]
        ln=selected_result[0][2]
        phone=selected_result[0][3]
        doj=selected_result[0][4]
        shift=selected_result[0][5]

        with st.expander("Edit security:"):
            col1,col2=st.columns(2)
            shift_sel=["Day","Night"]
            with col1:
                new_sid=st.text_input("Security ID:",sid)
                new_fname=st.text_input("First Name:",fn)
                new_lname=st.text_input("Last Name:",ln)
            with col2:
                new_phone=st.text_input("Phone Number:",phone)
                new_doj=st.date_input("Date of joining:",value=doj,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
                new_shift=st.selectbox("Shift:",["Day","Night"],index=shift_sel.index(shift))

            if st.button("Update security"):
                edit_security(new_sid, new_fname, new_lname, new_phone, new_doj, new_shift, sid)
                st.success("Updated security successfully")

def delete_security():
    result=view_all_security()
    df=pd.DataFrame(result,columns=["securityID","Fname","Lname","phone","doj","shift"],dtype=str)
    with st.expander("Current securities:"):
        st.table(df)

    list_security=[i for i in df['securityID']]
    selected_security=st.selectbox("Security to delete:",list_security)
    st.warning(f"Do you want to delete security {selected_security}?")

    if st.button("Delete security"):
        drop_security(selected_security)
        st.success("Deleted the security successfully")
