#Codsoft internship task1 simple calculator
inputnum1 = float(input("Enter the first input number: "))
inputnum2 = float(input("Enter the second input number: "))
operation = input("Choose an operation (+, -, *, /): ")


result = (
    inputnum1 + inputnum2 if operation == '+' else
    inputnum1 - inputnum2 if operation == '-' else
    inputnum1 * inputnum2 if operation == '*' else
    inputnum1 / inputnum2 if operation == '/' and inputnum2 != 0 else
    "Error: Invalid operation or division by zero."
)


print("Result for the given input:", result)
