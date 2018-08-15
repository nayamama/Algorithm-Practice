"""
deriv(B) takes the list B containing each parameter and returns the derivative of the polynomial B as a string like
" 9y**2 + -20y**3 ". While we execute this function that returns a string >for display< ... we are filling a list called
B_drv , which is a list containing the parameters of the differentiated function
the function calc_deriv() is for calculating the differentiated function with 'y' as a number
"""

B = input('please enter the polynomial of B in the form ( 3y**3 + -5y**4 + 30) : ')
while '+' in B:
    index = B.index('+')
    B = B.replace('+', ' ')
B = B.split()

B_drv = []
print(B)


def deriv(B):
    for parameter in B:
        if 'y' in parameter:
            index_y = parameter.index('y')
            multiply = parameter[0:index_y]
            # multiply refers to the number multiplied by 'y' , which is '9' in '9y**2'
            if multiply == '':
                multiply = '1'  # in case the user wrote 'y**3' instead of '1y**3'
            power = parameter[index_y + 3:]
            # power refers to the power of 'y' , which is '2' in '9y**2'
            if power != '0':
                drv_parameter = str(float(multiply) * float(power)) + 'y**' + str(float(power) - 1)
            else:
                drv_parameter = str(0)  # in case the user wrote a parameter '4y**0' instead of '4'
            B_drv.append(drv_parameter)  # filling the list
        else:  # if there is no 'y' in the parameter
            drv_parameter = str(0)
            B_drv.append(drv_parameter)
    result = ' + '.join(B_drv)  # for display
    return result


def calc_deriv(B_drv):
    y_value = input('please input the value of y : ')
    for parameter in B_drv:
        index_parameter = B_drv.index(parameter)
        B_drv[index_parameter] = parameter.replace('y', '*' + y_value)  # to replace '4y**3' with '4*number**3'
        B_drv[index_parameter] = str(eval(B_drv[index_parameter]))
    result = eval(' + '.join(B_drv))
    return result


print('The derivative of B is : ' + deriv(B))
print('Do you want to input the value of y into the derivative ? (y/n)')
answer = input()
if answer == 'y':
    print('The final result is : ' + str(calc_deriv(B_drv)))
