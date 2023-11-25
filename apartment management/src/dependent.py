import streamlit as st
import pandas as pd
import datetime as dt
from database import view_all_residentids,add_dependent,view_all_dependents,get_dependent,edit_dependent,drop_dependent,view_all_dependents_resident

def create_dependent():
    col1,col2=st.columns(2)
    residentids=view_all_residentids()
    df=pd.DataFrame(residentids,columns=["ResidentUID"],dtype=str)
    list_rids=[i for i in df['ResidentUID']]
    
    with col1:
        aadhar=st.text_input("Aadhar:")
        residentUID=st.selectbox("Resident UID:",list_rids)
        fname=st.text_input("First Name:")
        lname=st.text_input("Last Name:")
    with col2:
        dob=st.date_input("Date Of Birth",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
        phone=st.text_input("Phone Number:")
        gender=st.selectbox("Gender",["M","F","O"])

    if st.button("Add dependent"):
        add_dependent(aadhar,residentUID,fname,lname,dob,phone,gender)
        st.success("Successfully added the complaint")

def show_dependents():
    result=view_all_dependents()
    df=pd.DataFrame(result,columns=["Aadhar","ResidentUID","Fname","Lname","DOB","phone","gender"],dtype=str)
    st.table(df)

def update_dependent():
    result=view_all_dependents()
    df=pd.DataFrame(result,columns=["Aadhar","ResidentUID","Fname","Lname","DOB","phone","gender"],dtype=str)
    
    residentids=view_all_residentids()
    df2=pd.DataFrame(residentids,columns=["ResidentUID"],dtype=str)
    list_rids=[i for i in df2['ResidentUID']]

    with st.expander("Current dependents:"):
        st.table(df)
    list_of_dependents=[i for i in df['Aadhar']]
    selected_dependent=st.selectbox("Select a dependent to edit:",list_of_dependents)
    selected_result=get_dependent(selected_dependent)

    if selected_result:
        aadhar=selected_result[0][0]
        residentuid=selected_result[0][1]
        fname=selected_result[0][2]
        lname=selected_result[0][3]
        dob=selected_result[0][4]
        phone=selected_result[0][5]
        gender=selected_result[0][6]
        

        with st.expander("Edit complaint:"):
            gen_select=["M","F","O"]
            col1,col2=st.columns(2)
            with col1:
                new_aadhar=st.text_input("Aadhar:",aadhar)
                new_residentUID=st.selectbox("Resident UID:",list_rids,index=list_rids.index(residentuid))
                new_fname=st.text_input("First Name:",fname)
                new_lname=st.text_input("Last Name:",lname)
            with col2:
                new_dob=st.date_input("Date Of Birth",value=dob,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
                new_phone=st.text_input("Phone Number:",phone)
                new_gender=st.selectbox("Gender",gen_select,index=gen_select.index(gender))

            if st.button("Update dependent"):
                edit_dependent(new_aadhar,new_residentUID,new_fname,new_lname,new_dob,new_phone,new_gender,aadhar)
                st.success("Successfully updated the dependent")

def delete_dependent():
    result=view_all_dependents()
    df=pd.DataFrame(result,columns=["Aadhar","ResidentUID","Fname","Lname","DOB","phone","gender"],dtype=str)
    with st.expander("Current dependents:"):
        st.table(df)
    list_of_dependents=[i for i in df['Aadhar']]
    selected_dependent=st.selectbox("Dependent to delete:",list_of_dependents)
    st.warning(f"Do you want to delete dependent {selected_dependent}?")
    if st.button("Delete dependent"):
        drop_dependent(selected_dependent)
        st.success("Dependent deleted successfully")


def create_dependent_resident(username):
    col1,col2=st.columns(2)
    residentids=view_all_residentids()
    df=pd.DataFrame(residentids,columns=["ResidentUID"],dtype=str)
    list_rids=[username]
    
    with col1:
        aadhar=st.text_input("Aadhar:")
        residentUID=st.selectbox("Resident UID:",list_rids)
        fname=st.text_input("First Name:")
        lname=st.text_input("Last Name:")
    with col2:
        dob=st.date_input("Date Of Birth",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
        phone=st.text_input("Phone Number:")
        gender=st.selectbox("Gender",["M","F","O"])

    if st.button("Add dependent"):
        add_dependent(aadhar,residentUID,fname,lname,dob,phone,gender)
        st.success("Successfully added the complaint")

def show_dependents_resident(username):
    result=view_all_dependents_resident(username)
    df=pd.DataFrame(result,columns=["Aadhar","ResidentUID","Fname","Lname","DOB","phone","gender"],dtype=str)
    st.table(df)

def update_dependent_resident(username):
    result=view_all_dependents_resident(username)
    df=pd.DataFrame(result,columns=["Aadhar","ResidentUID","Fname","Lname","DOB","phone","gender"],dtype=str)
    
    list_rids=[username]

    with st.expander("Current dependents:"):
        st.table(df)
    
    list_of_dependents = df.loc[df['ResidentUID'] == username, 'Aadhar'].tolist()
    selected_dependent=st.selectbox("Select a dependent to edit:",list_of_dependents)
    selected_result=get_dependent(selected_dependent)

    if selected_result:
        aadhar=selected_result[0][0]
        residentuid=selected_result[0][1]
        fname=selected_result[0][2]
        lname=selected_result[0][3]
        dob=selected_result[0][4]
        phone=selected_result[0][5]
        gender=selected_result[0][6]
        

        with st.expander("Edit complaint:"):
            gen_select=["M","F","O"]
            col1,col2=st.columns(2)
            with col1:
                new_aadhar=st.selectbox("Aadhar:",[aadhar])
                new_residentUID=st.selectbox("Resident UID:",list_rids,index=list_rids.index(residentuid))
                new_fname=st.text_input("First Name:",fname)
                new_lname=st.text_input("Last Name:",lname)
            with col2:
                new_dob=st.date_input("Date Of Birth",value=dob,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
                new_phone=st.text_input("Phone Number:",phone)
                new_gender=st.selectbox("Gender",gen_select,index=gen_select.index(gender))

            if st.button("Update dependent"):
                edit_dependent(new_aadhar,new_residentUID,new_fname,new_lname,new_dob,new_phone,new_gender,aadhar)
                st.success("Successfully updated the dependent")

def delete_dependent_resident(username):
    result=view_all_dependents_resident(username)
    df=pd.DataFrame(result,columns=["Aadhar","ResidentUID","Fname","Lname","DOB","phone","gender"],dtype=str)
    with st.expander("Current dependents:"):
        st.table(df)
    list_of_dependents = df.loc[df['ResidentUID'] == username, 'Aadhar'].tolist()
    selected_dependent=st.selectbox("Dependent to delete:",list_of_dependents)
    st.warning(f"Do you want to delete dependent {selected_dependent}?")
    if st.button("Delete dependent"):
        drop_dependent(selected_dependent)
        st.success("Dependent deleted successfully")






