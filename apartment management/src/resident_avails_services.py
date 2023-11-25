import streamlit as st
import pandas as pd
import datetime as dt
from database import view_all_residentids,view_all_serviceids,add_ras,view_all_ras,get_ras,edit_ras,drop_ras,view_all_ras_resident,get_residents_with_service

#nested_query#####################################################################
def get_residents():
    list_services=serviceids()
    service_id=st.selectbox("Enter Service ID:",list_services)
    result = get_residents_with_service(service_id)
    df=pd.DataFrame(result,columns=["Uid","Fname","Lname","gender","phone","FlatID","rent/owned"],dtype=str)
    st.table(df)

def residentids():
    result=view_all_residentids()
    df=pd.DataFrame(result,columns=["Aadhar"])
    list_residents=[i for i in df['Aadhar']]
    return list_residents
def serviceids():
    result=view_all_serviceids()
    df=pd.DataFrame(result,columns=["serviceID"])
    list_services=[i for i in df['serviceID']]
    return list_services

def create_ras():
    list_residents=residentids()
    list_services=serviceids()

    rid=st.selectbox("Resident ID:",list_residents)
    sid=st.selectbox("Service ID:",list_services)
    date=st.date_input("Date:",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
    time=st.time_input("Time:")

    dts=str(date)+" "+str(time)

    if st.button("Add resident avails service"):
        add_ras(rid, sid, dts)
        st.success("Added resident avails service successfully")

def show_ras():
    result=view_all_ras()
    df=pd.DataFrame(result,columns=["ResidentUID","serviceID","ServiceTime"],dtype=str)
    st.table(df)

def update_ras():
    result=view_all_ras()
    df=pd.DataFrame(result,columns=["ResidentUID","serviceID","ServiceTime"],dtype=str)
    with st.expander("Current resident avails services:"):
        st.table(df)
    
    list_residents=residentids()
    list_services=serviceids()

    list_rid=[i for i in df['ResidentUID']]
    list_sid=[i for i in df['serviceID']]
    list_ras=[]
    for i in range(len(list_rid)):
        list_ras.append(f"{list_rid[i]}-{list_sid[i]}")

    selected_ras=st.selectbox("Select a resident availed service to edit:",list_ras)
    selected_result=get_ras(selected_ras.split('-')[0], selected_ras.split('-')[1])

    if selected_result:
        rid=selected_result[0][0]
        sid=selected_result[0][1]
        dts=str(selected_result[0][2])
        date=dt.date(int(dts.split(" ")[0].split('-')[0]),int(dts.split(" ")[0].split('-')[1]),int(dts.split(" ")[0].split('-')[2]))
        time=dt.time(int(dts.split(" ")[1].split(':')[0]),int(dts.split(" ")[1].split(':')[1]),int(dts.split(" ")[1].split(':')[2]))

        with st.expander("Edit resident availed service:"):
            new_rid=st.selectbox("Resident ID:",list_residents,index=list_residents.index(rid))
            new_sid=st.selectbox("Service ID:",list_services,index=list_services.index(sid))
            new_date=st.date_input("Date:",value=date,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
            new_time=st.time_input("Time:",time)

            new_dts=str(new_date)+" "+str(new_time)

            if st.button("Update resident availed service:"):
                edit_ras(new_rid, new_sid, new_dts, rid, sid)
                st.success("Updated the resident availed service successfully")

def delete_ras():
    result=view_all_ras()
    df=pd.DataFrame(result,columns=["ResidentUID","serviceID","ServiceTime"],dtype=str)
    with st.expander("Current resident avails services:"):
        st.table(df)
    
    list_residents=residentids()
    list_services=serviceids()

    list_rid=[i for i in df['ResidentUID']]
    list_sid=[i for i in df['serviceID']]
    list_ras=[]
    for i in range(len(list_rid)):
        list_ras.append(f"{list_rid[i]}-{list_sid[i]}")

    selected_ras=st.selectbox("Select a resident availed service to delete:",list_ras)
    st.warning(f"Do you want to delete resident availed service {selected_ras}?")

    if st.button("Delete resident availed service"):
        drop_ras(selected_ras.split('-')[0], selected_ras.split('-')[1])
        st.success("Deleted the resident successfully")


def create_ras_resident(username):
    list_residents=residentids()
    list_services=serviceids()

    rid=st.selectbox("Resident ID:",[username])
    sid=st.selectbox("Service ID:",list_services)
    date=st.date_input("Date:",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
    time=st.time_input("Time:")

    dts=str(date)+" "+str(time)

    if st.button("Add resident avails service"):
        add_ras(rid, sid, dts)
        st.success("Added resident avails service successfully")

def show_ras_resident(username):
    result=view_all_ras_resident(username)
    df=pd.DataFrame(result,columns=["ResidentUID","serviceID","ServiceTime"],dtype=str)
    st.table(df)

def update_ras_resident(username):
    result=view_all_ras_resident(username)
    df=pd.DataFrame(result,columns=["ResidentUID","serviceID","ServiceTime"],dtype=str)
    with st.expander("Current resident avails services:"):
        st.table(df)
    
    list_residents=residentids()
    list_services=serviceids()

    list_rid=[username]
    list_sid= df.loc[df['ResidentUID'] == username, 'serviceID'].tolist()
    list_ras=[]
    for i in range(len(list_sid)):
        list_ras.append(f"{list_rid[0]}-{list_sid[i]}")

    selected_ras=st.selectbox("Select a resident availed service to edit:",list_ras)
    selected_result=get_ras(selected_ras.split('-')[0], selected_ras.split('-')[1])

    if selected_result:
        rid=selected_result[0][0]
        sid=selected_result[0][1]
        dts=str(selected_result[0][2])
        date=dt.date(int(dts.split(" ")[0].split('-')[0]),int(dts.split(" ")[0].split('-')[1]),int(dts.split(" ")[0].split('-')[2]))
        time=dt.time(int(dts.split(" ")[1].split(':')[0]),int(dts.split(" ")[1].split(':')[1]),int(dts.split(" ")[1].split(':')[2]))

        with st.expander("Edit resident availed service:"):
            new_rid=st.selectbox("Resident ID:",[username])
            new_sid=st.selectbox("Service ID:",list_services,index=list_services.index(sid))
            new_date=st.date_input("Date:",value=date,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
            new_time=st.time_input("Time:",time)

            new_dts=str(new_date)+" "+str(new_time)

            if st.button("Update resident availed service:"):
                edit_ras(new_rid, new_sid, new_dts, rid, sid)
                st.success("Updated the resident availed service successfully")

def delete_ras_resident(username):
    result=view_all_ras_resident(username)
    df=pd.DataFrame(result,columns=["ResidentUID","serviceID","ServiceTime"],dtype=str)
    with st.expander("Current resident avails services:"):
        st.table(df)
    
    list_residents=residentids()
    list_services=serviceids()

    list_rid=[username]
    list_sid= df.loc[df['ResidentUID'] == username, 'serviceID'].tolist()
    list_ras=[]
    for i in range(len(list_sid)):
        list_ras.append(f"{list_rid[0]}-{list_sid[i]}")

    selected_ras=st.selectbox("Select a resident availed service to delete:",list_ras)
    st.warning(f"Do you want to delete resident availed service {selected_ras}?")

    if st.button("Delete resident availed service"):
        drop_ras(selected_ras.split('-')[0], selected_ras.split('-')[1])
        st.success("Deleted the resident successfully")