import streamlit as st
import pandas as pd
from database import add_flat,view_all_flats,get_flat,edit_flat,drop_flat

def create_flat():
    fid=st.text_input("Flat ID:")
    nbhk=st.number_input("How many BHK?",step=1)

    if st.button("Add flat"):
        add_flat(fid, nbhk)
        st.success("Added flat successfully")

def show_flats():
    result=view_all_flats()
    df=pd.DataFrame(result,columns=["FlatID","no_bhk"])
    st.table(df)

def update_flat():
    result=view_all_flats()
    df=pd.DataFrame(result,columns=["FlatID","no_bhk"])

    with st.expander("Current flats:"):
        st.table(df)
    
    list_flats=[i for i in df['FlatID']]
    selected_flat=st.selectbox("Select flat to edit:",list_flats)
    selected_result=get_flat(selected_flat)

    if selected_result:
        fid=selected_result[0][0]
        nbhk=selected_result[0][1]

        with st.expander("Edit flat:"):
            new_fid=st.text_input("Flat ID:",fid)
            new_nbhk=st.number_input("How many bhk?",value=nbhk,step=1)

            if st.button("Update flat"):
                edit_flat(new_fid, new_nbhk, fid)
                st.success("Updated flat details successfully")

def delete_flat():
    result=view_all_flats()
    df=pd.DataFrame(result,columns=["FlatID","no_bhk"])

    with st.expander("Current flats:"):
        st.table(df)

    list_flats=[i for i in df['FlatID']]
    selected_flat=st.selectbox("Select flat to delete:",list_flats)
    st.warning(f"Do you want to delete flat {selected_flat}?")

    if st.button("Delete flat"):
        drop_flat(selected_flat)
        st.success("Deleted the flat succesfully")