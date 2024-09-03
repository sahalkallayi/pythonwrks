from json import load

f=open("C:\\Users\\User\\OneDrive\\Desktop\\PythonWorks\\jsonworks\\country.json",encoding="UTF-8")

country=load(f)

#1region

region_filter=[c.get("name") for c in country if c.get("region")=="Asia"]

#print(region_filter)

#2highest population

def highest_population(dic):

    return dic.get("population")

#population_filter=max(country,key=highest_population)

#print(population_filter.get("name"))

#3lowest area

def lowest_area(dic):

    return dic.get("area")

#area_filter=min(country,key=lowest_area)

#print(area_filter)

#4indipendent country

indipendent_country=[c.get("name")for c in country if c.get("independent")==True]

#print(len(indipendent_country))

#5capital of country

country_filter=[c.get("capital")for c in country]

#print(country_filter)

#6calling codes of country

calling_code_filter=[c.get("callingCodes") for c in country if c.get("region")=="Europe"]

#print(calling_code_filter)

#7country currencies

currencies_filter=[c.get("name")for c in country if c.get("currencies")=="United States dollar"]

#print(currencies_filter)

all_region={c.get("region") for c in country}

#print(all_region)

region_summary={}

for c in country:

    region_name=c.get("region")

    if region_name in region_summary:

        region_summary[region_name]+=c.get("area",0)

    else:

        region_summary[region_name]=c.get("area",0)

value_key=[(v,k)for k,v in region_summary.items()]

print(max(value_key))






#8country languages
#9english languages
#10most translation