# aisles.csv -> aisles_id, aisles 마트내 구역 아이디
# departments.csv -> department_id, department -> 부서 별 아이디
# order_products__prior.csv -> order_id,product_id,add_to_cart_order(개수),reordered
# order_producets__train.csv -> order_id,product_id,add_to_cart_order,reordered
# orders.csv -> order_id, user_id, eval_set, order_number, order_dow(주문 요일), order_hour_of_day, days_since_prior_order(주문 경과 시간)
# products.csv -> product_id, product_name, aisle_id, department_id

import streamlit as st
from streamlit.session_state import SessionState
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache
def load_data1():
    df1 = pd.read_csv('aisles.csv')
    return df1
    
@st.cache
def load_data2():
    df2 = pd.read_csv('departments.csv')
    return df2

def init_session_state():
    return SessionState.get(page="Home")

session_state = init_session_state()

def page_products():
    st.title('Products')
def page_aisles():
        
    st.title("aisles")
    aisles = load_data1()
    
    value1 = st.slider("Choose the aisle'id",1, 134)

    selected_aisle = aisles[aisles['aisle_id'] == value1]['aisle'].values
    st.write(f"Selected Aisle ID: {value1}")
    
    if selected_aisle:
        st.write(f"Aisle Value: {selected_aisle[0]}")
    else:
        st.write("No matching aisle found for the selected ID.")
        
    st.table(aisles)

def page_departments():
    st.title('Departments')
    departments = load_data2()

    value2 = st.slider("Choose the departments'id", 1, 21)

    selected_department = departments[departments['department_id'] == value2]['department'].values
    st.write(f"Selected Department ID : {value2}")

    if selected_department:
        st.write(f"Department Value : {selected_department[0]}")
    else :
        st.write("No matching department found for the selected ID.")

    st.table(departments)
    

def main():
    st.markdown("<h1 style='text-align: center; color: #623AA2;'>Instacart Market</h1>", unsafe_allow_html=True)
    st.sidebar.title("Menu")

    if st.sidebar.button("Aisles"):
        session_state.page = "Aisles"
    if st.sidebar.button("Departments"):
        session_state.page = "Departments"
    if st.sidebar.button("Products"):
        session_state.page = "Products"
        
    if session_state.page == "Home":
        st.write("Welcome to the Instacart Market Page")
    elif session_state.page == "Aisles":
        page_aisles()
    elif session_state.page == "Departments":
        page_departments()
    elif session_state.page == "Products":
        page_products()
    
        
    

if __name__ == "__main__":
    main()
