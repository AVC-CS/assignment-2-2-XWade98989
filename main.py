def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int(input('Enter celsius: '))
    fahrenheit = celsius * 9/5 + 32
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    print("fahrenheit:", fahrenheit)
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
