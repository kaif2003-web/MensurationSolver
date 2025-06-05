import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils import validate_positive_input, format_result, PI

def plot_sphere(radius):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create a sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = radius * np.cos(u) * np.sin(v)
    y = radius * np.sin(u) * np.sin(v)
    z = radius * np.cos(v)
    
    # Plot the surface
    ax.plot_wireframe(x, y, z, color="blue", alpha=0.5)
    
    # Set limits and title
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.set_zlim(-radius, radius)
    ax.set_title(f"Sphere with radius {radius}")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    return fig

def plot_hollow_sphere(outer_radius, inner_radius):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create the outer sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x_outer = outer_radius * np.cos(u) * np.sin(v)
    y_outer = outer_radius * np.sin(u) * np.sin(v)
    z_outer = outer_radius * np.cos(v)
    
    # Plot the outer surface
    ax.plot_wireframe(x_outer, y_outer, z_outer, color="blue", alpha=0.5)
    
    # Create the inner sphere (shown as a partial cutout)
    u2, v2 = np.mgrid[0:np.pi:10j, 0:np.pi:10j]
    x_inner = inner_radius * np.cos(u2) * np.sin(v2)
    y_inner = inner_radius * np.sin(u2) * np.sin(v2)
    z_inner = inner_radius * np.cos(v2)
    
    # Plot the inner surface
    ax.plot_wireframe(x_inner, y_inner, z_inner, color="red", alpha=0.5)
    
    # Set limits and title
    ax.set_xlim(-outer_radius, outer_radius)
    ax.set_ylim(-outer_radius, outer_radius)
    ax.set_zlim(-outer_radius, outer_radius)
    ax.set_title(f"Hollow Sphere (Outer r={outer_radius}, Inner r={inner_radius})")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    return fig

