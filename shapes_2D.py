import streamlit as st
import math
from utils import (
    validate_positive_input, validate_triangle_sides, format_result, PI,
    create_circle_plot, create_rectangle_plot, create_triangle_plot,
    create_square_plot, create_trapezium_plot, create_ellipse_plot
)

def display_circle():
    st.subheader("Circle")
    
    # Input form
    with st.form("circle_form"):
        radius = st.number_input("Radius of Circle", min_value=0.1, value=1.0, step=0.1)
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Diameter", "Circumference", "Area"]
        )
        submitted = st.form_submit_button("Calculate")
    
    if submitted and validate_positive_input(radius, "Radius"):
        # Visual representation
        col1, col2 = st.columns([2, 3])
        
        with col1:
            fig = create_circle_plot(radius)
            st.pyplot(fig)
        
        with col2:
            if calculation_type == "Diameter":
                diameter = 2 * radius
                format_result("Diameter", diameter, "D = 2 × r", "units")
            
            elif calculation_type == "Circumference":
                circumference = 2 * PI * radius
                format_result("Circumference", circumference, "C = 2 × π × r", "units")
            
            elif calculation_type == "Area":
                area = PI * radius * radius
                format_result("Area", area, "A = π × r²", "square units")

def display_triangle():
    st.subheader("Triangle")
    
    triangle_type = st.selectbox(
        "Choose Triangle Type",
        ["Scalene Triangle", "Isosceles Triangle", "Equilateral Triangle"]
    )
    
    if triangle_type == "Scalene Triangle":
        with st.form("scalene_triangle_form"):
            side1 = st.number_input("Length of First Side", min_value=0.1, value=3.0, step=0.1)
            side2 = st.number_input("Length of Second Side", min_value=0.1, value=4.0, step=0.1)
            side3 = st.number_input("Length of Third Side", min_value=0.1, value=5.0, step=0.1)
            submitted = st.form_submit_button("Calculate")
        
        if submitted:
            if (validate_positive_input(side1, "Side 1") and 
                validate_positive_input(side2, "Side 2") and 
                validate_positive_input(side3, "Side 3") and
                validate_triangle_sides(side1, side2, side3)):
                
                # Visual representation
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    fig = create_triangle_plot(side1, side2, side3)
                    if fig:
                        st.pyplot(fig)
                
                with col2:
                    # Semi-perimeter
                    s = (side1 + side2 + side3) / 2
                    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
                    perimeter = side1 + side2 + side3
                    
                    format_result("Area", area, "A = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2", "square units")
                    format_result("Perimeter", perimeter, "P = a + b + c", "units")
    
    elif triangle_type == "Isosceles Triangle":
        with st.form("isosceles_triangle_form"):
            common_side = st.number_input("Length of Common Side", min_value=0.1, value=5.0, step=0.1)
            other_side = st.number_input("Length of Remaining Side", min_value=0.1, value=6.0, step=0.1)
            submitted = st.form_submit_button("Calculate")
        
        if submitted:
            if (validate_positive_input(common_side, "Common Side") and 
                validate_positive_input(other_side, "Other Side") and
                validate_triangle_sides(common_side, common_side, other_side)):
                
                # Visual representation
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    fig = create_triangle_plot(common_side, common_side, other_side)
                    if fig:
                        st.pyplot(fig)
                
                with col2:
                    # Calculate height
                    height = math.sqrt(common_side**2 - (other_side/2)**2)
                    area = 0.5 * other_side * height
                    perimeter = 2 * common_side + other_side
                    
                    format_result("Area", area, "A = 0.5 × b × h, where h = √(a² - (b/2)²)", "square units")
                    format_result("Perimeter", perimeter, "P = 2a + b", "units")
    
    elif triangle_type == "Equilateral Triangle":
        with st.form("equilateral_triangle_form"):
            side = st.number_input("Length of Side", min_value=0.1, value=5.0, step=0.1)
            submitted = st.form_submit_button("Calculate")
        
        if submitted and validate_positive_input(side, "Side"):
            # Visual representation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                fig = create_triangle_plot(side, side, side)
                st.pyplot(fig)
            
            with col2:
                area = (math.sqrt(3) / 4) * side * side
                perimeter = 3 * side
                height = (math.sqrt(3) / 2) * side
                
                format_result("Area", area, "A = (√3/4) × s²", "square units")
                format_result("Perimeter", perimeter, "P = 3 × s", "units")
                format_result("Height", height, "h = (√3/2) × s", "units")

def display_rectangle():
    st.subheader("Rectangle")
    
    with st.form("rectangle_form"):
        length = st.number_input("Length of Rectangle", min_value=0.1, value=5.0, step=0.1)
        breadth = st.number_input("Breadth of Rectangle", min_value=0.1, value=3.0, step=0.1)
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Perimeter", "Area"]
        )
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if validate_positive_input(length, "Length") and validate_positive_input(breadth, "Breadth"):
            # Visual representation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                fig = create_rectangle_plot(length, breadth)
                st.pyplot(fig)
            
            with col2:
                if calculation_type == "Perimeter":
                    perimeter = 2 * (length + breadth)
                    format_result("Perimeter", perimeter, "P = 2 × (l + b)", "units")
                
                elif calculation_type == "Area":
                    area = length * breadth
                    format_result("Area", area, "A = l × b", "square units")

