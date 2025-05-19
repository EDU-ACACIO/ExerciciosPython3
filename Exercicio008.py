distancia = float(input('\033[7;30;46mDigite a distância em metros: '))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print (f'A medida de {distancia} corresponde a')
print (f'{km:.3f} km')
print (f'{hm:.2f} hm')
print (f'{dam:.1f} dam')
print (f'{dm:.0f} dm')
print (f'{cm:.0f} cm')
print (f'{mm:.0f} mm')
