import streamlit as st
import pandas as pd
from database import add_fhs,view_all_fhs,get_fhs,edit_fhs,drop_fhs,view_all_flats,view_all_security

def flatids():
    result=view_all_flats()
    df=pd.DataFrame(result,columns=["FlatID","no_bhk"])
    list_flatids=[i for i in df['FlatID']]
    return list_flatids
def securityids():
    result=view_all_security()
    df=pd.DataFrame(result,columns=["securityID","Fname","Lname","phone","doj","shift"],dtype=str)
    list_securities=[i for i in df['securityID']]
    return list_securities

def create_fhs():
    list_flatids=flatids()
    list_securities=securityids()

    fid=st.selectbox("Flat ID:",list_flatids)
    sid=st.selectbox("Security ID:",list_securities)

    if st.button("Add flat has security"):
        add_fhs(fid, sid)
        st.success("Added flat has security successfully")

def show_fhs():
    result=view_all_fhs()
    df=pd.DataFrame(result,columns=["FlatID","Block_No","securityID","name","shift"],dtype=str)
    st.table(df)

def update_fhs():
    result=view_all_fhs()
    df=pd.DataFrame(result,columns=["FlatID","Block_No","securityID","Name","shift"],dtype=str)
    with st.expander("Current flat has security:"):
        st.table(df)
    
    list_flatids=flatids()
    list_securities=securityids()
    list_fhs=[i for i in df['FlatID']]
    selected_fhs=st.selectbox("Select a flat has security to edit:",list_fhs)
    selected_result=get_fhs(selected_fhs)

    if selected_result:
        fid=selected_result[0][0]
        sid=selected_result[0][1]

        with st.expander("Edit flat has security:"):
            new_fid=st.selectbox("Flat ID:",list_flatids,index=list_flatids.index(fid))
            new_sid=st.selectbox("Security ID:",list_securities,index=list_securities.index(sid))

            if st.button("Update flat has security:"):
                edit_fhs(new_fid, new_sid, fid)
                st.success("Updated the flat has security successfully")

def delete_fhs():
    result=view_all_fhs()
    df=pd.DataFrame(result,columns=["FlatID","Block_No","securityID","Name","shift"],dtype=str)
    with st.expander("Current flat has security:"):
        st.table(df)
    
    list_flatids=flatids()
    list_securities=securityids()
    list_fhs=[i for i in df['FlatID']]
    selected_fhs=st.selectbox("Select a flat has security to delete:",list_fhs)
    st.warning(f"Do you want to delete flat {selected_fhs} with security?")

    if st.button("Delete flat has security:"):
        drop_fhs(selected_fhs)
        st.success("Deleted the flat has security successfully")