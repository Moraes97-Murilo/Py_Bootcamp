#See your travel log
log = []
def cities_list(n_city):
    cont, city = 0, []
    while cont < n_city:
        ct = input("\nType the name of city that you visited: ").lower()
        if ct not in city:
            city.append(ct)
            cont += 1
        else:
            print(f"{ct} was already mentioned...")
    return city
def new_trip(n,country,time,city):
    n_country = {}
    n_country[n] = country
    n_country["week amount"] = time
    n_country["cities"] = city
    return n_country
def revisit(num,time,city):
    log[num]["week amount"] += time
    for j in city:
        log[num]["cities"].append(j)
#start
print("--- Welcome to Travel_Log ---")
verif, n = True, 0
while verif:
    country = input("\nWhat country did you travel last time? ").upper()
    store = []
    if len(log) != 0:
        for c in range(len(log)):
            resto = list([log[x].values() for x in range(len(log))][c])
            resto = resto[0]
            store.append(resto)
        
    if len(log) == 0 or country not in store:
        n += 1
        try:
            duration = float(input("How much weeks did you stay there? "))
        except:
            duration = float(input("You must type only numbers now...How much weeks did you stay there? "))
        try:    
            n_city = int(input(f"How many cities did you visit in {country}? "))
        except:
            n_city = int(input(f"You must type only numbers now...How many cities did you visit in {country}? "))
        city = cities_list(n_city)
        n_country = new_trip(n,country,duration,city)
        log.append(n_country)
        print(log)
        end = input(f"\n\nDo you have another trip to store? (yes/no).. ").lower()
        if end != "yes":
            verif = False
        else:
            continue
    else:
        ind = store.index(country)
        print(f"Seems that is not the first time you visit {country}..")
        try:
            duration = float(input("How much weeks did you stay this time? "))
        except:
            duration = float(input("Please type numbers...How much weeks did you stay this time? "))
        try:    
            n_city = int(input(f"How many NEW cities did you visit in {country}? "))
        except:
            n_city = int(input(f"Please type numbers...How many NEW cities did you visit in {country}? "))    
        city = cities_list(n_city)
        revisit(ind,duration,city)
        print(log)
        end = input(f"\n\nDo you have another trip to store? (yes/no).. ").lower()
        if end != "yes":
            verif = False
        else:
            continue
