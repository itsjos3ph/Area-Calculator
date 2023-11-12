#user chooses either traingle or cube
#either one calculates the area of choice
#outputs the answer

Choice = input("Which would you like to find the area of... 'Square' or 'Triangle': ")

if Choice == "Square":
    SquareLength = int(input("Enter the side length of your Square: "))
    print("The area of your square is: ", SquareLength **2)

elif Choice == "Triangle":
    TriangleLength = int(input("Enter the length of your Triangle: "))
    TriangleWidth = int(input("Enter the width of your Triangle: "))
    print("The area of your Triangle is: ", (TriangleLength * TriangleWidth)/2 )

else: 
    print("Error, please try typing it again :D")