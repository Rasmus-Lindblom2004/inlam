import math;

punkt_ett = list(map(float, input("Skriv första kordinaterna delade med ',' t.ex '3,4': ").split(",")))
punkt_tva = list(map(float, input("Skriv andra kordinaterna delade med ',' t.ex '3,4': ").split(",")))

distans = math.sqrt(pow(punkt_ett[0]-punkt_tva[0],2)+pow(punkt_ett[1]-punkt_tva[1],2))

print(f"Distansen mellan punkterna är {distans}")