def display_ellipse():
    st.subheader("Ellipse")
    
    with st.form("ellipse_form"):
        semi_major = st.number_input("Semi-Major Axis (a)", min_value=0.1, value=5.0, step=0.1)
        semi_minor = st.number_input("Semi-Minor Axis (b)", min_value=0.1, value=3.0, step=0.1)
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if validate_positive_input(semi_major, "Semi-Major Axis") and validate_positive_input(semi_minor, "Semi-Minor Axis"):
            # Visual representation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                fig = create_ellipse_plot(semi_major, semi_minor)
                st.pyplot(fig)
            
            with col2:
                area = PI * semi_major * semi_minor
                format_result("Area", area, "A = π × a × b", "square units")

def display_square():
    st.subheader("Square")
    
    with st.form("square_form"):
        side = st.number_input("Side Length of Square", min_value=0.1, value=5.0, step=0.1)
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Perimeter", "Area"]
        )
        submitted = st.form_submit_button("Calculate")
    
    if submitted and validate_positive_input(side, "Side"):
        # Visual representation
        col1, col2 = st.columns([2, 3])
        
        with col1:
            fig = create_square_plot(side)
            st.pyplot(fig)
        
        with col2:
            if calculation_type == "Perimeter":
                perimeter = 4 * side
                format_result("Perimeter", perimeter, "P = 4 × s", "units")
            
            elif calculation_type == "Area":
                area = side * side
                format_result("Area", area, "A = s²", "square units")

def display_right_angle_triangle():
    st.subheader("Right Angle Triangle")
    
    with st.form("right_angle_triangle_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Perimeter", "Area"]
        )
        
        if calculation_type == "Perimeter":
            base = st.number_input("Base Length", min_value=0.1, value=3.0, step=0.1)
            height = st.number_input("Height/Perpendicular Length", min_value=0.1, value=4.0, step=0.1)
            hypotenuse = st.number_input("Hypotenuse Length", min_value=0.1, value=5.0, step=0.1)
        else:
            base = st.number_input("Base Length", min_value=0.1, value=3.0, step=0.1)
            height = st.number_input("Height/Perpendicular Length", min_value=0.1, value=4.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if calculation_type == "Perimeter":
            if (validate_positive_input(base, "Base") and 
                validate_positive_input(height, "Height") and 
                validate_positive_input(hypotenuse, "Hypotenuse")):
                
                # Check if it's a valid right angle triangle
                if abs(base**2 + height**2 - hypotenuse**2) > 0.01:
                    st.error("The given sides do not form a right-angled triangle. Please check your inputs.")
                else:
                    # Visual representation
                    col1, col2 = st.columns([2, 3])
                    
                    with col1:
                        fig = create_triangle_plot(base, height, hypotenuse)
                        if fig:
                            st.pyplot(fig)
                    
                    with col2:
                        perimeter = base + height + hypotenuse
                        format_result("Perimeter", perimeter, "P = a + b + c", "units")
        
        elif calculation_type == "Area":
            if validate_positive_input(base, "Base") and validate_positive_input(height, "Height"):
                # Visual representation
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    hypotenuse = math.sqrt(base**2 + height**2)
                    fig = create_triangle_plot(base, height, hypotenuse)
                    if fig:
                        st.pyplot(fig)
                
                with col2:
                    area = 0.5 * base * height
                    format_result("Area", area, "A = 0.5 × b × h", "square units")

def display_trapezium():
    st.subheader("Trapezium")
    
    with st.form("trapezium_form"):
        parallel_side1 = st.number_input("Length of First Parallel Side", min_value=0.1, value=6.0, step=0.1)
        parallel_side2 = st.number_input("Length of Second Parallel Side", min_value=0.1, value=4.0, step=0.1)
        height = st.number_input("Height", min_value=0.1, value=3.0, step=0.1)
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if (validate_positive_input(parallel_side1, "First Parallel Side") and 
            validate_positive_input(parallel_side2, "Second Parallel Side") and 
            validate_positive_input(height, "Height")):
            
            # Visual representation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                fig = create_trapezium_plot(parallel_side1, parallel_side2, height)
                st.pyplot(fig)
            
            with col2:
                area = ((parallel_side1 + parallel_side2) * height) / 2
                format_result("Area", area, "A = ((a + b) × h) / 2", "square units")

def display_2d_shapes():
    st.header("2D Shapes")
    
    shape_type = st.selectbox(
        "Select a 2D Shape",
        [
            "Circle", 
            "Triangle", 
            "Rectangle", 
            "Ellipse", 
            "Square", 
            "Right Angle Triangle",
            "Trapezium"
        ]
    )
    
    st.markdown("---")
    
    if shape_type == "Circle":
        display_circle()
    elif shape_type == "Triangle":
        display_triangle()
    elif shape_type == "Rectangle":
        display_rectangle()
    elif shape_type == "Ellipse":
        display_ellipse()
    elif shape_type == "Square":
        display_square()
    elif shape_type == "Right Angle Triangle":
        display_right_angle_triangle()
    elif shape_type == "Trapezium":
        display_trapezium()