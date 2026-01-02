import pandas
from fpdf import FPDF


df = pandas.read_csv("articles.csv",dtype = str)

class Store:
    def __init__(self,id,needed):
        self.id = id
        self.needed=needed
    def available(self):
        '''Checks if there is the given item in the store or not!'''
        availability=df.loc[df["id"]==self.id,"stock"].squeeze()
        if int(availability)>=int(self.needed):
            return True
        else:
            return False
    def purchase_item(self):
        '''Purachese the item and then  changes its stock by one or the amount they want!'''
        df.loc[df["id"]==self.id,"stock"]=f"{int(int(df.loc[df["id"]==self.id,"stock"].squeeze())-int(self.needed))}"
        df.to_csv("articles.csv",index=False)

class Receipt:
    def __init__(self,receipt_no,price,name):
        self.receipt_no=receipt_no
        self.price=price
        self.name = name
    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"RECEIPT NUMBER :{self.receipt_no}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"PRICE :${self.price}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"NAME :{self.name}", ln=1)

        pdf.output("receipt.pdf")

print(df)
user_need=input("Enter the id the object you want:")
stock_need=input("Enter the amount you want:")
store=Store(user_need,stock_need)

receipt_number=100

if store.available():
    store.purchase_item()
    name=input("enter your name:")
    receipt_number=receipt_number+1
    receipt=Receipt(receipt_no=receipt_number,price=df.loc[df["id"]==user_need,"price"].squeeze(),name=name)
    receipt.generate()
    print("your receipt has been generated")
else:
    print("The item is sold out.")