#name = input("What's your name? " )
#Fi_color = input("What's your favorite color? ") + ' white😲😍'
#color_cpy= ' and for me is just ('+Fi_color[0:4]+')'
#print("Hi bro, what's up, Ah I think that "+name[0:5]+" likes "+Fi_color+color_cpy)

#print("Ok, let's do some games🎮🕹️")
#print("let's guess your age")
#Bo_year = int(input("when were you born? "))
#age = 2025 - Bo_year 
#print("you are "+str(age)+" years old😁")
#print("Now...🤔")
#weight = input("please give me your weight in pounds? ")
#weight_kg = float(weight)*0.45
#print("your weight in Kilograms is equal to: "+str(weight_kg))
#red=input()
#print(type(int(red)))
#print(9/3,"$$",9//3,"$$",9%3,"$$",9**2,"$$",9+3,"$$",9-3,"$$",9*3)
#name_1= input("what is your name? ")
#Fa_name_1= input("what's your family name? ")
#text_msg= f'{name_1[0:5]} ({Fa_name_1}) is a full stack developer.'
#len(text_msg) || 'word' in text_msg || text_msg.upper(),type(text_msg)
#text_msg.lower() || text_msg.capitalize() || text_msg.title()
#text_msg.swapcase() || text_msg.replace('full stack','full stack developer')
#text_msg.find('full stack') || text_msg.index('I')
#text_msg.startswith('full stack') || text_msg.endswith('developer.')
#text_msg.count('full stack developer.') || text_msg.split(' ')
#print('\nWarm-up Drils!!.')
#NAME= input("what's your name? ")
#NAME= NAME.capitalize()
#print(f"Hello, {NAME}! welcome to Python.\n")

#print('Price Calculator!!')
#pro_name = input("what's your product's name? ")
#price = float(input("How much is it? "))
#quantity = int(input("How many did you buy? "))
#total = price*quantity
#print(f'you bought {type(quantity)} of {type(pro_name)} at {type(price)}$ each, So Total: {type(total)}$\n')

#print('String Analyzer!! ')
#msg= input("Please,write a text message: ")
#print(msg.isdigit())
#print(f'Your sentence has {len(msg)} characters and {msg.split()} words!!😎')
#print(f"The sentence in uppercase: {msg.upper()} 👍")
#rint(f"The sentence in lowercase: {msg.lower()} 👍\n")

#print("Contact Info Cleaner!!")
#name= input('Enter your name: ').capitalize()
#email= input('Enter your email: ')
#age= input('Enter your age: ')

#if  not age.isdigit():
#    print('Invalid age!! ')
#if "@gmail.com" not in email:
#    print('Invalid email!! ')
#else:
#    print(f'{name} (age: {age}) -Email: {email}\n')
#print('Temperture Converter!! ')
#cel_degree= float(input('Enter the temperture in Celsuis: '))
#feh_degree= cel_degree*1.8 +32
#print(f'The temperture in Fehrenheit degree: {feh_degree:.2f} F\n')
#print('Student Grade Report!! ')     
#std_name= input('Enter your full name: ').capitalize()
#score_1= float(input('Enter 1st score: '))
#score_2= float(input('Enter 2nd score: '))    
#score_3= float(input('Enter 3rd score: ')) 
#average= (score_1+score_2+score_3)/3

#print(f'Student: {std_name}')
#print(f'Average: {average:.2f}')

#if average>=10:
#    print('Passed🎉\n')
#else: 
#    print(f'Failed!!😢\n')

#print('Price of a house in $1M!!')
#price= 10**6
#good_credit= input('do you have a good credit(yes or no): ')
#if good_credit== "yes":
#  print(f"Down payment: ${price*0.1:,.2f} !! ")     
#else:
#   print(f"Down payment: ${price*0.2:,.2f} !! ")

#import math
#print('\nAbsolute Deffirence!! ')
# This program calculates the absolute difference between two numbers.
#n1= float(input('enter the first number: '))
#n2= float(input('enter the second number: '))
#abs_def= abs(n1-n2)
#print(f'the absolute deffirence between {n1} and {n2} is: {abs_def:+,.2f}\n')


#print('Rounding Calculator!! ')
#number= float(input('Enter a decimal number: '))
#num_round= round(number)
#print(f'\nThe rounded number: {num_round}')
#print(f'The rounded number to 2 decimal places: {round(number,2)}')


#radius= float(input('Please enter the raduis of the circle in (cm): '))
#area= (math.pi*pow(radius,2))*pow(10,-2)
#perimeter=(math.pi*2*radius)*pow(10,-2)
#print(f'The Area: {area:,.3f} m²')
#print(f'The Perimeter: {perimeter:,.3f} m')


#username= input('Enter your name: ')
#len(username)
#weight=float(input('Enter your weight: '))
#choice=input('type (l)for bs, (k)for kg: ')
#if len(username)<3:
#    print('name must be at least of 3 characters!!')
#elif len(username)>50:
#    print('name can be a maximum of 50 characters!!')
#else:
#    print('Your name looks good👍') 
#if choice=='l':
 #   weight=weight*0.45
 #   print(f"You're {weight:.2f} KG")
