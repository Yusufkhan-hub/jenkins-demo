primary_list=['Honey','David','Mike','Xavier','Wood','Kofi','Cena','Ortan','Triple H','Undertaker','Kane']
print("This application is used for check the index number of the elements in the list using Python.")
count=0
try:
    print("The given list is",primary_list)
    for i in primary_list:
        count+=1
        print("The index number of",i,"is",count)    
except Exception as e:
    print(e)
