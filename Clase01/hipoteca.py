'''David solicitó un crédito a 30 años para comprar una vivienda, 
con una tasa fija nominal anual del 5%. Pidió $500000 al banco y 
acordó un pago mensual fijo de $2684,11.'''
#-----------------------------------------------------------------


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))


#-----------------------------------------------------------------
''''Supongamos que David adelanta pagos extra de $1000/mes durante los primeros
12 meses de la hipoteca.
Modificá el programa para incorporar estos pagos extra y para que imprima el 
monto total pagado junto con la cantidad de meses requeridos.
Debería dar un pago total de 929965.62 en 342 meses.'''
#-----------------------------------------------------------------

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra = 1000
total_pagado = 0.0
mes = 0

while saldo > 0:
    if mes < 12:
        saldo = saldo * (1+tasa/12) - (pago_mensual + pago_extra)
        total_pagado += pago_mensual + pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado += pago_mensual
    mes += 1

print('Total pagado:', round(total_pagado, 2), 'en', mes, 'meses.')

#----------------------------------------------------------------
'''¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años,
comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
total_pagado = 0.0
mes = 0

while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1 + tasa / 12) - (pago_mensual + pago_extra)
        total_pagado += pago_mensual + pago_extra
    else:
        saldo = saldo * (1 + tasa / 12) - pago_mensual
        total_pagado += pago_mensual
    mes += 1

print('Total pagado:', round(total_pagado, 2), 'en', mes, 'meses.')
#-------------------------------------------------------------

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
total_pagado = 0.0
mes = 0

print("Mes\tTotal Pagado\tSaldo Restante")
while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1 + tasa / 12) - (pago_mensual + pago_extra)
        total_pagado += pago_mensual + pago_extra
    else:
        saldo = saldo * (1 + tasa / 12) - pago_mensual
        total_pagado += pago_mensual
    
    print(f"{mes+1}\t{round(total_pagado, 2)}\t{round(saldo, 2)}")
    
    mes += 1

print('\nTotal pagado:', round(total_pagado, 2))
print('Meses:', mes)
#-----------------------------------------------------------
'''Ya que estamos, corregí el código anterior de forma que 
el pago del último mes se ajuste a lo adeudado.'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
total_pagado = 0.0
mes = 0

print("Mes\tTotal Pagado\tSaldo Restante")
while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo_anterior = saldo
        saldo = saldo * (1 + tasa / 12) - (pago_mensual + pago_extra)
        total_pagado += pago_mensual + pago_extra
        if saldo > 0:
            total_pagado += saldo_anterior - saldo
            saldo = 0
    else:
        saldo_anterior = saldo
        saldo = saldo * (1 + tasa / 12) - pago_mensual
        total_pagado += pago_mensual
        if saldo > 0:
            total_pagado += saldo_anterior - saldo
            saldo = 0
    
    print(f"{mes+1}\t{round(total_pagado, 2)}\t{round(saldo, 2)}")
    
    mes += 1

print('\nTotal pagado:', round(total_pagado, 2))
print('Meses:', mes)
#--------------------------------------------------------------------
