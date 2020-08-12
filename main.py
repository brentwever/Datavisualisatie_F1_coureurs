import csv
from pad_naar_bestand import abs_to_rel_path
from country_codes import landnaam_omzetten_in_code
from pygal.maps.world import World
from pygal.bar import Bar

filename = abs_to_rel_path('drivers.csv')
with open(filename) as data:
    reader= csv.reader(data)
    header_row = next(reader)
 
    nationaliteiten = []
    for row in reader:
        nationaliteiten.append(row[7])
        
# het verkrijgen van unieke landen dus geen dubbele landen
geen_dubbele_nationaliteiten = set(nationaliteiten)

# het weergeven van aantal coureurs per land en plaatsen in een woordenboek
per_land_aantal_coureurs = {}
for land in geen_dubbele_nationaliteiten:
    aantal_per_land = nationaliteiten.count(land)
    per_land_aantal_coureurs[land]=aantal_per_land
#print(per_land_aantal_coureurs)

# nu de landnamen omzetten in landcodes met diens aantallen in woordenboek plaatsen
landcodes_en_diens_aantal = {}
for landnaam, aantal in per_land_aantal_coureurs.items():
    code = landnaam_omzetten_in_code(landnaam)
    landcodes_en_diens_aantal[code] = aantal
print(landcodes_en_diens_aantal)

pop0, pop1, pop2, pop3 = {},{},{},{}
for land, aantal in landcodes_en_diens_aantal.items():
    if aantal < 10:
        pop0[land]= aantal
    if aantal < 50:
        pop1[land]= aantal
    elif aantal < 100:
        pop2[land]= aantal  
    else:
        pop3[land]= aantal

# het plotprogramma
wm = World()
wm.title = 'Aantal coureurs die in F1 hebben geraced per land in de geschiedenis'
wm.add(' < 10', pop0)
wm.add(' < 50', pop1)
wm.add(' < 100', pop2)
wm.add(' > 100', pop3)

bestandsnaam = abs_to_rel_path('drivers_op_wereldkaart.svg')
wm.render_to_file(bestandsnaam) # nu kun je klikken op die bestandsnaam en de wereldmap bekijken in je browser

