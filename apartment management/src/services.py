import streamlit as st
import pandas as pd
from database import add_service,view_all_services,get_service,edit_service,drop_service

def create_service():
    sid=st.text_input("Service ID:")
    cost=st.number_input("Cost:",step=50)
    _type=st.text_input("Type:")

    if st.button("Add service"):
        add_service(sid,cost,_type)
        st.success("Added service successfully")

def show_services():
    result=view_all_services()
    df=pd.DataFrame(result,columns=["serviceID","cost","type"],dtype=str)
    st.table(df)

def update_service():
    result=view_all_services()
    df=pd.DataFrame(result,columns=["serviceID","cost","type"],dtype=str)
    with st.expander("Current services:"):
        st.table(df)
    
    list_services=[i for i in df['serviceID']]
    selected_service=st.selectbox("Select service to edit:",list_services)
    selected_result=get_service(selected_service)

    if selected_result:
        sid=selected_result[0][0]
        cost=int(selected_result[0][1])
        _type=selected_result[0][2]

        with st.expander("Edit service:"):
            new_sid=st.text_input("Service ID:",sid)
            new_cost=st.number_input("Cost:",cost,step=50)
            new_type=st.text_input("Type:",_type)

            if st.button("Update service"):
                edit_service(new_sid, new_cost, new_type,sid)
                st.success("Updated service details successfully")

def delete_service():
    result=view_all_services()
    df=pd.DataFrame(result,columns=["serviceID","cost","type"])
    with st.expander("Current services:"):
        st.table(df)

    list_services=[i for i in df['serviceID']]
    selected_service=st.selectbox("Select service to delete:",list_services)
    st.warning(f"Do you want to delete service {selected_service}?")

    if st.button("Delete service"):
        drop_service(selected_service)
        st.success("Deleted the service succesfully")