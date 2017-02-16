# -*- coding: utf-8 -*-
# @Author: Maria Villalobos
# @Date:   2017-02-16 13:37:47
# @Last Modified by:   mati
# @Last Modified time: 2017-02-16 17:11:06
# Advanced Python Programming - Lab 4
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

from datetime import timedelta


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


def get_crossover_signal(self, on_date):
    '''This is another example of Smelly Code from the Test- Driven Python Development book
    by Siddharta Govindaraj Chapter 3'''
    cpl = []
    for i in range(11):
        chk = on_date.date() - timedelta(i)
        for price_event in reversed(self.price_history):
            if price_event.timestamp.date() > chk:
                pass
            if price_event.timestamp.date() == chk:
                cpl.insert(0, price_event)
                break
            if price_event.timestamp.date() < chk:
                cpl.insert(0, price_event)
                break

            # Return NEUTRAL signal
            if len(cpl) < 11:
                cpl.insert(0, price_event)
                break

            # BUY signal
            if sum([update.price for update in cpl[-11:-1]]) / 10 \
                    > sum([update.price for update in cpl[-6:-1]]) / 5 \
                    and sum([update.price for update in cpl[-10:]]) / 10 \
                    < sum([update.price for update in cpl[-5:]]) / 5:
                        return 1
            # BUY signal
            if sum([update.price for update in cpl[-11:-1]]) / 10 \
                    < sum([update.price for update in cpl[-6:-1]]) / 5 \
                    and sum([update.price for update in cpl[-10:]]) / 10 \
                    > sum([update.price for update in cpl[-5:]]) / 5:
                        return -1

            # NEUTRAL signal
            return 0
