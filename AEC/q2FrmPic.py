cricketer_profile={
    "name":None,
    "age":None,
    "favorite_players":None,
    "countries_played":None
}
nVal=str(input("Enter the name: "))
aVal=int(input("Enter the age: "))
plVal=list(input("Enter the favorite playeers: ").split())
cnVal=list(input("Enter the countries played: ").split())

cricketer_profile['name']=nVal
cricketer_profile['age']=aVal
cricketer_profile['favorite_players']=plVal
cricketer_profile['countries_played']=cnVal

print(cricketer_profile)