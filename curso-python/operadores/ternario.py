#!pyhon3
lockdown = False
grana = 130

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuuuuu!'

print(f'O status é: {status}')