def userInput():
    userInputList=[]
# Recipe Name
    recipeName = input("Enter Recipe name :")

    if len(recipeName.strip())> 0 :
        recipeName = recipeName.strip()
    else:
        recipeName = 'Recipe_1'
        
    # print('recipeName :',recipeName)
    userInputList.insert(0,recipeName)

    # <-------------------------------------------------------------------------------------------------------------------------------->
#Operator Name

    operatorName = input("Enter Operator name :")

    if len(operatorName.strip())> 0 :
        operatorName = operatorName.strip()
    else:       
        operatorName = 'Operator_1'
        
    # print('operatorName :',operatorName)
    userInputList.insert(1,operatorName)

    # <---------------------------------------------------------------------------------------------------------------------------------->
 #isBatch   
    
    isBatch = str(input("Is it a batch? yes or no: "))
    isBatch.lower()
    if isBatch == "yes":
        userInputList.insert(2,isBatch.lower())
    else:
        userInputList.insert(2,isBatch.lower())
    
    #<------------------------------------------------->
# Target


    target = int(input("What is the target(range 0 to 5000):"))
    if(0<= target <= 5000):
        userInputList.insert(3,target)
    else:
        print("is not in range,but you can continue")
        userInputList.insert(3,target)
    
    #<------------------------------------------------------->
 # Cycle Design Time   


    cycleDesignTime = int(input("What is cycle design time(range 0 to 60 seconds:"))
    if(0<= cycleDesignTime <=60):
        userInputList.insert(4,cycleDesignTime)
    else:
        print("is not in range,but you can continue")
        userInputList.insert(4,cycleDesignTime)
    #<--------------------------------------------------->
# Vendor Name

    flagVendorName = 0   # 0 : not valid vender , 1 : valid vander
    vendorName = input("Enter vendor name:")

    vendorNameList = ['Almaco', 'Nexxus', 'Automata']
    for i in range(3):          # maximum 3 tries user are allowed to logged-in
        if vendorName in vendorNameList :
            flagVendorName = 1
            break
        elif i==2:
            break
        else:
            vendorName = input("Enter vendor name:")

    if flagVendorName==0 :
        print('User reached to max retires')
    else:
        userInputList.insert(5,vendorName)
    
#Displaying the Data

    if(flagVendorName==1):
        print("Recipe Name  Operator Name  Batch  Target  Cycle Design Time  Vendor Name")
        print(userInputList)
       
    
    

userInput()