import calendar
from colorama import Fore, Style
yy = 2023
def display_calendar(yy, mm, hdays):
    cal = calendar.monthcalendar(yy, mm)
    print(calendar.month_name[mm], yy)
    print("Mo Tu We Th Fr Sa Su")
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end = " ")
            elif day in hdays:
                print(f"{Fore.RED}{day:2}{Style.RESET_ALL}", end = " ")
            else:
                print(f"{day:2}", end = " ")
        print(" ")
while True:
    print("")
    print ("Subject Codes", "                     ", "Months")
    print ("   ")
    print ("1. ITE 260", "               ", "1: January", "   ","7: July")
    print ("2. ITE 366", "               ", "2: February", "  ","8: August")
    print ("3. GEN 001", "               ", "3: March", "     ","9: September")
    print ("4. GEN 002", "               ", "4: April", "     ","10: October")
    print ("5. GEN 006", "               ", "5: May", "       ","11: November")
    print ("6. MAT 152", "               ", "6: June", "      ","12: December")
    print ("7. NST 021")
    print ("8. PED 030")
    print ("   ")
    mm = int(input("Enter month: "))
    print ("   ")
    print (" (1/2/3/4/5/6/7/8)")
    choice = input("Enter Subject Code Number:")
    if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
        if choice == ('1'):
            print("")
            print("Computer Programming 1")
            print("Destura, Jimuel")
            print("September 4 - October 28 2023")
            print("Tuesday/Friday")
            print("9am/8am - 12pm")
            print("1pm - 4pm")
            print("")
            if mm == (9):
                hdays = [1, 5, 12, 19, 26, 8, 15, 22, 29]
            elif mm == (10):
                hdays = [3, 10, 17, 24, 31, 6, 13, 20, 27]
            else:
                hdays = []
                breakpoint
        elif choice == ('2'):
            print("")
            print("Introduction to Computing")
            print("(Including IT Fundamentals)")
            print("Tabon, Jerry")
            print("July 31 - September 30 2023")
            print("Monday/Wednesday/Saturday")
            print("8am - 12pm")
            print("1pm - 4pm")
            print("")
            if mm == (7):
                hdays = [31]
            elif mm == (8):
                hdays = [7,14,21,28,2,9,16,30,5,12,19,26,23]
            elif mm == (9):
                hdays = [4,11,18,25,6,13,20,27,2,9,16,23,30]
            else:
                hdays = []
                breakpoint
        elif choice == ('3'):
            print("")
            print("Purposive Communication")
            print("Tabanao, Rechel")
            print("July 31 - August 29 2023")
            print("Tuesday/Friday")
            print("9am - 12pm")
            print("1pm - 4pm")
            print("")
            if mm == (8):
                hdays = [1,8,15,22,29,4,11,18,25]
            else:
                hdays = []
                breakpoint
        elif choice == ('4'):
            print("")
            print("Understanding The Self")
            print("Degamo, Joy Tiffany")
            print("September 4 - September 30 2023")
            print("Wednesday/Saturday")
            print("9am - 12pm")
            print("1pm - 4pm")
            print("")
            if mm == (9):
                hdays = [6,13,20,27,2,9,16,23,39]
            else:
                hdays = []
                breakpoint
        elif choice == ('5'):
            print("")
            print("Ethics")
            print("Bolso, Roland N.")
            print("July 31 - August 29 2023")
            print("Monday/Thursday")
            print("9am - 12pm")
            print("1pm - 4pm")
            print("")
            if mm == (8):
                hdays = [7,14,21,28,3,10,17,24,31]
            else:
                hdays = []
                breakpoint
        elif choice == ('6'):
            print("")
            print("Mathematics in the Modern World")
            print("N/A")
            print("October 2 - October 28 2023")
            print("Wednesday/Saturday")
            print("9am - 12pm")
            print("1pm - 4pm")
            print("9pm - 12pm")
            print("")
            if mm == (10):
                hdays = [4,11,18,25,7,14,21,28]
            else:
                hdays = []
                breakpoint
        elif choice == ('7'):
            print("")
            print("National Service Training Program 1")
            print("Bolso, Roland N.")
            print("July 31 - October 28 2023")
            print("Monday/Thursday")
            print("4pm - 5:30pm")
            print("")
            if mm == (7):
                hdays = [31]
            elif mm == (8):
                hdays = [7,14,21,28,3,10,17,24,31]
            elif mm == (9):
                hdays = [4,11,18,25,7,14,21,28]
            elif mm == (10):
                hdays = [2,9,16,23,30,5,12,19,26]
            else:
                hdays = []
                breakpoint
        elif choice == ('8'):
            print("")
            print("Physical Activities Toward Health and Fitness", "(PATHFit 1)")
            print("Movement Competency Training")
            print("Garcia, Marino")
            print("July 31 - October 28 2023")
            print("Saturday")
            print("7am - 9am")
            print("") 
            if mm == (8):
                hdays = [5,12,19,26]
            elif mm == (9):
                hdays = [2,9,16,23,30]
            elif mm == (10):
                hdays = [7,14,21,28]
            else:
                hdays = []
                breakpoint
    else:
        print("")
        print("Subject does not exist")
        print("please rerun the code")
        print("")
        break
    display_calendar (yy, mm, hdays)
    print()
    print("(Yes/No)")
    endorcontinue = input("Find a different subject?:  ")
    if endorcontinue == ("Yes"):
                breakpoint
    elif endorcontinue == ("No"):
        break
    else:
        print("   ")
        print("Invalid input (or add capitals)")
        print("Please rerun the code")
        print("   ")
        break
    print("")