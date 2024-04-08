import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title = "Iris Flowers",
    page_icon = "🌸",
    layout = "centered",
)

st.title("🌸🌼🌺 Iris Flower 🌹🌷🪻")

st.header("Introduction")
st.markdown("""
    This dataset includes measurements of the sepal length and width, and petal length and width of 150 iris flowers from three different species. 
"""
)

st.divider()

df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

with st.sidebar:
    # Input filter options
    sepal_length_slider = st.slider(
        "Sepal Length (mm)",
        min(df["sepal_length"]),
        max(df["sepal_length"]),
    )
    sepal_width_slider = st.slider(
        "Sepal Width (mm)",
        min(df["sepal_width"]),
        max(df["sepal_width"]),
    )
    pedal_length_slider = st.slider(
        "Petal Length (mm)",
        min(df["petal_length"]),
        max(df["petal_length"]),
    )
    pedal_width_slider = st.slider(
        "Petal Width (mm)",
        min(df["petal_width"]),
        max(df["petal_width"]),
    )
    species_filter = st.selectbox(
        "Species",
        df["species"].unique(),
        index = None
    )

# Filter the data
if species_filter:
    df = df[df["species"] == species_filter]

df = df[df["sepal_length"] > sepal_length_slider]
df = df[df["sepal_width"] > sepal_width_slider]
df = df[df["petal_length"] > pedal_length_slider]
df = df[df["petal_width"] > pedal_width_slider]

with st.expander("RAW Data"):
    st.write(df)

# Plotting fig & fig3
fig = px.histogram(
    df,
    x = "sepal_length",
    y = "sepal_width",
)

fig3 = px.histogram(
    df,
    x = "petal_length",
    y = "petal_width",
)

tab1, tab2 = st.tabs(["Sepal", "Petal"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig3, theme="streamlit", use_container_width=True)

# Plotting fig2 & fig4
fig2 = px.scatter(
    df,
    x = "sepal_length", 
    y = "sepal_width",
    color= "species",
    hover_name= "species",
)

fig4 = px.scatter(
    df,
    x = "petal_length", 
    y = "petal_width",
    color= "species",
    hover_name= "species",
)

tab1, tab2 = st.tabs(["Sepal", "Petal"])
with tab1:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig4, theme="streamlit", use_container_width=True)