import streamlit as st
import pandas as pd
import datetime as dt
from database import add_employee,view_all_serviceids,edit_employee,view_all_employees,drop_employee,get_employee

def create_employee():
    col1,col2=st.columns(2)
    serviceids=view_all_serviceids()
    df=pd.DataFrame(serviceids,columns=["serviceid"],dtype=str)
    list_sids=[i for i in df['serviceid']]

    with col1:
        eid=st.text_input("Employee ID:")
        fname=st.text_input("First Name:")
        lname=st.text_input("Last Name:")
        phone=st.text_input("Phone Number:")
        salary=st.number_input("Salary:",step=500)
    with col2:
        doj=st.date_input("Date of joining:",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
        gender=st.selectbox("Gender:",["M","F","O"])
        shift=st.selectbox("Shift:",["Day","Night"])
        serviceid=st.selectbox("Service ID:",list_sids)
    
    if st.button("Add Employee"):
        add_employee(eid, fname, lname, phone, doj, gender, shift, serviceid, salary)
        st.success("Successfulyy added the employee")

def show_employees():
    result=view_all_employees()
    emp_og_list = ["employeeID","Fname","Lname","phone","doj","gender","shift","serviceID","salary"]
    df=pd.DataFrame(result,columns=["employeeID","Fname","phone","shift","serviceID","type","cost"],dtype=str)
    st.table(df)

def update_employee():
    result=view_all_employees()
    df=pd.DataFrame(result,columns=["employeeID","Fname","Lname","phone","doj","gender","shift","serviceID","salary"],dtype=str)

    with st.expander("Current employees:"):
        st.table(df)
    
    serviceids=view_all_serviceids()
    df2=pd.DataFrame(serviceids,columns=["serviceid"],dtype=str)
    list_sids=[i for i in df2['serviceid']]

    list_employees=[i for i in df['employeeID']]
    selected_employee=st.selectbox("Select a employee to edit:",list_employees)
    selected_result=get_employee(selected_employee)

    if selected_result:
        eid=selected_result[0][0]
        fn=selected_result[0][1]
        ln=selected_result[0][2]
        phone=selected_result[0][3]
        doj=selected_result[0][4]
        gender=selected_result[0][5]
        shift=selected_result[0][6]
        sid=selected_result[0][7]
        salary=selected_result[0][8]

        with st.expander("Edit employee:"):
            col1,col2=st.columns(2)
            gen_sel=["M","F","O"]
            shift_sel=["Day","Night"]
            with col1:
                new_eid=st.text_input("Employee ID:",eid)
                new_fname=st.text_input("First Name:",fn)
                new_lname=st.text_input("Last Name:",ln)
                new_phone=st.text_input("Phone Number:",phone)
                new_salary=st.number_input("Salary:",step=500,value=int(salary))
            with col2:
                new_doj=st.date_input("Date of joining:",value=doj,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
                new_gender=st.selectbox("Gender:",["M","F","O"],index=gen_sel.index(gender))
                new_shift=st.selectbox("Shift:",["Day","Night"],index=shift_sel.index(shift))
                new_serviceid=st.selectbox("Service ID:",list_sids,index=list_sids.index(sid))

            if st.button("Update employee"):
                edit_employee(new_eid, new_fname, new_lname, new_phone, new_doj, new_gender, new_shift, new_serviceid, new_salary, eid)
                st.success("Updated employee successfully")

def delete_employee():
    result=view_all_employees()
    df=pd.DataFrame(result,columns=["employeeID","Fname","Lname","phone","doj","gender","shift","serviceID","salary"],dtype=str)

    with st.expander("Current employees:"):
        st.table(df)

    list_employees=[i for i in df['employeeID']]
    selected_employee=st.selectbox("Employee to delete:",list_employees)
    st.warning(f"Do you want to delete employee {selected_employee}?")

    if st.button("Delete employee"):
        drop_employee(selected_employee)
        st.success("Delete the employee successfully")