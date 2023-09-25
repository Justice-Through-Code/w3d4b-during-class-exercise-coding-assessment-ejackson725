#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14
    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print("Welcome to the Circle shape area calculator!")
#     # User Options
#     Circle = 1
#     Rectangle = 2
#     Triangle = 3
#         
#     # TODO: Using one print statement, use string concatenation to print the options only 
    print("Circle = 1", "Rectangle = 2", "Triangle = 3")
#     # as a single string (make sure to add a space between each option)

#     # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input("Select a shape by entering 1, 2, or 3")
    choice = int(choice)
    
#     # TODO: Convert the variable 'choice' to an integer data type.

   

#     # TODO: Convert the variable 'choice' to an integer data type.


    if choice is int:
    	print(True) 
    
#     # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    
    if choice == 1:  #DO NOT REMOVE THE 'IF'
# #     #     # Calculate the area of a circle
    
#         # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
#         
    # TODO: Convert 'radius' to float.
     
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math. 
        radius = input("What is the radius of the cirlce?")
        radius = float(radius)
        area = circle_pi * radius ** 2
        
    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula to find the area of a rectangle: length times width

        length = input("What is the length of a the rectangle?")
        width = input("What is the width of the rectangle?")
        length = float(length)
        width = float(width)
        area = length * width
    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The formula to find the area of a Triangle: half times base times height
        base = input("What is the base the length?")
        height = input("What is the height of the triangle?")
        base = float(base)
        height = float(height)
        area = (.5 * base) * height
    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
    	print("Invalid choice .")
    if choice in [1, 2, 3]: # DO NOT MODIFY
    	print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    print("Intially I would go to Canvas and accept the assignment, after accepting the assignment I would click on the link that will direct me to github. Copy the assignment using the clipboard. I will move over to VS code then git clone and paste the link after that. git status git add .")

if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
