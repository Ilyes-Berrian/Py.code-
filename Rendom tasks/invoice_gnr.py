from openpyxl import load_workbook 

wb=load_workbook('Faz Food.xlsx')
sheet=wb['Invoice Generator']
sheet.append(['Product','Price/unit','Quantiy','Amount'])
 
print(f'{"\nget your invoice!!".title():=>37}\n{"="*18}\n')

num_prod=int(input('Enter the number of the products you bought: '))
print('\nNow Enter the product details:\n')
Total=0
cart=[]
for prod in range(num_prod):
    name=input(f'Product {prod+1}: ')
    price=float(input('Price: '))
    quantity=int(input('Quantity: '))
    amount=price*quantity
    Total+=amount
    cart.append((name,price,quantity,amount))
    print()


for row in range(2,num_prod+2):
    sheet.append(cart[row-2])
        
wb.save('Faz Food.xlsx')




























