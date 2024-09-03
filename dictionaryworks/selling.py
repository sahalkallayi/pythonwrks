
mobiles={"brand":"samsung galaxy","model":"s22 ultra","price":130000,"is_available":True,"offer":2000}

if "offer" in mobiles:

    selling_price=mobiles.get("price")-mobiles.get("offer")

    print(selling_price)

else:

    selling_price=mobiles.get("price")

    print(selling_price)