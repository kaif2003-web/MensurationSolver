import streamlit as st
import math
from shapes_2D import display_2d_shapes
from shapes_3D import display_3d_shapes

# Set page configuration
st.set_page_config(
    page_title="Mensuration Calculator",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App title and description
st.title("Mensuration Calculator")
st.write("""
This application helps you calculate various properties of 2D and 3D geometric shapes. 
Select a shape category from the sidebar and enter the required dimensions to get your results.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
shape_category = st.sidebar.radio(
    "Select shape category:",
    ["2D Shapes", "3D Shapes"]
)

# Display the selected shape category
if shape_category == "2D Shapes":
    display_2d_shapes()
else:
    display_3d_shapes()

# Footer
st.markdown("---")
st.markdown("### About")
st.markdown("""
This application is built with Streamlit to help calculate properties of geometric shapes.
It covers a wide range of 2D shapes like circles, triangles, and rectangles, as well as 
3D shapes like spheres, cones, and cylinders.
""")