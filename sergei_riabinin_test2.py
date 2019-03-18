def string_comparison():
    """
        Task:
        Write a software library that accepts 2 version string as input and returns
        whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”.
        Provide all test cases you could think of.


        Returning result of string comparison
        Testcases:
        1. string and int ( 'banana' and 10 )
        2. different strings ( 'banana' and 'banan' )
        3. lowercase and uppercase same string ( 'Banana' and 'banana' )
        4. int and float ( 10 and 10.1 )
        5. float and float ( 1.2 and 1.3 )
        6. values not None

    :return: result
    """

    # enter both strings
    value1 = input("Enter first string: ")
    value2 = input("Enter second string: ")

    result = None

    if value1 or value2 is not None:

        if value1 < value2:
            result = '{} is less than {}'.format(value1, value2)
        elif value1 == value2:
            result = '{} is equal {}'.format(value1, value2)
        else:
            result = '{} is greater than {}'.format(value1, value2)

    print(result)
    return result

string_comparison()
