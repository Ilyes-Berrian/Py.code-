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

print(f'\n{"\nThe invoice":=>23}\n{"="*11}\n')

print(f'{"Product":<25}{"Price/unit":<15}{"Quantiy":<15}{"Amount":<15}')
print("_"*70)
for i in cart:
    print(f'{i[0]:<25}{i[1]:<15,.2f}{i[2]:<15}{i[3]:<15,.2f}\n')

print("_"*70)

print(f'{"Total":<55}{Total:<,.2f}DZD')
print('\n\nPrint invoice ⬇️\n'.upper())