def plot_cylinder(radius, height):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create cylinder
    angle = np.linspace(0, 2*np.pi, 20)
    z = np.linspace(0, height, 2)
    theta, z = np.meshgrid(angle, z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Plot the side surface
    ax.plot_surface(x, y, z, alpha=0.5, color='blue')
    
    # Plot top and bottom circles
    z_bottom = np.zeros(20)
    z_top = np.ones(20) * height
    x_circle = radius * np.cos(angle)
    y_circle = radius * np.sin(angle)
    
    ax.plot(x_circle, y_circle, z_bottom, color='blue')
    ax.plot(x_circle, y_circle, z_top, color='blue')
    
    # Set limits
    max_range = max(radius, height/2)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(0, height)
    
    ax.set_title(f"Cylinder (r={radius}, h={height})")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set aspect ratio
    ax.set_box_aspect([1, 1, height/max_range])
    
    return fig

def plot_hollow_cylinder(outer_radius, inner_radius, height):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create outer cylinder
    angle = np.linspace(0, 2*np.pi, 20)
    z = np.linspace(0, height, 2)
    theta, z = np.meshgrid(angle, z)
    x_outer = outer_radius * np.cos(theta)
    y_outer = outer_radius * np.sin(theta)
    
    # Plot the outer side surface
    ax.plot_surface(x_outer, y_outer, z, alpha=0.5, color='blue')
    
    # Create inner cylinder (shown as partial)
    angle_inner = np.linspace(0, np.pi, 10)
    z_inner = np.linspace(0, height, 2)
    theta_inner, z_inner = np.meshgrid(angle_inner, z_inner)
    x_inner = inner_radius * np.cos(theta_inner)
    y_inner = inner_radius * np.sin(theta_inner)
    
    # Plot the inner side surface
    ax.plot_surface(x_inner, y_inner, z_inner, alpha=0.5, color='red')
    
    # Plot top and bottom rims
    z_bottom = np.zeros(20)
    z_top = np.ones(20) * height
    x_outer_circle = outer_radius * np.cos(angle)
    y_outer_circle = outer_radius * np.sin(angle)
    x_inner_circle = inner_radius * np.cos(angle)
    y_inner_circle = inner_radius * np.sin(angle)
    
    ax.plot(x_outer_circle, y_outer_circle, z_bottom, color='blue')
    ax.plot(x_outer_circle, y_outer_circle, z_top, color='blue')
    ax.plot(x_inner_circle, y_inner_circle, z_bottom, color='red')
    ax.plot(x_inner_circle, y_inner_circle, z_top, color='red')
    
    # Set limits
    max_range = max(outer_radius, height/2)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(0, height)
    
    ax.set_title(f"Hollow Cylinder (Outer r={outer_radius}, Inner r={inner_radius}, h={height})")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set aspect ratio
    ax.set_box_aspect([1, 1, height/max_range])
    
    return fig

def plot_cone(radius, height):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create cone
    angle = np.linspace(0, 2*np.pi, 20)
    height_points = np.linspace(0, height, 20)
    
    # Create the cone mesh
    for h in height_points:
        r = radius * (1 - h/height)  # radius decreases linearly with height
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        z = np.ones_like(angle) * h
        ax.plot(x, y, z, color='blue', alpha=0.5)
    
    # Plot straight lines from apex to base
    for ang in np.linspace(0, 2*np.pi, 10):
        x = [0, radius * np.cos(ang)]
        y = [0, radius * np.sin(ang)]
        z = [height, 0]
        ax.plot(x, y, z, color='blue', alpha=0.5)
    
    # Plot base circle
    z_bottom = np.zeros(angle.shape)
    x_circle = radius * np.cos(angle)
    y_circle = radius * np.sin(angle)
    ax.plot(x_circle, y_circle, z_bottom, color='blue')
    
    # Set limits
    max_range = max(radius, height/2)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(0, height)
    
    ax.set_title(f"Cone (r={radius}, h={height})")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set aspect ratio
    ax.set_box_aspect([1, 1, height/max_range])
    
    return fig

def plot_hollow_cone(outer_radius, inner_radius, height):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create outer cone
    angle = np.linspace(0, 2*np.pi, 20)
    height_points = np.linspace(0, height, 10)
    
    # Create the outer cone mesh
    for h in height_points:
        r = outer_radius * (1 - h/height)  # radius decreases linearly with height
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        z = np.ones_like(angle) * h
        ax.plot(x, y, z, color='blue', alpha=0.5)
    
    # Create inner cone (shown as partial)
    angle_inner = np.linspace(0, np.pi, 10)
    height_points_inner = np.linspace(0, height * 0.99, 10)  # Slightly shorter to avoid overlap
    
    # Create the inner cone mesh
    for h in height_points_inner:
        r = inner_radius * (1 - h/height)  # radius decreases linearly with height
        x = r * np.cos(angle_inner)
        y = r * np.sin(angle_inner)
        z = np.ones_like(angle_inner) * h
        ax.plot(x, y, z, color='red', alpha=0.5)
    
    # Plot outer base circle
    z_bottom = np.zeros(angle.shape)
    x_outer_circle = outer_radius * np.cos(angle)
    y_outer_circle = outer_radius * np.sin(angle)
    ax.plot(x_outer_circle, y_outer_circle, z_bottom, color='blue')
    
    # Plot inner base circle
    x_inner_circle = inner_radius * np.cos(angle)
    y_inner_circle = inner_radius * np.sin(angle)
    ax.plot(x_inner_circle, y_inner_circle, z_bottom, color='red')
    
    # Set limits
    max_range = max(outer_radius, height/2)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_zlim(0, height)
    
    ax.set_title(f"Hollow Cone (Outer r={outer_radius}, Inner r={inner_radius}, h={height})")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set aspect ratio
    ax.set_box_aspect([1, 1, height/max_range])
    
    return fig

def plot_cube(side):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Cube vertices
    r = [0, side]
    vertices = np.array([(x, y, z) for x in r for y in r for z in r])
    
    # Define the 12 edges
    edges = [
        # Bottom face
        (0, 1), (1, 3), (3, 2), (2, 0),
        # Top face
        (4, 5), (5, 7), (7, 6), (6, 4),
        # Vertical edges
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    
    # Plot the edges
    for i, j in edges:
        ax.plot([vertices[i, 0], vertices[j, 0]],
                [vertices[i, 1], vertices[j, 1]],
                [vertices[i, 2], vertices[j, 2]], color='blue')
    
    # Set limits and title
    ax.set_xlim(0, side)
    ax.set_ylim(0, side)
    ax.set_zlim(0, side)
    ax.set_title(f"Cube with side {side}")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1, 1, 1])
    
    return fig

