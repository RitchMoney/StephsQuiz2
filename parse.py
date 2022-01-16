import json, os

#pulling the json data into python
f = open('fixed_big_boss_list')
data = json.load(f)

#these dicts will be used to sort out the dicts by country and asn
country_dct = {
    "null": []
}
asn_dct = {
    "null": []
}

#this actually does the sorting
for d in data:
    if "country" in d:
        if d["country"] in country_dct:
            country_dct[d["country"]].append(d)
        else:
            country_dct[d["country"]] = [d]
    else:
        country_dct["null"].append(d)

for d in data:
    if "asn" in d:
        if d["asn"] in asn_dct:
            asn_dct[d["asn"]].append(d)
        else:
            asn_dct[d["asn"]] = [d]
    else:
        asn_dct["null"].append(d)

if not os.path.exists('sortAsn'):
    os.makedirs('sortAsn')

if not os.path.exists('sortCountry'):
    os.makedirs('sortCountry')

#convert to json and write to file
for i in country_dct:
    json.dumps(i)
    with open("sortCountry/"+i+".json", "a+") as f:
        f.write(i)

for i in asn_dct:
    json.dumps(i)
    with open("sortAsn/"+i+".json", "a+") as f:
        f.write(i)
