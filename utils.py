import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

# Constants
PI = math.pi

def validate_positive_input(value, name):
    """Validate that an input is a positive number."""
    if value <= 0:
        st.error(f"{name} must be greater than zero.")
        return False
    return True

def validate_triangle_sides(a, b, c):
    """Check if three sides can form a triangle."""
    if a + b <= c or a + c <= b or b + c <= a:
        st.error("These sides cannot form a triangle. The sum of the lengths of any two sides must be greater than the length of the third side.")
        return False
    return True

def format_result(title, value, formula=None, unit=""):
    """Format result with title, value, and optional formula."""
    st.markdown(f"### {title}")
    st.markdown(f"<h2 style='color: #1E88E5'>{value:.4f} {unit}</h2>", unsafe_allow_html=True)
    if formula:
        st.markdown(f"**Formula**: {formula}")

def create_circle_plot(radius):
    """Create a circle plot."""
    fig, ax = plt.subplots(figsize=(4, 4))
    circle = plt.Circle((0, 0), radius, fill=False, color='blue')
    ax.add_patch(circle)
    ax.set_xlim(-radius*1.2, radius*1.2)
    ax.set_ylim(-radius*1.2, radius*1.2)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(f'Circle with radius {radius}')
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    return fig

def create_rectangle_plot(length, width):
    """Create a rectangle plot."""
    fig, ax = plt.subplots(figsize=(4, 4))
    rectangle = plt.Rectangle((-length/2, -width/2), length, width, fill=False, color='blue')
    ax.add_patch(rectangle)
    ax.set_xlim(-length, length)
    ax.set_ylim(-width, width)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(f'Rectangle {length} x {width}')
    return fig

def create_triangle_plot(a, b, c):
    """Create a triangle plot using the side lengths."""
    # Check if sides can form a triangle
    if not (a + b > c and a + c > b and b + c > a):
        return None
    
    # Semi-perimeter
    s = (a + b + c) / 2
    # Area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # Use law of cosines to find angles
    angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    
    # Coordinates of vertices
    x1, y1 = 0, 0
    x2, y2 = c, 0
    x3 = b * math.cos(angle_A)
    y3 = b * math.sin(angle_A)
    
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'b-')
    
    # Set limits with some padding
    max_coord = max(c, x3, y3) * 1.2
    ax.set_xlim(-max_coord * 0.2, max_coord)
    ax.set_ylim(-max_coord * 0.2, max_coord)
    
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title('Triangle')
    
    # Label sides
    ax.text((x1 + x2) / 2, y1 - max_coord * 0.1, f'c = {c}')
    ax.text((x2 + x3) / 2, (y2 + y3) / 2, f'a = {a}')
    ax.text((x1 + x3) / 2, (y1 + y3) / 2, f'b = {b}')
    
    return fig

def create_square_plot(side):
    """Create a square plot."""
    return create_rectangle_plot(side, side)

def create_trapezium_plot(a, b, h):
    """Create a trapezium plot."""
    fig, ax = plt.subplots(figsize=(4, 4))
    
    if a > b:
        top_left = (-b/2, h)
        top_right = (b/2, h)
        bottom_left = (-a/2, 0)
        bottom_right = (a/2, 0)
    else:
        top_left = (-a/2, h)
        top_right = (a/2, h)
        bottom_left = (-b/2, 0)
        bottom_right = (b/2, 0)
    
    x = [bottom_left[0], bottom_right[0], top_right[0], top_left[0], bottom_left[0]]
    y = [bottom_left[1], bottom_right[1], top_right[1], top_left[1], bottom_left[1]]
    
    ax.plot(x, y, 'b-')
    
    # Set limits with some padding
    max_width = max(a, b)
    ax.set_xlim(-max_width * 0.7, max_width * 0.7)
    ax.set_ylim(-h * 0.2, h * 1.2)
    
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title('Trapezium')
    
    # Label
    if a > b:
        ax.text(0, -0.1 * h, f'a = {a}')
        ax.text(0, h + 0.1 * h, f'b = {b}')
    else:
        ax.text(0, -0.1 * h, f'b = {b}')
        ax.text(0, h + 0.1 * h, f'a = {a}')
    
    ax.text(-max_width * 0.6, h/2, f'h = {h}')
    
    return fig

def create_ellipse_plot(a, b):
    """Create an ellipse plot."""
    fig, ax = plt.subplots(figsize=(4, 4))
    ellipse = plt.Ellipse((0, 0), 2*a, 2*b, fill=False, color='blue')
    ax.add_patch(ellipse)
    ax.set_xlim(-a*1.5, a*1.5)
    ax.set_ylim(-b*1.5, b*1.5)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(f'Ellipse with a={a}, b={b}')
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Draw major and minor axes
    ax.plot([-a, a], [0, 0], 'r--', alpha=0.7)
    ax.plot([0, 0], [-b, b], 'r--', alpha=0.7)
    
    # Label axes
    ax.text(a/2, -0.2*b, 'a', color='red')
    ax.text(0.2*a, b/2, 'b', color='red')
    
    return fig