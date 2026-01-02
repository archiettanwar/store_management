import pandas

df = pandas.read_csv("articles.csv",dtype = {"stock":str})

class Store:
    def __init__(self,id,needed):
        self.id = id
        self.needed=needed
    def available(self):
        '''Checks if there is the given item in the store or not!'''
        availability=df.loc[df["id"]==self.id,"stock"].squeeze()
        if availability=="yes":
            return True
        else:
            return False
    def purchase_item(self):
        '''Purachese the item and then  changes its stock by one or the amount they want!'''
        df.loc[df["id"]==self.id,"stock"]=f"{int(int(self.id)-int(self.needed))}"
        df.to_csv("articles.csv",index=False)

class Receipt:
    def __init__(self,receipt_no,price,name):
        self.receipt_no=receipt_no
        self.price=price
        self.name = name
    def generate(self):
        pass

print(df)
user_need=input("Enter the id the object you want:")
stock_need=input("Enter the amount you want:")
store=Store(user_need,stock_need)

if store.available():
    store.purcahse_item()
    name=input("enter your name:")
    receipt=Receipt()
    print(receipt.generate())
else:
    print("The item is sold out.")