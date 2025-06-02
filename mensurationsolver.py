import math  # Adding math module for more precise calculations

PI = math.pi  # Define PI as a constant

shapes = int(input("1.CIRCLE\n"
"2.TRIANGLE\n"
"3.RECTANGLE\n"
"4.ELLIPSE\n"
"5.SQUARE\n"
"6.RIGHT ANGLE TRIANGLE\n"
"7.SOLID CONE\n"
"8.SOLID CYLINDER\n"
"9.SOLID SPHERE\n"
"10.HOLLOW SPHERE\n"
"11.HOLLOW CONE\n"
"12.HOLLOW CYLINDER\n"
"13.CUBE\n"
"14.CUBOID\n"
"15.TRAPEZIUM\n"
"ENTER YOUR CHOICE: "))


if shapes==1:
    print("YOU HAVE CHOSEN CIRCLE")
    p=int(input("1.DIAMETER OF CIRCLE\n"
    "2.CIRCUMFERENCE OF CIRCLE\n"
    "3.AREA OF CIRCLE\n"
    "ENTER YOUR CHOICE: "))  
    r=float(input("ENTER THE RADIUS OF GIVEN CIRCLE: "))
    if p==1:
        print("DIAMETER OF GIVEN CIRCLE IS= ", 2*r)
    elif p==2:
        print("CIRCUMFERENCE OF CIRCLE = ", 2*PI*r)  # Using PI constant
    elif p==3:
        print("AREA OF GIVEN CIRCLE = ", PI*r*r)  # Using PI constant
    else:
        print("WRONG OPTION CHOSEN") 


elif shapes==2:
    print("YOU HAVE CHOSEN TRIANGLE")
    t=int(input("1.SCALENE TRIANGLE\n"
    "2.ISOSCELES TRIANGLE\n"  
    "3.EQUILATERAL TRIANGLE\n"
    "ENTER YOUR CHOICE: "))  

    if t==1:
        print("YOU HAVE CHOSEN SCALENE TRIANGLE")
        s1=float(input("ENTER THE LENGTH OF FIRST SIDE: "))
        s2=float(input("ENTER THE LENGTH OF SECOND SIDE: "))
        s3=float(input("ENTER THE LENGTH OF THIRD SIDE: "))
        s=(s1+s2+s3)/2
        A=(s*(s-s1)*(s-s2)*(s-s3))**0.5
        print("THE AREA OF THE GIVEN SCALENE TRIANGLE = ",A)

    elif t==2:
        print("YOU HAVE CHOSEN ISOSCELES TRIANGLE")  
        s1=float(input("ENTER THE LENGTH OF COMMON SIDE: "))
        s2=float(input("ENTER THE LENGTH OF REMAINING SIDE: "))
        A=0.5*s2*((s1*s1 - (s2*s2)/4))**0.5  
        print("THE AREA OF GIVEN ISOSCELES TRIANGLE = ",A)  

    elif t==3:
        print("YOU HAVE CHOSEN EQUILATERAL TRIANGLE")
        s=float(input("ENTER THE LENGTH OF SIDE: "))
        A=(math.sqrt(3)/4)*s*s  
        print("THE AREA OF GIVEN EQUILATERAL TRIANGLE IS = ",A)
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==3:
    print("YOU HAVE CHOSEN RECTANGLE") 
    l=float(input("ENTER THE LENGTH OF RECTANGLE: "))
    b=float(input("ENTER THE BREADTH OF RECTANGLE: "))
    p=int(input("1.PERIMETER OF RECTANGLE\n"
    "2.AREA OF RECTANGLE\n"
    "ENTER YOUR CHOICE: "))  
    if p==1:
        P= 2*(l+b)
        print("THE PERIMETER OF GIVEN RECTANGLE = ",P)
    elif p==2:
        A=(l*b)
        print("THE AREA OF GIVEN RECTANGLE IS = ",A)           
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==4:
    print("YOU HAVE CHOSEN ELLIPSE")
    a=float(input("ENTER THE LENGTH OF SEMI MAJOR AXIS: "))
    b=float(input("ENTER THE LENGTH OF SEMI MINOR AXIS: "))
    p=int(input("1.AREA OF ELLIPSE\n" 
    "ENTER YOUR CHOICE: "))  
    if p==1:
        A=(PI*a*b)  # Using PI constant
        print("THE AREA OF ELLIPSE = ",A)
    else:
        print("WRONG OPTION CHOSEN") 


