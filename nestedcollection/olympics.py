
olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

#country mist most number of gold medals

def get_medals(oly):

    return oly.get("gold")

most_gold_medals=max(olympic_medal_count,key=get_medals)

#print(most_gold_medals)

for country in olympic_medal_count:

    total_medal=country["total"]=country["gold"]+country["silver"]+country["bronze"]

    #print(country)

least_medal_country=min(olympic_medal_count,key=lambda oly:oly["total"])

#print(least_medal_country)

sorted_countries=sorted(olympic_medal_count,key=lambda oly:oly["total"],reverse=True)

print(sorted_countries)