def plot_cuboid(length, breadth, height):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')
    
    # Cuboid vertices
    vertices = np.array([
        [0, 0, 0],  # 0
        [length, 0, 0],  # 1
        [0, breadth, 0],  # 2
        [length, breadth, 0],  # 3
        [0, 0, height],  # 4
        [length, 0, height],  # 5
        [0, breadth, height],  # 6
        [length, breadth, height]  # 7
    ])
    
    # Define the 12 edges
    edges = [
        # Bottom face
        (0, 1), (1, 3), (3, 2), (2, 0),
        # Top face
        (4, 5), (5, 7), (7, 6), (6, 4),
        # Vertical edges
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    
    # Plot the edges
    for i, j in edges:
        ax.plot([vertices[i, 0], vertices[j, 0]],
                [vertices[i, 1], vertices[j, 1]],
                [vertices[i, 2], vertices[j, 2]], color='blue')
    
    # Set limits and title
    ax.set_xlim(0, length)
    ax.set_ylim(0, breadth)
    ax.set_zlim(0, height)
    ax.set_title(f"Cuboid (l={length}, b={breadth}, h={height})")
    
    # Make the panes transparent
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Make the grid lines transparent
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set aspect ratio
    ax.set_box_aspect([length, breadth, height])
    
    return fig

def display_solid_cone():
    st.subheader("Solid Cone")
    
    with st.form("solid_cone_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Total Surface Area (TSA)", "Curved Surface Area (CSA)", "Volume"]
        )
        
        radius = st.number_input("Radius of Cone", min_value=0.1, value=3.0, step=0.1)
        
        if calculation_type in ["Total Surface Area (TSA)", "Curved Surface Area (CSA)"]:
            slant_height = st.number_input("Slant Height/Length of Cone", min_value=0.1, value=5.0, step=0.1)
            height = None
        else:
            height = st.number_input("Height of Cone", min_value=0.1, value=4.0, step=0.1)
            slant_height = None
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if validate_positive_input(radius, "Radius"):
            # Calculate height or slant height if one is missing
            if height is None and slant_height is not None:
                if validate_positive_input(slant_height, "Slant Height"):
                    height = math.sqrt(slant_height**2 - radius**2)
            elif slant_height is None and height is not None:
                if validate_positive_input(height, "Height"):
                    slant_height = math.sqrt(height**2 + radius**2)
            
            # Visual representation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                fig = plot_cone(radius, height)
                st.pyplot(fig)
            
            with col2:
                if calculation_type == "Total Surface Area (TSA)":
                    tsa = PI * radius * (radius + slant_height)
                    format_result("Total Surface Area", tsa, "TSA = π × r × (r + l)", "square units")
                
                elif calculation_type == "Curved Surface Area (CSA)":
                    csa = PI * radius * slant_height
                    format_result("Curved Surface Area", csa, "CSA = π × r × l", "square units")
                
                elif calculation_type == "Volume":
                    volume = (PI * radius**2 * height) / 3
                    format_result("Volume", volume, "V = (π × r² × h) / 3", "cubic units")

