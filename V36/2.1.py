Materstall_Idag=float(input("Mätarställning i dag? "))
Materstall_År=float(input("Mäterställning för ett år sedan? "))
Bensin_Förbrukad=float(input("Hur många liter har du förbrukat i år? "))

Km_Körda=Materstall_Idag-Materstall_År
Bensin_per_KM=Bensin_Förbrukad/Km_Körda

print(f"Antal körda km: {Km_Körda}")
print(f"Förbrukning per km: {round(Bensin_per_KM,2)}")