elif shapes==5:
    print("YOU HAVE CHOSEN SQUARE")
    p=int(input("1.PERIMETER OF SQUARE\n"
    "2.AREA OF SQUARE\n" 
    "ENTER YOUR CHOICE: "))  
    s=float(input("ENTER THE SIDE LENGTH: "))
    if p==1:
        print("THE PERIMETER OF GIVEN SQUARE = ", 4*s) 
    elif p==2:
        print("THE AREA OF GIVEN SQUARE = ", s*s) 
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==6:
    print("YOU HAVE CHOSEN RIGHT ANGLED TRIANGLE") 
    P=int(input("1.PERIMETER OF RIGHT ANGLED TRIANGLE\n"
    "2.AREA OF RIGHT ANGLED TRIANGLE\n"
    "ENTER YOUR CHOICE: "))  
    if P==1:
        p=float(input("ENTER THE PERPENDICULAR LENGTH: "))
        b=float(input("ENTER THE BASE LENGTH: "))
        h=float(input("ENTER THE HYPOTENUSE LENGTH: "))
        se=p+b+h
        print("THE PERIMETER OF GIVEN TRIANGLE = ",se)

    elif P==2:
        b=float(input("ENTER THE BASE LENGTH: "))
        h=float(input("ENTER THE HEIGHT/PERPENDICULAR LENGTH OF TRIANGLE: "))
        a=0.5*b*h
        print("THE AREA OF GIVEN TRIANGLE = ",a)

    else:
        print("WRONG OPTION CHOSEN")    

elif shapes==7:
    print("YOU HAVE CHOSEN SOLID CONE")
    P=int(input("1.TSA\n"
                "2.CSA\n"
                "3.VOLUME\n"
                "ENTER YOUR CHOICE: "))
    
    if P==1:
        print("YOU HAVE CHOSEN TSA")
        r=float(input("ENTER THE RADIUS OF CONE: "))
        l=float(input("ENTER THE SLANT HEIGHT/LENGTH OF CONE: "))
        A=(PI*r*r)+(PI*r*l)  # Using PI constant
        print("THE TOTAL SURFACE AREA OF THE GIVEN CONE IS: ", A)

    elif P==2: 
        print("YOU HAVE CHOSEN CSA") 
        r=float(input("ENTER THE RADIUS OF CONE: "))      
        l=float(input("ENTER THE SLANT HEIGHT/LENGTH OF CONE: "))
        A=(PI*r*l)  # Using PI constant
        print("THE CURVED SURFACE AREA OF THE GIVEN CONE IS: ", A)

    elif P==3:  
        print("YOU HAVE CHOSEN VOLUME")
        r=float(input("ENTER THE RADIUS OF CONE: "))
        h=float(input("ENTER THE HEIGHT OF CONE: "))
        V=(PI*r*r*h)/3  # Using PI constant
        print("THE VOLUME OF GIVEN CONE = ", V)
    
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==8:
    print("YOU HAVE CHOSEN SOLID CYLINDER")
    P=int(input("1.TSA\n"
                "2.CSA\n"
                "3.VOLUME\n"
                "ENTER YOUR CHOICE: "))
    if P==1:
        print("YOU HAVE CHOSEN TSA")
        h=float(input("ENTER THE HEIGHT OF CYLINDER: "))   
        r=float(input("ENTER THE RADIUS OF CYLINDER: "))
        A=(2*PI*r)*(r+h)  # Using PI constant
        print("THE TOTAL SURFACE AREA OF GIVEN CYLINDER = ", A)

    elif P==2:  
        print("YOU HAVE CHOSEN CSA")
        h=float(input("ENTER THE HEIGHT OF CYLINDER: "))   
        r=float(input("ENTER THE RADIUS OF CYLINDER: "))
        A=2*PI*r*h  # Using PI constant
        print("THE CURVED SURFACE AREA OF GIVEN CYLINDER = ", A)

    elif P==3:  
        print("YOU HAVE CHOSEN VOLUME")
        r=float(input("ENTER THE RADIUS OF CYLINDER: "))
        h=float(input("ENTER THE HEIGHT OF CYLINDER: "))   
        V=PI*r*r*h  # Using PI constant
        print("THE VOLUME OF GIVEN CYLINDER = ", V)
    
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==9:
    print("YOU HAVE CHOSEN SOLID SPHERE")
    P=int(input("1.SA\n"
                "2.VOLUME\n"
                "ENTER YOUR CHOICE: "))
    if P==1:
        print("YOU HAVE CHOSEN SA")
        r=float(input("ENTER THE RADIUS OF SOLID SPHERE: "))
        A=4*PI*r*r  # Using PI constant
        print("THE SURFACE AREA OF THE GIVEN SPHERE = ", A)

    elif P==2:  
        print("YOU HAVE CHOSEN VOLUME")
        r=float(input("ENTER THE RADIUS OF SOLID SPHERE: "))
        V=(4*PI*r*r*r)/3  # Using PI constant
        print("THE VOLUME OF GIVEN SPHERE = ", V)
    
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==13:
    print("YOU HAVE CHOSEN CUBE")
    P=int(input("1.TSA\n"  
                "2.CSA\n"
                "3.VOLUME\n"
                "4.DIAGONAL\n"
                "ENTER YOUR CHOICE: "))
    if P==1:
        print("YOU HAVE CHOSEN TSA")
        s=float(input("ENTER THE SIDE LENGTH OF CUBE: "))
        A=6*s*s
        print("THE TOTAL SURFACE AREA OF THE GIVEN CUBE IS: ", A)

    elif P==2:  
        print("YOU HAVE CHOSEN CSA") 
        s=float(input("ENTER THE SIDE LENGTH OF CUBE: "))  
        A=4*s*s
        print("THE CURVED SURFACE AREA OF THE GIVEN CUBE IS: ", A) 

    elif P==3:  
        print("YOU HAVE CHOSEN VOLUME")
        s=float(input("ENTER THE SIDE LENGTH OF CUBE: "))
        V=s*s*s
        print("THE VOLUME OF THE GIVEN CUBE IS: ", V)

    elif P==4: 
        print("YOU HAVE CHOSEN DIAGONAL") 
        s=float(input("ENTER THE SIDE LENGTH OF CUBE: ")) 
        D=math.sqrt(3)*s  
        print("THE DIAGONAL OF THE GIVEN CUBE IS: ", D)  
    
    else:
        print("WRONG OPTION CHOSEN")

