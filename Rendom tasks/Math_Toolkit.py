import math 
print(f'{"\nMini Project!!":=>29}\n{"="*14}')

while True:
    print('''Menu:
1 → Absolute Difference
2 → Circle Calculator
3 → Power & Roots
4 → Floor & Ceil
5 → Min & Max Finder
6 → Exit''')
    choice=int(input('Enter you choice with the compatible number: '))
    print()
    if choice==1:
        print(f"{'\nAbsolute Difference':=>39}\n{'='*19}\n")
        set=input('Enter two numbers seperated by space: ')
        list=[float(num) for num in set.split()]
        print(abs(list[0]-list[1]))     
        print()
            
    elif choice==2:
        print(f"{'\nCircle Calculator':=>35}\n{'='*17}\n")
        radius=float(input('Enter the radius of a circle: '))
        area=math.pi*pow(radius,2)
        perimeter=2*math.pi*radius
        print(f'Area: {area:.3f} m²\nPerimeter: {perimeter:.3f} m\n')
   
    elif choice==3:
        print(f"{'\nPower & Roots':=>27}\n{'='*13}\n")
        num=float(input('Enter a real number: '))
        power=int(input('Enter the power you want: '))
        sequare_r=math.sqrt(num)
        cube_r=num**(1/3)
        print(f'Sequare root: {sequare_r:.4f}\nCube root: {cube_r:.4f}\nNumber to the power of {power}: {pow(num,power):,}\n')
        
    elif choice==4:
        print(f"{'\nFloor & Ceil':=>25}\n{'='*12}\n")
        num=float(input('Enter a real number: '))
        print(f'Floor: {math.floor(num)} \nCeiling: {math.ceil(num)}\n')
        
    elif choice==5:
        print(f"{'\nMin & Max Finder':=>33}\n{'='*16}\n")
        set=input('Enter 5 numbers seperated by space: ')
        list=[float(num) for num in set.split()]
        print(f'The maximum in the list: {max(list)} \nThe minimum in the list: {min(list)}\n')
        
    elif choice==6:
        print('program ended.\n')
        quit()
    else:
        print(f'{"Invalid choice!!\n"}{'-'*16}\n')
