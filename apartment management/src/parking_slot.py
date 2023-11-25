import streamlit as st
import pandas as pd
from database import add_parking,view_all_parking,get_parking,edit_parking,drop_parking,view_all_flats

def flatids():
    result=view_all_flats()
    df=pd.DataFrame(result,columns=["FlatID","no_bhk"])
    list_flatids=[i for i in df['FlatID']]
    return list_flatids

def create_parking():
    list_flatids=flatids()
    slot=st.number_input("Slot number:",step=1)
    vt=st.text_input("Vehicle type:")
    fid=st.selectbox("Flat ID:",list_flatids)

    if st.button("Add parking slot"):
        add_parking(slot, vt, fid)
        st.success("Successfully added parking slot")

def show_parking():
    result=view_all_parking()
    df=pd.DataFrame(result,columns=["slotNo","vehicle_type","flatID"])
    st.table(df)

def update_parking():
    result=view_all_parking()
    df=pd.DataFrame(result,columns=["slotNo","vehicle_type","flatID"])
    with st.expander("Current parking slots:"):
        st.table(df)
    
    list_slots=[i for i in df['slotNo']]
    selected_slot=st.selectbox("Select a parking slot to edit:",list_slots)
    selected_result=get_parking(selected_slot)

    list_flatids=flatids()

    if selected_result:
        slot=selected_result[0][0]
        vt=selected_result[0][1]
        fid=selected_result[0][2]

        with st.expander("Edit parking slot:"):
            new_slot=st.number_input("Slot number:",step=1,value=slot)
            new_vt=st.text_input("Vehicle type:",vt)
            new_fid=st.selectbox("Flat ID:",list_flatids,index=list_flatids.index(fid))

            if st.button("Update parking slot"):
                edit_parking(new_slot, new_vt, new_fid, slot)
                st.success("Updated the slot successfully")

def delete_parking():
    result=view_all_parking()
    df=pd.DataFrame(result,columns=["slotNo","vehicle_type","flatID"])
    with st.expander("Current parking slots:"):
        st.table(df)

    list_slots=[i for i in df['slotNo']]
    selected_slot=st.selectbox("Select a parking slot to delete:",list_slots)
    st.warning(f"Do you want to delete parking slot {selected_slot}?")

    if st.button("Delete parking slot"):
        drop_parking(selected_slot)
        st.success("Deleted the parking slot successfully")