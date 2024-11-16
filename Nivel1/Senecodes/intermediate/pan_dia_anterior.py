def calcular_total_pan_comprado(frescos, viejos):
    valor_frescos = frescos*450
    valor_viejos = viejos*(450*0.6)
    return valor_frescos + valor_viejos
print(calcular_total_pan_comprado(10,1))