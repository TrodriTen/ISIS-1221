def conteo_materias(materia1, materia2, materia3):
    conteo = 0
    if 'programacion' in materia1 or 'matematica' in materia1 or 'filosofia' in materia1 or 'literatura' in materia1:
        conteo += 1
    if 'programacion' in materia2 or 'matematica' in materia2 or 'filosofia' in materia2 or 'literatura' in materia2:
        conteo += 1
    if 'programacion' in materia3 or 'matematica' in materia3 or 'filosofia' in materia3 or 'literatura' in materia3:
        conteo += 1 
    return conteo

