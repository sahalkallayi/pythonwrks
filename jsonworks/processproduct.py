
from json import load

f=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\jsonworks\\products.json",encoding="UTF-8")

items=load(f)

#print(len(items))

#for i in items:

    #print(i.get("title"))

title_name=[i.get("title")for i in items]

#print(title_name)

jwellery_products=[i.get("title")for i in items if i.get("category")=="jewelery"]

#print(jwellery_products)

product_price=[i.get("title")for i in items if i.get("price")>100]

#print(product_price)

product_range=[i.get("title")for i in items if i.get("price")>=100 and i.get("price")<=150]

#print(product_range)

def get_rating_count(dic):

    return dic.get("rating").get("count")

top_selling_product=max(items,key=get_rating_count)

print(top_selling_product)

