#elif choice.lower()=='k':
#    weight=weight/0.45
#    print(f"You're {weight:.2f} LB")
#else:
#    print("Invalid choice!\n\n")


#print('Adult Classefier!!\n')
#age=int(input('Please enter your age: '))
#<13:child,13-17:Teen,18-64:adult,>64:seior
#if age<=0:
#    print('Invalid age!!')
#elif age<13:
#    print("You're: child.")
#elif 13<=age<=17:
#    print("You're: teen.")
#else:
#    print("You're: ","adult" if 18<=age<=64 else "senior")


#print(f'{"\nTemperature Category!!?\n":=>48}{'='*23}')
#degree= float(input("Enter temperature in Celsuis(°C): "))
#<0:freezing,0-10:cold,10-20:cool,20-30:warm,>30:hot
#if degree<=0:
#    print("Weather is: Freezing🥶")
#elif 0<degree<=10:
#    print("Weather is: Cold❄️")
#elif 10<degree<=20:
#    print("Weather is: Cool😎")
#else:
#    print("Weather is: ",'Warm☀️' if 20<degree<=30 else 'Hot🥵')


#print(f"{'\nLogin Attempts!!':=>33}\n{'='*16}")
#user_name=input('Enter user name: ')
#password=input('Enter your password: ')
#attempt=1
#print(f"{'\nWelcome':=>15}\n{'='*7}")
#while (attempt<=3): 
#    print(f'\nAttempt: {attempt}')
#    user_again=input('Enter user name: ')
#    pass_again=input('Enter your password: ')
#    if (user_again == user_name) and (pass_again == password):
#        print(f'{"\nAccount opened!!":=>33}')
#        break
#    attempt+=1
#else:
#    print(f'{"\nAccount locked!!":=>33}')


#print(f'{"\nGuessing Game!!":=>31}\n{"="*15}')
#guess_count=1
#secret_num=13
#while guess_cout<=3:
#    guess_n=int(input('Guess: '))
#    if guess_n==secret_num:
#        print('You won!!') 
#        break
#    guess_cout+=1
#else:
#    print('Game Over!!')

#print(f'{"\nCar Game!!":=>21}\n{"="*10}')
#stop_check=False
#while True:
#    command=input('> ').lower()
#    if command=="help":
#        print('''"start" -to start the car. 
#"stop" -to stop the car.
#"quit" -to exit.''')
#    elif command=="start":
#        if not stop_check:
#            print('The car started...Ready to go!! ')
#            stop_check=True
#        else:
#            print('Hey,the car already started,what do you do?')
#    elif command=="stop":
#        if  stop_check:
#            print('The car stopped!!')
#            stop_check=False
#        else:
#            print('Hey,the car already stopped,what do you do?')
#    elif command=="quit":
#        break
#    else:
#        print("I don't understand that...")

#list=[1,2,3,4,5,6,7,8]
#for cursor in list:
#    printer=''
#    for count in range(cursor):
#        printer+='x '
#    print(printer)   

#print('Find Maximum!!')
#list_num=[3,10.2,997.5,45]
#max=list_num[0]
#for test in list_num:
#        if test>max:
#            max=test
#print(f'max:{max}')

#print('Remove duplications!!')
#list=[1,2,4,4]
#x, y, z, printk=list   
#print(x,'',y,'',z,'',k,'\n',list.count(k),' ',list.index(y))
import math
#Xn+1=[2Xn+(A/Xn**2)]/3
    
#while True:
#    A=float(input('Enter the number: '))
#    if A>=0: 
#        X1=A/3   
#        while True:
#            X2=(2*X1+(A/X1**2))/3
#            if abs(X2-X1)<10**-6:
#                print(f'the cube root of {A} is:{round(X1,5)}')
#                break
#            else:
#                X1=X2
#    break
#print("Exercise 05.")
#list=[]
#while True: 
#    N=int(input('choose the list size with up to 100 integers or : '))
#    if 0<N<=100:
#        for i in range(N):
#            num=int(input(f'Ener the number {i+1}: ')) 
#            list.append(num)
#    break
#print(list)
#list.sort()
#print(list)
#list.reverse()
#print(list)

#print("Exercise 18.")

#A=[]
#vowel=['a','e','i','o','u','A','E','I','O','U']
#while True:
#    M=int(input('Enter the number of columns: '))
#    N=int(input('Enter the number of rows: '))
#    if 0<N<20 and 0<M<30:
#        for row in range(N):
#            a=[]
#            print('fill in the row',row+1)
#            for column in range(M):
#                ind_A=input()
#                a.append(ind_A)
#            A.append(a)
#    break
#print(A)

#print(f'\n{"\nSearch for your character!!":=>55}\n{"="*27}\n')
#ch_look=input("Enter the character you're looking for: ")
#found=False
#for row in A:
#    for column in row:
#        if column==ch_look:
#            print('the character is found!!\n')
#            found=True
#            break
#if not found:
#    print("the character doesn't exist!!\n")
    
#print(f'{"\nCounting vowels!!":=>35}\n{"="*17}\n')
#count=0
#for row in A:
#    for column in row:
#        for ch in column:
#            if ch in vowel:
#                count+=1
#print(f'the number of vowels in this matrix is{count:>3}')
