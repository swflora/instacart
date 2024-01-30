# aisles.csv -> aisles_id, aisles 마트내 구역 아이디
# departments.csv -> department_id, department -> 부서 별 아이디
# order_products__prior.csv -> order_id,product_id,add_to_cart_order(개수),reordered
# order_producets__train.csv -> order_id,product_id,add_to_cart_order,reordered
# orders.csv -> order_id, user_id, eval_set, order_number, order_dow(주문 요일), order_hour_of_day, days_since_prior_order(주문 경과 시간)
# products.csv -> product_id, product_name, aisle_id, department_id

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv("aisles.csv")
    return df

def main():
    st.markdown("<h1 style='text-align: center; color: #623AA2;'>Instacart Market</h1>", unsafe_allow_html=True)
    
    st.title("aisles")
    aisles = load_date()
    
    st.table(aisles)

if __name__ == "__main__":
    main()
