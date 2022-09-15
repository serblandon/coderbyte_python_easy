'''Questions Marks
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
'''


def QuestionsMarks(strParam):

  a = 0
  b = 0

  ok = 1

  oksum = 0

  for i in range(len(strParam)):
    if strParam[i].isdigit() == True:
      a = int(strParam[i])
      for j in range(i + 1, len(strParam)):
        if strParam[j].isdigit() == True:
          b = int(strParam[j])
          if ( a + b ) == 10:
            cntq = 0
            oksum = 1
            for k in range(i,j):
              if strParam[k] == '?':
                cntq += 1
            if cntq != 3:
              ok = 0
          break

  if ok == 0 or oksum == 0:
    strParam = "false"
  else:
    strParam = "true"

  return strParam

# keep this function call here
print(QuestionsMarks(input()))