def Binary_Search(list, lowbound, upbound, value):
    
    if lowbound>upbound:
        return "doens't exist" 
    else:
        middle=(lowbound+upbound)//2
        if value==list[middle]:
            return "exist"
        elif value<list[middle]:
            return Binary_Search(list, lowbound, middle-1, value)
        else:
            return Binary_Search(list, middle+1, upbound, value)

list=[1,2,3,4,5,6,8,9,45,50]
value=5.5

print(Binary_Search(list, 0, len(list),value))
        