import streamlit as st
import pandas as pd


st.markdown("<center><u><h1>Registration Form</h1></cenetr></u>",unsafe_allow_html=True)
with st.form("my_form"):
    f_name,m_name,l_name=st.columns(3)
    with f_name:
           f_name=st.text_input("",placeholder="First name",label_visibility="collapsed")
    with m_name:
          m_name=st.text_input("",placeholder="Middle name",label_visibility="collapsed")
    with l_name:
        l_name=st.text_input("",placeholder="Last name",label_visibility="collapsed")
    age,number=st.columns(2)
    with age:
        age=st.text_input("",placeholder="DD/MM/YYYY",label_visibility="collapsed") 
    with number:
        number=st.text_input("",placeholder="Enter Phone Number",label_visibility="collapsed")
    email=st.text_input("",placeholder="Enetr E-mail ID",label_visibility="collapsed")
    course=st.multiselect("Select Course",["CO-Computer engineering","IF-Information technology","CE-Civil engineering","ME-Mechanical engineering","EE-Electrical engineering","AE-Automobile engineering"])
    photo=st.file_uploader("Select Photo",type=["jpg","png","jpeg"])
    s_state=st.form_submit_button("submit")
    if s_state:
        if f_name=="" and m_name=="" and l_name=="":
           st.warning("Please fill above information!")
        else:
           st.success("Submitted Successfully!")
        if s_state:
         data={"f_Name":[f_name],"m_name":[m_name],"l_name":[l_name],"Email":[email],"Phone number":[number],"Course":[course],"Photo":[photo]}
         df=pd.DataFrame(data)
         try:
            existing_df=pd.read_excel("data.xlsx")
            combined_df=pd.concat([existing_df,df])
            combined_df.to_excel("data.xlsx",index=False)
              
         except FileNotFoundError :
            df.to_excel("data.xlsx",index=False)
         st.write("Thank you")

            
            