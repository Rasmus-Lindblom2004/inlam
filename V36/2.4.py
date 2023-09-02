mil_per_gal = list(map(float, input("Skriv miles per gallon sperareret med ett snedstreck t.ex '10/1': ").split("/")))

liter_per_km = [mil_per_gal[1]*3.785, mil_per_gal[0]*1.609]

print(f"{liter_per_km[0]} liter per {liter_per_km[1]} km")