elif shapes==14:
    print("YOU HAVE CHOSEN CUBOID")
    P=int(input("1.TSA\n"  
                "2.CSA\n"
                "3.VOLUME\n"
                "4.DIAGONAL\n"
                "ENTER YOUR CHOICE: "))   

    if P==1:
        print("YOU HAVE CHOSEN TSA") 
        l=float(input("ENTER THE LENGTH OF CUBOID: "))
        b=float(input("ENTER THE BREADTH OF CUBOID: "))
        h=float(input("ENTER THE HEIGHT OF CUBOID: "))  
        A=2*((l*b)+(b*h)+(h*l))
        print("THE TOTAL SURFACE AREA OF CUBOID IS: ", A)

    elif P==2: 
        print("YOU HAVE CHOSEN CSA")
        l=float(input("ENTER THE LENGTH OF CUBOID: "))
        b=float(input("ENTER THE BREADTH OF CUBOID: "))
        h=float(input("ENTER THE HEIGHT OF CUBOID: "))  
        A=2*(l+b)*h
        print("THE CURVED SURFACE AREA OF CUBOID IS: ", A)

    elif P==3: 
        print("YOU HAVE CHOSEN VOLUME")
        l=float(input("ENTER THE LENGTH OF CUBOID: "))
        b=float(input("ENTER THE BREADTH OF CUBOID: "))
        h=float(input("ENTER THE HEIGHT OF CUBOID: "))
        V=l*b*h
        print("THE VOLUME OF THE GIVEN CUBOID IS: ",V)

    elif P==4:  
        print("YOU HAVE CHOSEN DIAGONAL")
        l=float(input("ENTER THE LENGTH OF CUBOID: "))
        b=float(input("ENTER THE BREADTH OF CUBOID: "))
        h=float(input("ENTER THE HEIGHT OF CUBOID: "))      
        D=((l*l)+(b*b)+(h*h))**0.5
        print("THE DIAGONAL OF THE GIVEN CUBOID IS: ",D)
    
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==15:
    print("YOU HAVE CHOSEN TRAPEZIUM")
    P=int(input("1.AREA\n"
            "ENTER YOUR CHOICE: "))
    if P==1:
        print("YOU HAVE CHOSEN AREA")
        a=float(input("ENTER THE LENGTH OF ONE PARALLEL SIDE: "))
        b=float(input("ENTER THE LENGTH OF ANOTHER PARALLEL SIDE: "))
        h=float(input("ENTER THE HEIGHT: "))
        A=((a+b)*h)/2
        print("THE AREA OF GIVEN TRAPEZIUM IS: ", A)
    
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==10:
    print("YOU HAVE CHOSEN HOLLOW SPHERE")
    P=int(input("1.THICKNESS\n"
                "2.OUTER SURFACE AREA\n"
                "3.INNER SURFACE AREA\n"
                "4.TOTAL SURFACE AREA\n"
                "ENTER YOUR CHOICE: "))
    if P==1:
        print("YOU HAVE CHOSEN THICKNESS")
        R=float(input("ENTER THE OUTER RADIUS: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        T=R-r     
        print("THE THICKNESS OF THE GIVEN HOLLOW SPHERE IS: ",T)

    elif P==2:  
        print("YOU HAVE CHOSEN OUTER SURFACE AREA") 
        R=float(input("ENTER THE OUTER RADIUS: "))        
        A=4*PI*R*R  # Using PI constant
        print("THE OUTER SURFACE AREA OF GIVEN SPHERE IS: ", A)

    elif P==3:  
        print("YOU HAVE CHOSEN INNER SURFACE AREA")
        r=float(input("ENTER THE INNER RADIUS: "))
        A=4*PI*r*r  # Using PI constant
        print("THE INNER SURFACE AREA OF THE GIVEN SPHERE IS: ",A)

    elif P==4:  
        print("YOU HAVE CHOSEN TOTAL SURFACE AREA")
        R=float(input("ENTER THE OUTER RADIUS: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        A=(4*PI*R*R)+(4*PI*r*r)  # Using PI constant
        print("THE TOTAL SURFACE AREA OF THE GIVEN HOLLOW SPHERE IS: ",A)  
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==12:
    print("YOU HAVE CHOSEN HOLLOW CYLINDER")
    P=int(input("1.THICKNESS\n"
                "2.VOLUME\n"
                "3.TOTAL SURFACE AREA\n"
                "4.CURVED SURFACE AREA\n"
                "ENTER YOUR CHOICE: "))
    if P==1:
        print("YOU HAVE CHOSEN THICKNESS")
        R=float(input("ENTER THE OUTER RADIUS: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        T=R-r     
        print("THE THICKNESS OF THE GIVEN HOLLOW CYLINDER IS: ",T)

    elif P==2:  
        print("YOU HAVE CHOSEN VOLUME")  
        R=float(input("ENTER THE OUTER RADIUS: "))
        h=float(input("ENTER THE HEIGHT: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        V=PI*h*(R*R-r*r)  # Using PI constant
        print("THE VOLUME OF GIVEN HOLLOW CYLINDER: ", V)

    elif P==3:  
        print("YOU HAVE CHOSEN TOTAL SURFACE AREA")
        R=float(input("ENTER THE OUTER RADIUS: "))
        h=float(input("ENTER THE HEIGHT: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        A=2*PI*h*(R+r)+2*PI*(R*R-r*r)  # Using PI constant
        print("THE TOTAL SURFACE AREA OF THE GIVEN HOLLOW CYLINDER IS: ", A) 

    elif P==4:  
        print("YOU HAVE CHOSEN CURVED SURFACE AREA")
        R=float(input("ENTER THE OUTER RADIUS: "))
        h=float(input("ENTER THE HEIGHT: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        A=2*PI*h*(R+r)  
        print("THE CURVED SURFACE AREA OF THE GIVEN HOLLOW CYLINDER IS: ", A) 
    
    else:
        print("WRONG OPTION CHOSEN")


elif shapes==11:
    print("YOU HAVE CHOSEN HOLLOW CONE")
    P=int(input("1.SLANT HEIGHT\n"
                "2.VOLUME\n"
                "3.TOTAL SURFACE AREA\n"
                "4.CURVED SURFACE AREA\n"
                "ENTER YOUR CHOICE: "))
    if P==1:
        print("YOU HAVE CHOSEN SLANT HEIGHT")
        R=float(input("ENTER THE OUTER RADIUS: "))
        h=float(input("ENTER THE HEIGHT: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        S=(h*h+(R-r)**2)**0.5
        print("THE SLANT HEIGHT OF GIVEN HOLLOW CONE IS: ", S)  

    elif P==2: 
        print("YOU HAVE CHOSEN VOLUME")
        R=float(input("ENTER THE OUTER RADIUS: "))
        h=float(input("ENTER THE HEIGHT: "))
        r=float(input("ENTER THE INNER RADIUS: ")) 
        V=(PI*h*(R*R+R*r+r*r))/3   #using PI constant
        print("THE VOLUME OF GIVEN HOLLOW CONE IS: ", V)  

    elif P==3:  
        print("YOU HAVE CHOSEN TOTAL SURFACE AREA")
        R=float(input("ENTER THE OUTER RADIUS: "))
        h=float(input("ENTER THE HEIGHT: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        l = (h*h + R*R)**0.5  
        A = PI*R*(R+l) + PI*r*(r+l) 
        print("THE TOTAL SURFACE AREA OF THE GIVEN HOLLOW CONE IS: ", A)

    elif P==4: 
        print("YOU HAVE CHOSEN CURVED SURFACE AREA")
        R=float(input("ENTER THE OUTER RADIUS: "))
        h=float(input("ENTER THE HEIGHT: "))
        r=float(input("ENTER THE INNER RADIUS: "))
        l = (h*h + R*R)**0.5  
        A = PI*R*l + PI*r*l  
        print("THE CURVED SURFACE AREA OF THE GIVEN HOLLOW CONE IS: ", A)
    
    else:
        print("WRONG OPTION CHOSEN")

else:
    print("INVALID SHAPE SELECTED. PLEASE TRY AGAIN.") 
