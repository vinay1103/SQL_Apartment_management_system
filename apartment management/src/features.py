import streamlit as st
from complaints import *
from dependent import *
from employee import *
from flat import *
from flat_has_security import *
from parking_slot import *
from resident import *
from resident_avails_services import *
from security import *
from services import *
from visitor import *

def resident_portion(choice,username):
    if choice=="complaints":
        st.header("complaints")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add complaint:")
            create_complaint_resident(username)
        elif sel_opt=="Show":
            st.subheader("All complaints:")
            show_complaints_resident(username)
        elif sel_opt=="Update":
            st.subheader("Update complaint:")
            update_complaint_resident(username)
        elif sel_opt=="Delete":
            st.subheader("Delete complaint:")
            delete_complaint_resident(username)
    elif choice=="dependent":
        st.header("dependent")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add dependent:")
            create_dependent_resident(username)
        elif sel_opt=="Show":
            st.subheader("All dependents:")
            show_dependents_resident(username)
        elif sel_opt=="Update":
            st.subheader("Update dependent:")
            update_dependent_resident(username)
        elif sel_opt=="Delete":
            st.subheader("Delete dependent:")
            delete_dependent_resident(username)
    elif choice=="employee":
        st.header("employee")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Show":
            st.subheader("All employees:")
            show_employees()

    elif choice=="flat_has_security":
        st.header("flat_has_security")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Show":
            st.subheader("All flat has security:")
            show_fhs()

    elif choice=="parking slot":
        st.header("parking slot")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Show":
            st.subheader("All parking slots:")
            show_parking()
    
    elif choice=="resident":
        st.header("resident")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add resident:")
            create_resident()
        elif sel_opt=="Show":
            st.subheader("All residents:")
            show_residents()
        elif sel_opt=="Update":
            st.subheader("Update resident:")
            update_resident()
        elif sel_opt=="Delete":
            st.subheader("Delete resident:")
            delete_resident()
    elif choice=="resident_avails_services":
        st.header("avail services")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add availed service:")
            create_ras_resident(username)
        elif sel_opt=="Show":
            st.subheader("All availed services:")
            show_ras_resident(username)
        elif sel_opt=="Update":
            st.subheader("Update availed service:")
            update_ras_resident(username)
        elif sel_opt=="Delete":
            st.subheader("Delete availed service:")
            delete_ras_resident(username)
    elif choice=="security":
        st.header("security")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add security:")
            create_security()
        elif sel_opt=="Show":
            st.subheader("All securities:")
            show_security()
        elif sel_opt=="Update":
            st.subheader("Update security:")
            update_security()
        elif sel_opt=="Delete":
            st.subheader("Delete security:")
            delete_security()
    elif choice=="services":
        st.header("services")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add service:")
            create_service()
        elif sel_opt=="Show":
            st.subheader("All services:")
            show_services()
        elif sel_opt=="Update":
            st.subheader("Update service:")
            update_service()
        elif sel_opt=="Delete":
            st.subheader("Delete service:")
            delete_service()
    elif choice=="visitor":
        st.header("visitor")
        opt=["Show","Show All"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Show":
            st.subheader("Your Visitors:")
            show_your_visitors(username)
        elif sel_opt=="Show All":
            st.subheader("All visitors:")
            show_visitors()

def security_portion(choice,username):
    if choice=="visitor":
        st.header("visitor")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add visitor:")
            create_visitor()
        elif sel_opt=="Show":
            st.subheader("All visitors:")
            show_visitors()
        elif sel_opt=="Update":
            st.subheader("Update visitor:")
            update_visitor()
        elif sel_opt=="Delete":
            st.subheader("Delete visitor:")
            delete_visitor()
    elif choice=="staff_list":
        st.header("Staff")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Show":
            st.subheader("Staff List:")
            show_staff()
    elif choice=="resident_list":
        st.header("Residents")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Show":
            st.subheader("Resident List:")
            show_residents_and_dependents()
    elif choice=="parking slot":
        st.header("parking slot")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Show":
            st.subheader("All parking slots:")
            show_parking()

def admin_portion(choice,username):
    if choice=="complaints":
        st.header("complaints")
        opt=["Show","Count"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add complaint:")
            create_complaint()
        elif sel_opt=="Show":
            st.subheader("All complaints:")
            show_complaints()
        elif sel_opt=="Update":
            st.subheader("Update complaint:")
            update_complaint()
        elif sel_opt=="Delete":
            st.subheader("Delete complaint:")
            delete_complaint()
        elif sel_opt=="Count":
            st.subheader("Complaint count for each Resident:")
            get_complaint_count()

    elif choice=="dependent":
        st.header("dependent")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add dependent:")
            create_dependent()
        elif sel_opt=="Show":
            st.subheader("All dependents:")
            show_dependents()
        elif sel_opt=="Update":
            st.subheader("Update dependent:")
            update_dependent()
        elif sel_opt=="Delete":
            st.subheader("Delete dependent:")
            delete_dependent()

    elif choice=="employee":
        st.header("employee")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add employee:")
            create_employee()
        elif sel_opt=="Show":
            st.subheader("All employees:")
            show_employees()
        elif sel_opt=="Update":
            st.subheader("Update employee:")
            update_employee()
        elif sel_opt=="Delete":
            st.subheader("Delete employee:")
            delete_employee()

    elif choice=="flat":
        st.header("flat")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add flat:")
            create_flat()
        elif sel_opt=="Show":
            st.subheader("All flats:")
            show_flats()
        elif sel_opt=="Update":
            st.subheader("Update flat:")
            update_flat()
        elif sel_opt=="Delete":
            st.subheader("Delete flat:")
            delete_flat()
    
    elif choice=="flat_has_security":
        st.header("flat_has_security")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add flat has security:")
            create_fhs()
        elif sel_opt=="Show":
            st.subheader("All flat has security:")
            show_fhs()
        elif sel_opt=="Update":
            st.subheader("Update flat has security:")
            update_fhs()
        elif sel_opt=="Delete":
            st.subheader("Delete flat has security:")
            delete_fhs()

    elif choice=="parking slot":
        st.header("parking slot")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add parking slot:")
            create_parking()
        elif sel_opt=="Show":
            st.subheader("All parking slots:")
            show_parking()
        elif sel_opt=="Update":
            st.subheader("Update parking slot:")
            update_parking()
        elif sel_opt=="Delete":
            st.subheader("Delete parking slot:")
            delete_parking()

    elif choice=="resident":
        st.header("resident")
        opt=["Add","Show","Delete","Total Size"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add resident:")
            create_resident()
        elif sel_opt=="Show":
            st.subheader("All residents:")
            show_residents()
        elif sel_opt=="Update":
            st.subheader("Update resident:")
            update_resident()
        elif sel_opt=="Delete":
            st.subheader("Delete resident:")
            delete_resident()
        elif sel_opt=="Total Size":
            st.header("Residents with Dependents Count")
            display_residents_with_dependents_count()

    elif choice=="resident_avails_services":
        st.header("avail services")
        opt=["Show","Count"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add availed service:")
            create_ras()
        elif sel_opt=="Show":
            st.subheader("All availed services:")
            show_ras()
        elif sel_opt=="Update":
            st.subheader("Update availed service:")
            update_ras()
        elif sel_opt=="Delete":
            st.subheader("Delete availed service:")
            delete_ras()
        elif sel_opt=="Count":
            st.subheader("Get Residents with Service:")
            get_residents()

    elif choice=="security":
        st.header("security")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add security:")
            create_security()
        elif sel_opt=="Show":
            st.subheader("All securities:")
            show_security()
        elif sel_opt=="Update":
            st.subheader("Update security:")
            update_security()
        elif sel_opt=="Delete":
            st.subheader("Delete security:")
            delete_security()

    elif choice=="services":
        st.header("services")
        opt=["Add","Show","Update","Delete"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add service:")
            create_service()
        elif sel_opt=="Show":
            st.subheader("All services:")
            show_services()
        elif sel_opt=="Update":
            st.subheader("Update service:")
            update_service()
        elif sel_opt=="Delete":
            st.subheader("Delete service:")
            delete_service()

    elif choice=="visitor":
        st.header("visitor")
        opt=["Show"]
        sel_opt=st.selectbox("Select the operation",opt)
        if sel_opt=="Add":
            st.subheader("Add visitor:")
            create_visitor()
        elif sel_opt=="Show":
            st.subheader("All visitors:")
            show_visitors()
        elif sel_opt=="Update":
            st.subheader("Update visitor:")
            update_visitor()
        elif sel_opt=="Delete":
            st.subheader("Delete visitor:")
            delete_visitor()
