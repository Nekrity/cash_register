#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#
import json
with open('purchase_list.json', 'r') as openfile:
    purchase_list= json.load(openfile)
discount=0
while True:
    
    print("\nWhat would you like to do?")
    print("1. Add a new product")
    print("2. Show your purchase list")
    print("3. Delete a certain product")
    print("4. Delete your purchase list")
    print("5. Add discount")
    print("6. Pay for products")
    print("7. Exit")
    choice=input("Enter your choice: ")
    if choice=="1": #adds product and it's price
        product={}
        product["name"]=input("Enter products name: ")
        if len(product["name"])<2 or len(product["name"])>120: #product name validation
            print("Error! product name must be from 2 to 120 symbols")
            pass
        else: #continue
            product["price"]=float(input("Enter products price (euros.cents): "))
            if product["price"]<0 or product["price"]>9999: #product price validation
                print("Error! Product price must be from 0 to 9999")
            else: #continue
                purchase_list.append(product)
    elif choice=="2": #shows your purchase list
        print("Showing your purchase list...")
        print(purchase_list)
    elif choice=="3": #deletes a certain product
        delete_product=int(input("Enter sequence number of product you want to delete: "))
        purchase_list.pop(delete_product-1)
    elif choice=="4": #clears purchase list
        confirmation=input("Are you sure you want to delete your purchase list? (yes/no) ")
        if confirmation=="yes": #extra verificatiion
            purchase_list.clear()
            print("Your list has been succesfully deleted")
    elif choice=="5": # adds a discount
        print("Discounts work until you exit the app (I'm too lazy to think how to save them)")
        discount=int(input("Enter discount (%, write only number): "))
    elif choice=="6": # paying for your products
        summ=0
        for product_payment in purchase_list: # to count the price
            summ+=product_payment["price"]
        if not discount==0: # if no discount
            print("discount",discount,"%")
            summ=summ-(summ*(discount*0.01))
        print(summ)
        print("\nYou must pay",summ)
        money=float(input("Enter sum of money you will give to us: "))
        print("Here's your change:",money-summ)
        print("Don't forget to take the check")
        for x in purchase_list: # printing purchases
            print(x)
        if not discount==0: # if no discount
            print("discount",discount,"%")
            
        print("===================================")
        print("The total amount without discount:",summ)
        if not discount==0:
            print("The total amount without discount:",summ-(summ*(discount*0.01)))
        else:
            print("The total amount without discount:",summ)
        print("Your change:",money-summ)
        purchase_list.clear()
        print("\nHave a great day (btw I deleted your purchase list because you have already paid for products)")
    elif choice=="7":
        print("Exiting...")
        with open("purchase_list.json", "w") as purchase_file:
            json.dump(purchase_list, purchase_file)
        break
    else:
        print("ERROR! You have entered incorrect number")
