"""
print("Dhananjay Kumar")
print("dhananjaykr306@gmail.com")
print("1BI20AI010")
"""
class shopKeeper:
    def _init_(self,name,uprice,gst,quantity):
        self.n = name
        self.p = uprice
        self.g = gst
        self.q = quantity
        self.gst = 0
        self.price = 0
        self.gprice = 0
        self.finalprice = 0
        
    def calc_dis_price(self):
        if self.p > 500:
            self.price = self.p + self.p * 1/20
        else:
            self.price = self.p    
    
    def calc_gst_price(self):
        self.gprice =self.price + self.price*(self.g/100)
    
    def quan_price(self):
        if self.gprice == 0:
            self.finalprice = self.q * self.price
        else:
            self.finalprice = self.q * self.gprice    
        
    def calc_gst(self):
        self.gst = self.price*(self.g/100)        
        

        

Product1 = shopKeeper("Leather wallet",1100,18,1)
Product2 = shopKeeper("Umbrella",900,12,4)
Product3 = shopKeeper("Cigarette",200,28,3)
Product4 = shopKeeper("Honey",100,0,2)

prod = [Product1,Product2,Product3,Product4]

for Product in prod:
    Product.calc_dis_price()
    Product.calc_gst_price()
    Product.quan_price()
    Product.calc_gst()

    
print("Product Gsts are : ")

max_gst = 0
pro = ""
j=1
for Product in prod:
    if Product.gst>max_gst:
        obj = Product.n
        max_gst = Product.gst
        j+=1
        
print("The Product for which we pay max GST amount is", pro)
total_amount = 0     
for Product in prod:
    total_amount = total_amount + Product.finalprice
                
print("The total amount to be paid to the shopkeeper is : ",total_amount)
