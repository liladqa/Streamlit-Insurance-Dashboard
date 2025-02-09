import streamlit as  st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *

st.set_page_config(page_title="Dashboard", page_icon="🌍", layout="wide")
st.subheader("🔔 Insurance Descriptive Analytics")
st.markdown("##")

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

st.dataframe(df)

