import streamlit as  st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *

st.set_page_config(page_title="Dashboard", page_icon="🌍", layout="wide")
st.subheader("🔔 Insurance Descriptive Analytics")
st.markdown("##")


#fetch data
result = view_all_data()
df = pd.DataFrame(result, columns=["Columns", 
                                   "Expiry",
                                   "Location",
                                   "State",
                                   "Region",
                                   "Investment",
                                   "Construction",
                                   "Business Type",
                                   "Earthquake",
                                   "Flood",
                                   "Rating",
                                   "id"])


#sidebar
st.sidebar.image("data/logo1.png", caption="Online Analytics")


#switcher
st.sidebar.header("Filter data")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

location = st.sidebar.multiselect(
    "Select Location",
    options=df["Location"].unique(),
    default=df["Location"].unique()
)

construction = st.sidebar.multiselect(
    "Select Construction",
    options=df["Construction"].unique(),
    default=df["Construction"].unique()
)

df_selection=df.query(
    "Region==@region & Location==@location & Construction==@construction"
)

def Home():
    with st.expander("Tabular"):
        showData = st.multiselect("Filter: ", df_selection.columns, default=[])
        st.write(df_selection[showData])

    #compute top analytics 
    total_investment = float(pd.Series(df_selection['Investment']).sum())
    investment_mode = float(pd.Series(df_selection['Investment']).mode())
    investment_mean = float(pd.Series(df_selection['Investment']).mean())
    investment_median= float(pd.Series(df_selection['Investment']).median()) 
    rating = float(pd.Series(df_selection['Rating']).sum())

    total1, total2, total3, total4, total5=st.columns(5, gap='large')

    with total1:
        st.info('Sum Investment',icon="💰")
        st.metric(label="Sum TZS",value=f"{total_investment:,.0f}")

    with total2:
        st.info("Most Frequent", icon="📌")
        st.metric(label="mode TZS", value=f"{investment_mode:,.0f}")

    with total3:
        st.info("Average", icon="📌")
        st.metric(label="mean TZS", value=f"{investment_mean:,.0f}")

    with total4:
        st.info("Central Earnings", icon="📌")
        st.metric(label="median TZS", value=f"{investment_median:,.0f}")

    with total5:
        st.info('Ratings',icon="💰")
        st.metric(label="Rating",value=numerize(rating),help=f""" Total Rating: {rating} """)

    st.markdown("""---""")

Home()




