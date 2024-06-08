
def propagar(fosforos):
    resultado = []
    for f in fosforos:
        resultado.append(f)
    for i, f in enumerate(fosforos):
        if f == 1:
            p = i - 1
            while p >= 0 and fosforos[p] != -1:
                resultado[p] = 1
                p -= 1    
            p = i + 1
            while p < len(fosforos) and fosforos[p] != -1:
                resultado[p] = 1
                p += 1
    return resultado
        
propagar([0, 1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 1, 0])


