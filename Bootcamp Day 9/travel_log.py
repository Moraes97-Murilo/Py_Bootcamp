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
    if len(log) != 0:
        store = [log[x].values() for x in range(len(log))]
        resto = [log[x].keys() for x in range(len(log))]
        store = store[0]
        print(store)
    if len(log) == 0 or country not in list(store):
        n += 1
        duration = float(input("How much weeks did you stay there? "))
        n_city = int(input(f"How many cities did you visit in {country}? "))
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
        ind = (list(resto))[0]
        print(f"Seems that is not the first time you visit {country}..")
        duration = float(input("How much weeks did you stay this time? "))
        n_city = int(input(f"How many NEW cities did you visit in {country}? "))
        city = cities_list(n_city)
        revisit(ind,duration,city)
        print(log)
        end = input(f"\n\nDo you have another trip to store? (yes/no).. ").lower()
        if end != "yes":
            verif = False
        else:
            continue
