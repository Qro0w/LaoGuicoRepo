print('')
quest = ('1. A loop enables a particular set of conditions to be executed repeatedly until a condition is satisfied.', '2. A loop has the ability to iterate over the items of any sequence, such as a list or string.', '3. If the else statement is used with a for loop, the else statement is not executed when the loop has exhausted iterating the list.','4. A range function either takes a single number and behaves like a list of numbers.','5. if the else statement is used with while loop[, the else statement is executed when the coondition becomes false.','6. range(n): generates a set of whole numbers starting from 0 to (n-1).','7. range(n): generates a set of whole number starting from start to stop-1.','8. If a sequence contains an expression list, it is evaluated last.','9. len(): provides the total number of elements in the tuple as well as the range() to give us the actual sequence to iterate over.','10. a loop has the ability to iterate over the items of any sequence, such as list or a string.')
quest2 = ('1. It is used inside the loop to exit out of the loop.\n a.  Break Statement b. Continue Statement c. Pass Statement','2. Allows you to bypass the curent iteration of any loop. \n a. Break Statement b. Continue Statement c. Pass Statement','3. Used to indicate "null" or unimplemented functions and loops. \n a. Control Statements b. Continue Statement c. Pass Statement','4. It is useful when we want to terminate the loop as soon as the condition is fulfilled. \n a. Break Statement b. Continue Statement c. Pass Statement','5. It is much like a comment, but the python interpreter treats the pass statements as valid Python Statements while completely ignoring the comment statement. \n a. Break Statement b. Control Statements c. Pass Statement','6. It does not end the loop but rather moves on to the next iteration. \n a. Control Statements b. Continue Statement c. Pass Statement','7. They alter the execution sequence in a loop. \n a. Control Statements b. Continue Statement c. Pass Statement','8. which control statement is being used when the python interpreter ignores the rest of the loop body statements for the current iteration and returns program execution to the very first statement in the loop body? \n a. Control Statements b. Continue Statement c. Pass Statement','9. Considered as a no-operation statement. \n a. Break Statement b. Continue Statement c. Pass Statement','10. It consumes the execution cycle like a valid Python Statement, but nothing actually happens when it is executed. \n a. Break Statement b. Continue Statement c. Pass Statement')
quest3 = ('1. Are used on conditional statements that yield a result of either a TRUE or FALSE value.','2. It determines whether two criteria are True at the same time.','3. It examines multiple conditions, like AND operator. However, it returns True when one or both of the conditions are met. ','4. In case an expression has several operators with the same precedence, Python will evaluate them from the________?','5. Python evaluates logical operators in the order they are listed when you mix them in an expression, which is known as?','6. True if either of the operand is true.','7. It is a programming concept in which the compiler skips the execution of evaluation of some sub-expressions in a logical expression.','8. It summarizes how we combine two logical conditions based on AND, OR, NOT.','9. In testing for Python programs, you may want to check multiple conditions at the same time. to do so, which operator will you use?','10. True if the operand is false.',)
ans = ("T", "F", "F", 'T', 'F', 'T', 'F', 'F', 'T', 'T','A','B','C','A','C','B','A','B','C','C','LOGICAL OPERATORS','AND','OR','LEFT TO RIGHT','OPERATOR PRECEDENCE','OR','SHORT-CIRCUIT EVALUATION','TRUTH TABLE','LOGICAL OPERATORS','NOT')
userscore = 0
userscore2 = 0
userscore3 = 0
num = 0
turns=5
while turns <= 5:
    cred = input('Enter username: ')
    cred2 = input('Enter password: ')
    if cred =='group2' and cred2 =='thor123':
        print()
        print('Logged In!!')
        print ()
        print ("!!!ANSWER ONCE ONLY, ALL CAPITALS ONLY, WRONG SPELLING WRONG!!!")
        print ("")
        print("Module 11")
        print()
        print("!!!TRUE OR FALSE!!!")
        print("Type T or F only!!")
        for q1 in quest:
            print()
            print(q1)
            print()
            userans = input("T/F: ")
            if userans == ans[num]:
                print("Naisu!!!")
                userscore += 1
                num += 1
            else:
                print("No! >:(")
                num += 1
        print()
        print("Module 12")
        print("!!MULTIPLE CHOICE!!")
        print()
        for q2 in quest2:
            print()
            print(q2)
            print()
            userans2 = input("A/B/C: ")
            if userans2 == ans[num]:
                print("Naisu!!!")
                userscore2 += 1
                num += 1
            else:
                print("No! >:(")
                num += 1
        print()
        print("Module 13")
        print("!!IDENTIFICATION!!")
        print("DASHES AND SPACES APPLY!!!")
        print()
        for q3 in quest3:
            print()
            print(q3)
            print()
            userans3 = input("Answer: ")
            if userans3 == ans[num]:
                print("Naisu!!!")
                userscore3 += 1
                num += 1
            else:
                print("No! >:(")
                num += 1
        userscore = int(userscore/len(quest)*10)
        userscore2 = int(userscore2/len(quest2)*10)
        userscore3 = int(userscore3/len(quest3)*10)
        totscore = int(userscore+userscore2+userscore3)
        print()
        print("===========Exam Ended=============")
        print("Your score is: ", str(int(totscore)))
        if totscore <10:
            print("Idiot")
        elif totscore >= 10 and totscore <= 15:
            print("Well, you passed, barely")
        elif totscore >= 16 and totscore <= 20:
            print("Doing great but you can do BETTER")
        elif totscore >= 21 and totscore <= 29:
            print("Sooo close! but your parents aren't proud of you yet")
        elif totscore == 30:
            print("YOU'RE A GENIUS!!!!")
        retry = input("Would you like to try again? Y/N: ")
        if retry == 'Y':
            print()
            continue
        elif retry == 'N':
            print("")
            print("Program Shutting Down")
            print("")
            break
        else:
            print()
            print("Dude, follow instructions")
            print("Program Shutting Down (with shame)")
            print()
            break
    else:
        print()
        print('Invalid!! Attempts left: ', turns)
        print()
        turns -= 1
        if turns == 0:
            print("All attempts depleted, please rerun the program")
            break