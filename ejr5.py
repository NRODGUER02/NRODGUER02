t = 30.0
sexo = 'M'
edad = 25

altura_previa = 69.089 + 2.232 * t if sexo == 'V' else 61.412 + 2.317 * t

altura = altura_previa - ((edad - 29) * 0.06) if edad >= 30 else altura_previa
