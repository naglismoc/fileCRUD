import SQLCRUD as sql


results = sql.getData(  "SELECT * FROM actor limit 5" )
for row in results:
  print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}")  # Access column data by index



results = sql.getData(  "SELECT * FROM customer limit 5" )
for row in results:
  print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}")  # Access column data by index

#atvaizduoti visus customerius
# atvaizduoti visus customerius ir stulpelį kuriame būtų atvaizduota kiek pinigų kiekvienas jų yra išleidęs nuomai, ir kiek filmų nuomavesis
# atvaizduoti aktorius ir keliuose filmuose jie yra filmavesi
# atvaizduoti visus filmus ir kiek aktorių juose vaidino
# su pitono pagalba: nustatyti kuris nuomos punktas:
#--turi daugiau customerių
#--išnuomavo daugiau(ir kiek kiekvienas) filmų
#--kiek sugeneravo pajamų