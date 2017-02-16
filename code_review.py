# -*- coding: utf-8 -*-
# @Author: Maria Villalobos
# @Date:   2017-02-16 13:37:47
# @Last Modified by:   mati
# @Last Modified time: 2017-02-16 13:42:05
# This example was extracted from http://web.mit.edu/6.005/www/sp15/classes/03-code-review/
# and translated to Python for the purpose of this course

# Write a new version of the Day_Of_Year and leap functions
# by iteratively taking into account the following elements:

# THINGS TO TAKE INTO ACCOUNT
# 1. Don’t Repeat Yourself
# 2. Comments Where Needed
# 3. Fail fast
# 4. Avoid Magic Numbers
# 5. One purpose for each variable
# 6. Use Good Names (take naming conventions into account)
# 7. Use Whitespace to Help the Reader


def Day_Of_Year(Month, Day_Of_Month, Year):
    if (Month == 2):
        Day_Of_Month += 31
    elif (Month == 3):
        Day_Of_Month += 59
    elif (Month == 4):
        Day_Of_Month += 90
    elif (Month == 5):
        Day_Of_Month += 31 + 28 + 31 + 30
    elif (Month == 6):
        Day_Of_Month += 31 + 28 + 31 + 30 + 31
    elif (Month == 7):
        Day_Of_Month += 31 + 28 + 31 + 30 + 31 + 30
    elif (Month == 8):
        Day_Of_Month += 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif (Month == 9):
        Day_Of_Month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif (Month == 10):
        Day_Of_Month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif (Month == 11):
        Day_Of_Month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif (Month == 12):
        Day_Of_Month += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 31
    return Day_Of_Month


def leap(y):
    tmp = str(y)
    if (tmp[2] == '1' or tmp[2] == '3' or tmp[2] == 5 or tmp[2] == '7' or tmp[2] == '9'):
        if (tmp[3] == '2' or tmp[3] == '6'):
            return True
        else:
            return False
    else:
        if (tmp.charAt(2) == '0' and tmp.charAt(3) == '0'):
            return False
        if (tmp[3] == '0' or tmp[3] == '4' or tmp[3] == '8'):
            return True
    return False