def display_solid_cylinder():
    st.subheader("Solid Cylinder")
    
    with st.form("solid_cylinder_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Total Surface Area (TSA)", "Curved Surface Area (CSA)", "Volume"]
        )
        
        radius = st.number_input("Radius of Cylinder", min_value=0.1, value=3.0, step=0.1)
        height = st.number_input("Height of Cylinder", min_value=0.1, value=5.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if validate_positive_input(radius, "Radius") and validate_positive_input(height, "Height"):
            # Visual representation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                fig = plot_cylinder(radius, height)
                st.pyplot(fig)
            
            with col2:
                if calculation_type == "Total Surface Area (TSA)":
                    tsa = 2 * PI * radius * (radius + height)
                    format_result("Total Surface Area", tsa, "TSA = 2π × r × (r + h)", "square units")
                
                elif calculation_type == "Curved Surface Area (CSA)":
                    csa = 2 * PI * radius * height
                    format_result("Curved Surface Area", csa, "CSA = 2π × r × h", "square units")
                
                elif calculation_type == "Volume":
                    volume = PI * radius**2 * height
                    format_result("Volume", volume, "V = π × r² × h", "cubic units")

def display_solid_sphere():
    st.subheader("Solid Sphere")
    
    with st.form("solid_sphere_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Surface Area", "Volume"]
        )
        
        radius = st.number_input("Radius of Sphere", min_value=0.1, value=3.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted and validate_positive_input(radius, "Radius"):
        # Visual representation
        col1, col2 = st.columns([2, 3])
        
        with col1:
            fig = plot_sphere(radius)
            st.pyplot(fig)
        
        with col2:
            if calculation_type == "Surface Area":
                surface_area = 4 * PI * radius**2
                format_result("Surface Area", surface_area, "SA = 4π × r²", "square units")
            
            elif calculation_type == "Volume":
                volume = (4/3) * PI * radius**3
                format_result("Volume", volume, "V = (4/3) × π × r³", "cubic units")

def display_hollow_sphere():
    st.subheader("Hollow Sphere")
    
    with st.form("hollow_sphere_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Thickness", "Outer Surface Area", "Inner Surface Area", "Total Surface Area", "Volume"]
        )
        
        outer_radius = st.number_input("Outer Radius", min_value=0.1, value=5.0, step=0.1)
        inner_radius = st.number_input("Inner Radius", min_value=0.1, value=3.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if validate_positive_input(outer_radius, "Outer Radius") and validate_positive_input(inner_radius, "Inner Radius"):
            if outer_radius <= inner_radius:
                st.error("Outer radius must be greater than inner radius.")
            else:
                # Visual representation
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    fig = plot_hollow_sphere(outer_radius, inner_radius)
                    st.pyplot(fig)
                
                with col2:
                    if calculation_type == "Thickness":
                        thickness = outer_radius - inner_radius
                        format_result("Thickness", thickness, "t = R - r", "units")
                    
                    elif calculation_type == "Outer Surface Area":
                        outer_sa = 4 * PI * outer_radius**2
                        format_result("Outer Surface Area", outer_sa, "OSA = 4π × R²", "square units")
                    
                    elif calculation_type == "Inner Surface Area":
                        inner_sa = 4 * PI * inner_radius**2
                        format_result("Inner Surface Area", inner_sa, "ISA = 4π × r²", "square units")
                    
                    elif calculation_type == "Total Surface Area":
                        total_sa = 4 * PI * (outer_radius**2 + inner_radius**2)
                        format_result("Total Surface Area", total_sa, "TSA = 4π × (R² + r²)", "square units")
                    
                    elif calculation_type == "Volume":
                        volume = (4/3) * PI * (outer_radius**3 - inner_radius**3)
                        format_result("Volume", volume, "V = (4/3) × π × (R³ - r³)", "cubic units")

def display_hollow_cone():
    st.subheader("Hollow Cone")
    
    with st.form("hollow_cone_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Slant Height", "Volume", "Total Surface Area", "Curved Surface Area"]
        )
        
        outer_radius = st.number_input("Outer Radius", min_value=0.1, value=5.0, step=0.1)
        inner_radius = st.number_input("Inner Radius", min_value=0.1, value=3.0, step=0.1)
        height = st.number_input("Height", min_value=0.1, value=7.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if (validate_positive_input(outer_radius, "Outer Radius") and 
            validate_positive_input(inner_radius, "Inner Radius") and 
            validate_positive_input(height, "Height")):
            
            if outer_radius <= inner_radius:
                st.error("Outer radius must be greater than inner radius.")
            else:
                # Calculate slant height
                slant_height = math.sqrt(height**2 + outer_radius**2)
                
                # Visual representation
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    fig = plot_hollow_cone(outer_radius, inner_radius, height)
                    st.pyplot(fig)
                
                with col2:
                    if calculation_type == "Slant Height":
                        format_result("Slant Height", slant_height, "l = √(h² + R²)", "units")
                    
                    elif calculation_type == "Volume":
                        volume = (PI * height * (outer_radius**2 + outer_radius*inner_radius + inner_radius**2)) / 3
                        format_result("Volume", volume, "V = (π × h × (R² + Rr + r²)) / 3", "cubic units")
                    
                    elif calculation_type == "Total Surface Area":
                        # Calculate outer and inner slant heights
                        outer_slant = math.sqrt(height**2 + outer_radius**2)
                        inner_slant = math.sqrt(height**2 + inner_radius**2)
                        
                        tsa = PI * (outer_radius * (outer_radius + outer_slant) + inner_radius * (inner_radius + inner_slant))
                        format_result("Total Surface Area", tsa, "TSA = π × (R(R + l₁) + r(r + l₂))", "square units")
                    
                    elif calculation_type == "Curved Surface Area":
                        # Calculate outer and inner slant heights
                        outer_slant = math.sqrt(height**2 + outer_radius**2)
                        inner_slant = math.sqrt(height**2 + inner_radius**2)
                        
                        csa = PI * (outer_radius * outer_slant + inner_radius * inner_slant)
                        format_result("Curved Surface Area", csa, "CSA = π × (R × l₁ + r × l₂)", "square units")

def display_hollow_cylinder():
    st.subheader("Hollow Cylinder")
    
    with st.form("hollow_cylinder_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Thickness", "Volume", "Total Surface Area", "Curved Surface Area"]
        )
        
        outer_radius = st.number_input("Outer Radius", min_value=0.1, value=5.0, step=0.1)
        inner_radius = st.number_input("Inner Radius", min_value=0.1, value=3.0, step=0.1)
        height = st.number_input("Height", min_value=0.1, value=7.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if (validate_positive_input(outer_radius, "Outer Radius") and 
            validate_positive_input(inner_radius, "Inner Radius") and 
            validate_positive_input(height, "Height")):
            
            if outer_radius <= inner_radius:
                st.error("Outer radius must be greater than inner radius.")
            else:
                # Visual representation
                col1, col2 = st.columns([2, 3])
                
                with col1:
                    fig = plot_hollow_cylinder(outer_radius, inner_radius, height)
                    st.pyplot(fig)
                
                with col2:
                    if calculation_type == "Thickness":
                        thickness = outer_radius - inner_radius
                        format_result("Thickness", thickness, "t = R - r", "units")
                    
                    elif calculation_type == "Volume":
                        volume = PI * height * (outer_radius**2 - inner_radius**2)
                        format_result("Volume", volume, "V = π × h × (R² - r²)", "cubic units")
                    
                    elif calculation_type == "Total Surface Area":
                        tsa = 2 * PI * (outer_radius + inner_radius) * height + 2 * PI * (outer_radius**2 - inner_radius**2)
                        format_result("Total Surface Area", tsa, "TSA = 2π × (R + r) × h + 2π × (R² - r²)", "square units")
                    
                    elif calculation_type == "Curved Surface Area":
                        csa = 2 * PI * (outer_radius + inner_radius) * height
                        format_result("Curved Surface Area", csa, "CSA = 2π × (R + r) × h", "square units")

def display_cube():
    st.subheader("Cube")
    
    with st.form("cube_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Total Surface Area (TSA)", "Curved Surface Area (CSA)", "Volume", "Diagonal"]
        )
        
        side = st.number_input("Side Length", min_value=0.1, value=4.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted and validate_positive_input(side, "Side"):
        # Visual representation
        col1, col2 = st.columns([2, 3])
        
        with col1:
            fig = plot_cube(side)
            st.pyplot(fig)
        
        with col2:
            if calculation_type == "Total Surface Area (TSA)":
                tsa = 6 * side**2
                format_result("Total Surface Area", tsa, "TSA = 6a²", "square units")
            
            elif calculation_type == "Curved Surface Area (CSA)":
                csa = 4 * side**2
                format_result("Curved Surface Area", csa, "CSA = 4a²", "square units")
            
            elif calculation_type == "Volume":
                volume = side**3
                format_result("Volume", volume, "V = a³", "cubic units")
            
            elif calculation_type == "Diagonal":
                diagonal = side * math.sqrt(3)
                format_result("Diagonal", diagonal, "d = a√3", "units")

def display_cuboid():
    st.subheader("Cuboid")
    
    with st.form("cuboid_form"):
        calculation_type = st.selectbox(
            "Choose calculation type",
            ["Total Surface Area (TSA)", "Curved Surface Area (CSA)", "Volume", "Diagonal"]
        )
        
        length = st.number_input("Length", min_value=0.1, value=6.0, step=0.1)
        breadth = st.number_input("Breadth", min_value=0.1, value=4.0, step=0.1)
        height = st.number_input("Height", min_value=0.1, value=3.0, step=0.1)
        
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        if (validate_positive_input(length, "Length") and 
            validate_positive_input(breadth, "Breadth") and 
            validate_positive_input(height, "Height")):
            
            # Visual representation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                fig = plot_cuboid(length, breadth, height)
                st.pyplot(fig)
            
            with col2:
                if calculation_type == "Total Surface Area (TSA)":
                    tsa = 2 * (length*breadth + breadth*height + height*length)
                    format_result("Total Surface Area", tsa, "TSA = 2(lb + bh + hl)", "square units")
                
                elif calculation_type == "Curved Surface Area (CSA)":
                    csa = 2 * (length + breadth) * height
                    format_result("Curved Surface Area", csa, "CSA = 2(l + b)h", "square units")
                
                elif calculation_type == "Volume":
                    volume = length * breadth * height
                    format_result("Volume", volume, "V = l × b × h", "cubic units")
                
                elif calculation_type == "Diagonal":
                    diagonal = math.sqrt(length**2 + breadth**2 + height**2)
                    format_result("Diagonal", diagonal, "d = √(l² + b² + h²)", "units")

def display_3d_shapes():
    st.header("3D Shapes")
    
    shape_type = st.selectbox(
        "Select a 3D Shape",
        [
            "Solid Cone", 
            "Solid Cylinder", 
            "Solid Sphere", 
            "Hollow Sphere", 
            "Hollow Cone", 
            "Hollow Cylinder", 
            "Cube",
            "Cuboid"
        ]
    )
    
    st.markdown("---")
    
    if shape_type == "Solid Cone":
        display_solid_cone()
    elif shape_type == "Solid Cylinder":
        display_solid_cylinder()
    elif shape_type == "Solid Sphere":
        display_solid_sphere()
    elif shape_type == "Hollow Sphere":
        display_hollow_sphere()
    elif shape_type == "Hollow Cone":
        display_hollow_cone()
    elif shape_type == "Hollow Cylinder":
        display_hollow_cylinder()
    elif shape_type == "Cube":
        display_cube()
    elif shape_type == "Cuboid":
        display_cuboid()