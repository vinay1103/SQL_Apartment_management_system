import streamlit as st
import pandas as pd
import datetime as dt
from database import view_all_flats,add_resident,view_all_residents,get_resident,edit_resident,drop_resident,view_all_residents_and_dependents,get_residents_with_dependents_count

#Procedure###################################################################
def display_residents_with_dependents_count():
    residents_data = get_residents_with_dependents_count()
    df=pd.DataFrame(residents_data,columns=["Uid","name","flat_Id","family_size"])
    st.table(df)

def flatids():
    result=view_all_flats()
    df=pd.DataFrame(result,columns=["FlatID","no_bhk"])
    list_flatids=[i for i in df['FlatID']]
    return list_flatids

def create_resident():
    list_flatids=flatids()
    
    col1,col2=st.columns(2)

    with col1:
        aadhar=st.text_input("Aadhar card number:")
        fn=st.text_input("First name:")
        ln=st.text_input("Last name:")
        dob=st.date_input("Date of birth:",min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
        phone=st.text_input("Phone number:")
    with col2:
        gender=st.selectbox("Gender:",["M","F","O"])
        pet=st.selectbox("Pet info:",["no pet","Cat","Dog"])
        fid=st.selectbox("Flat ID:",list_flatids)
        ro=st.selectbox("Rent or Own?",["Own","Rent"])
    
    if st.button("Add resident"):
        add_resident(aadhar, fn, ln, dob, phone, gender, pet, fid, ro)
        st.success("Added resident successfully")

def show_residents():
    result=view_all_residents()
    df=pd.DataFrame(result,columns=["Aadhar","Fname","Lname","DOB","phone","gender","pet_info","FlatID","rent_owned"],dtype=str)
    st.table(df)

def show_residents_and_dependents():
    result = view_all_residents_and_dependents()
    df = pd.DataFrame(result, columns=["FlatID", "resident_type", "UID", "Fname", "Lname", "age", "phone", "gender", "pet_info", "rent_owned"], dtype=str)
    st.table(df)

def update_resident():
    result=view_all_residents()
    df=pd.DataFrame(result,columns=["Aadhar","Fname","Lname","DOB","phone","gender","pet_info","FlatID","rent_owned"],dtype=str)
    with st.expander("Current residents:"):
        st.table(df)
    
    list_flatids=flatids()
    list_ids=[i for i in df['Aadhar']]
    selected_id=st.selectbox("Select a resident to update:",list_ids)
    selected_result=get_resident(selected_id)

    if selected_result:
        aadhar=selected_result[0][0]
        fn=selected_result[0][1]
        ln=selected_result[0][2]
        dob=selected_result[0][3]
        phone=selected_result[0][4]
        gender=selected_result[0][5]
        pet=selected_result[0][6]
        fid=selected_result[0][7]
        ro=selected_result[0][8]

        list_pets=["no pet","Cat","Dog"]
        list_gender=["M","F","O"]
        lits_ro=["Own","Rent"]
        with st.expander("Edit resident:"):
            col1,col2=st.columns(2)
            with col1:
                new_aadhar=st.text_input("Aadhar card number:",aadhar)
                new_fn=st.text_input("First name:",fn)
                new_ln=st.text_input("Last name:",ln)
                new_dob=st.date_input("Date of birth:",value=dob,min_value=dt.date(1800,1,1),max_value=dt.datetime.today())
                new_phone=st.text_input("Phone number:",phone)
            with col2:
                new_gender=st.selectbox("Gender:",list_gender,index=list_gender.index(gender))
                new_pet=st.selectbox("Pet info:",list_pets,index=list_pets.index(pet))
                new_fid=st.selectbox("Flat ID:",list_flatids,index=list_flatids.index(fid))
                new_ro=st.selectbox("Rent or Own?",lits_ro,index=lits_ro.index(ro))
            if st.button("Update resident"):
                edit_resident(new_aadhar, new_fn, new_ln, new_dob, new_phone, new_gender, new_pet, new_fid, new_ro, aadhar)
                st.success("Updated the resident successfully")

def delete_resident():
    result=view_all_residents()
    df=pd.DataFrame(result,columns=["Aadhar","Fname","Lname","DOB","phone","gender","pet_info","FlatID","rent_owned"],dtype=str)
    with st.expander("Current residents:"):
        st.table(df)
    
    list_ids=[i for i in df['Aadhar']]
    selected_id=st.selectbox("Select a resident to delete:",list_ids)
    st.warning(f"Do you want to delete resident {selected_id}?")

    if st.button("Delete resident"):
        drop_resident(selected_id)
        st.success("Deleted the resident successfully")

        