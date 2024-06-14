import tkinter as tk 
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import random 
from datetime import date
from datetime import datetime


prices = {
    "Shawarma Wrap" : 25,
    "Shawarma Menu" : 35,
    "Shawarma Arabi" : 40,
    "Chicken Grill" : 50,
    "Pepsi" : 10,
    "7UP" : 10
}

root = Tk()

root.title("El-Naser Restaurant")


#-------------------- Functions --------------------#

def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "BIN_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id

def add():

    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + ".." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")


def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:

        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")



def displayShawarmaWrap(): 
    ShawarmaWrapDishFrame.configure(
        relief= "sunken",
        style="SelectedDish.TFrame"
    )
 
    displayLabel.configure(
        image = ShawarmaWrapImage,
        text = "Shawarma Wrap",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )


def displayShawarmaMenu():
    ShawarmaMenuDishFrame.configure(
        relief= "sunken",
        style="SelectedDish.TFrame"
    )
 
    displayLabel.configure(
        text = "Shawarma Menu",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = ShawarmaMenuImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayShawarmaArabi(): 
    ShawarmaArabiDishFrame.configure(
        relief= "sunken",
        style="SelectedDish.TFrame"
    )
   

    displayLabel.configure(
        text="Shawarma Arabi",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = ShawarmaArabiImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )


def displayChickenGrill():
    ChickenGrillDishFrame.configure(
        relief= "sunken",
        style="SelectedDish.TFrame"
    )
   
  
    
    displayLabel.configure(
        text="Chicken Grill",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = ChickenGrillImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayPepsi(): 
    PepsiDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
   

    displayLabel.configure(
        text="Pepsi",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = PepsiImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def display7up():
    SevenUpDishFrame.configure(
        relief="sunken",
        style="SelectedDish.TFrame"
    )
   


    displayLabel.configure(
        text="7UP",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = SevenUpImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )


def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("The Binary")
        file.write("\n")
        file.write("________________________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ODER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")



s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#1A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('DishFrame.TFrame', background = "#4A4A48", relief = "raised")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (6, 6, 6, 6),
            width = 30
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )



# Top Banner images


# Menu images
displayDefaultImageObject = Image.open("Images/display - Default.png").resize((450,580))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

ShawarmaWrapImageObject = Image.open("Images/menu/ShawarmaWrap.jpg").resize((450,550))
ShawarmaWrapImage = ImageTk.PhotoImage(ShawarmaWrapImageObject)

ShawarmaMenuImageObject = Image.open("Images/menu/ShawarmaMenu.jpg").resize((450,550))
ShawarmaMenuImage = ImageTk.PhotoImage(ShawarmaMenuImageObject)

ShawarmaArabiImageObject = Image.open("Images/menu/ShawarmaArabi.jpg").resize((450,550))
ShawarmaArabiImage = ImageTk.PhotoImage(ShawarmaArabiImageObject)

ChickenGrillImageObject = Image.open("Images/menu/ChickenGrill.jpg").resize((450,550))
ChickenGrillImage = ImageTk.PhotoImage(ChickenGrillImageObject)

PepsiImageObject = Image.open("Images/menu/pepsi.jpg").resize((450,550))
PepsiImage = ImageTk.PhotoImage(PepsiImageObject)

SevenUpImageObject = Image.open("Images/menu/7up.png").resize((450,550))
SevenUpImage = ImageTk.PhotoImage(SevenUpImageObject)




# Section Frames
mainFrame = ttk.Frame(root, width = 1200, height = 750, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 7, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 8, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 10, pady = 3, sticky = "NSEW")

# Dish Frames
ShawarmaWrapDishFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
ShawarmaWrapDishFrame.grid(row = 1, column = 0, sticky = "NSEW")

ShawarmaMenuDishFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
ShawarmaMenuDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

ShawarmaArabiDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
ShawarmaArabiDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

ChickenGrillDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
ChickenGrillDishFrame.grid(row = 4, column = 0, sticky ="NSEW")

PepsiDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
PepsiDishFrame.grid(row = 5, column = 0, sticky ="NSEW")

SevenUpDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
SevenUpDishFrame.grid(row = 6, column = 0, sticky ="NSEW")



#Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

ShawarmaWrapDishLabel = ttk.Label(ShawarmaWrapDishFrame, text ="Shawarma Wrap ... 25RON", style ="MenuLabel.TLabel")
ShawarmaWrapDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

ShawarmaMenuDishLabel = ttk.Label(ShawarmaMenuDishFrame, text ="Shawarma Menu ... 35RON", style ="MenuLabel.TLabel")
ShawarmaMenuDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

ShawarmaArabiDishLabel = ttk.Label(ShawarmaArabiDishFrame, text ="Shawarma Arabi ... 40RON", style ="MenuLabel.TLabel")
ShawarmaArabiDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

ChickenGrillDishLabel = ttk.Label(ChickenGrillDishFrame, text ="Chicken Grill ... 50RON", style ="MenuLabel.TLabel")
ChickenGrillDishLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

PepsiDishLabel = ttk.Label(PepsiDishFrame, text ="Pepsi ... 10RON", style ="MenuLabel.TLabel")
PepsiDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SevenUpDishLabel = ttk.Label(SevenUpDishFrame, text ="7UP .... 10RON", style ="MenuLabel.TLabel")
SevenUpDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
ShawarmaWrapDisplayButton = ttk.Button(ShawarmaWrapDishFrame, text ="Display", command = displayShawarmaWrap )
ShawarmaWrapDisplayButton.grid(row = 0, column = 1, padx = 10)

ShawarmaMenuDisplayButton = ttk.Button(ShawarmaMenuDishFrame, text ="Display", command= displayShawarmaMenu )
ShawarmaMenuDisplayButton.grid(row = 0, column = 1, padx = 10)

ShawarmaArabiDisplayButton = ttk.Button(ShawarmaArabiDishFrame, text ="Display", command= displayShawarmaArabi )
ShawarmaArabiDisplayButton.grid(row = 0, column = 1, padx = 10)

ChickenGrillDisplayButton = ttk.Button(ChickenGrillDishFrame, text ="Display", command= displayChickenGrill)
ChickenGrillDisplayButton.grid(row = 0, column = 1, padx = 10)

PepsiDisplayButton = ttk.Button(PepsiDishFrame, text ="Display", command= displayPepsi)
PepsiDisplayButton.grid(row = 0, column = 1, padx = 10)

SevenUpDisplayButton = ttk.Button(SevenUpDishFrame, text ="Display", command= display7up)
SevenUpDisplayButton.grid(row = 0, column = 1, padx = 10)



#Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command= order)
orderButton.grid(row = 4, column = 0, sticky = "EW")



#Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 5)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command= add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command= remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

addItemButton = ttk.Button(displayFrame, text="ADD ITEM")
addItemButton.grid(row = 1, column= 3, padx=2 , sticky = "NSEW")

removeItemButton = ttk.Button(displayFrame, text="REMOVE ITEM")
removeItemButton.grid(row = 1, column = 4, padx = 2, sticky = "NSEW" )



#---------- GRID CONFIGURATIONS ----------#


mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)






root.mainloop()