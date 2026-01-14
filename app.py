import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Data Explorer",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Data Explorer")
st.markdown("Upload a CSV file and explore your data interactively!")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)

    # Show basic info
    st.subheader("Dataset Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Memory", f"{df.memory_usage().sum() / 1024:.2f} KB")

    # Display data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Statistics
    st.subheader("Statistics")
    st.dataframe(df.describe())

    # Visualization
    st.subheader("Visualization")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("X-axis", numeric_cols)
        with col2:
            y_axis = st.selectbox("Y-axis", numeric_cols, index=1)

        fig = px.scatter(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("👆 Upload a CSV file to get started!")


"""
import streamlit as st

st.title("Hello, Streamlit! 👋")
st.write("This is my first Streamlit app!")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

import streamlit as st

# Title
st.title("My App Title")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Regular text
st.write("This is regular text")

# Markdown
st.markdown("**Bold** and *italic* text")

# Code
st.code("print('Hello, World!')", language='python')


import streamlit as st
import pandas as pd
import numpy as np

# DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 92, 78]
})

st.dataframe(df)  # Interactive table
st.table(df)      # Static table

# Metrics
st.metric(label="Temperature", value="70 °F", delta="-1.2 °F")

# JSON
st.json({'name': 'Alice', 'age': 25})


import streamlit as st

# Text input
name = st.text_input("Enter your name")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=120)

# Slider
score = st.slider("Select score", 0, 100, 50)

# Select box
option = st.selectbox("Choose option", ['A', 'B', 'C'])

# Multi-select
choices = st.multiselect("Choose multiple", ['Option 1', 'Option 2', 'Option 3'])

# Checkbox
agree = st.checkbox("I agree")

# Radio buttons
choice = st.radio("Pick one", ['Option A', 'Option B'])

# Button
if st.button("Click me"):
    st.write("Button clicked!")

# File uploader
file = st.file_uploader("Upload file", type=['csv', 'txt'])


import streamlit as st
import pandas as pd
import numpy as np

# Line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Area chart
st.area_chart(chart_data)

# Map (with lat/lon data)
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# Plotly charts (more advanced)
import plotly.express as px
fig = px.scatter(chart_data, x='A', y='B')
st.plotly_chart(fig)



import streamlit as st

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is in the sidebar")
sidebar_option = st.sidebar.selectbox("Choose", ['A', 'B', 'C'])

# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
with col3:
    st.write("Column 3")

# Expander
with st.expander("Click to expand"):
    st.write("Hidden content here")

# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Content for tab 1")
with tab2:
    st.write("Content for tab 2")
with tab3:
    st.write("Content for tab 3")

# Container
with st.container():
    st.write("This is inside a container")



import streamlit as st
import pandas as pd

# Cache data loading
@st.cache_data
def load_data():
    # This function only runs once, then caches the result
    return pd.read_csv('large_file.csv')

# Cache resource (like ML models)
@st.cache_resource
def load_model():
    # Load expensive resource once
    return load_my_ml_model()

# Use cached functions
df = load_data()
model = load_model()

import streamlit as st

# Initialize session state
if 'count' not in st.session_state:
    st.session_state.count = 0

# Increment button
if st.button('Increment'):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")

"""
