'''Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
'''

def CodelandUsernameValidation(strParam):
    cont = 1

    if len(strParam) < 4 or len(strParam) > 25:
        cont = 0

    if (strParam[0] < 'a' or strParam[0] > 'z') and (strParam[0] < 'A' or strParam[0] > 'Z'):
        cont = 0

    for char in range(len(strParam)):
        if strParam[char] != '_' and (strParam[0] < 'a' or strParam[0] > 'z') and (
                strParam[0] < 'A' or strParam[0] > 'Z') and strParam[char].isdigit() == False:
            cont = 0
            break

    if strParam[len(strParam) - 1] == '_':
        cont = 0

    if cont == 0:
        strParam = "false"
    else:
        strParam = "true"

    return strParam

x = input("input here")

# keep this function call here
print(CodelandUsernameValidation(x))