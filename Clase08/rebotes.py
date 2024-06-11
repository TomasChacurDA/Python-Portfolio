import sys

def rebotar(altura, rebotes_a_registrar):
    factor_perdida_altura=3/5
    cantidad_rebotes=0

    for cantidad_rebotes in range (rebotes_a_registrar):
        cantidad_rebotes+=1
        altura=altura*factor_perdida_altura
        print(f"{cantidad_rebotes:^4}: {round(altura, 2):>8.2f}")

if __name__=='__main__':
    if len(sys.argv)!=3:
        print(f'Uso adecuado: {sys.argv[0]} altura_inicial rebotes_a_registrar')
        sys.exit(1)
    else:
        altura=float(sys.argv[1])
        rebotes_a_registrar=int(sys.argv[2])
        rebotar(altura,rebotes_a_registrar)

