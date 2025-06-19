def cantidad_palabras_leidas_por_minuto():
    # El usurio ingresa un número.
    while True:
        try:
            numero = int(input("Ingresa el número de palabras leídas por minuto: "))
            if numero <= 0:
                print("Por favor, ingresa un número positivo.")
            else:
                return numero
        except ValueError:
            print("Por favor, ingresa un valor numérico válido.")


def clasificar_lectura_1ro(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 1ro básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 56:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 47 <= numero <= 55:
        print(f"El número {numero} está entre 47 y 55. La lectura es Rápida.")
    elif 38 <= numero <= 46:
        print(f"El número {numero} está entre 38 y 46. La lectura es Media Alta.")
    elif 29 <= numero <= 37:
        print(f"El número {numero} está entre 29 y 37. La lectura es Media Baja.")
    elif 22 <= numero <= 28:
        print(f"El número {numero} está entre 22 y 28. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")



def clasificar_lectura_2do(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 2do básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 84:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 74 <= numero <= 83:
        print(f"El número {numero} está entre 74 y 83. La lectura es Rápida.")
    elif 64 <= numero <= 73:
        print(f"El número {numero} está entre 64 y 73. La lectura es Media Alta.")
    elif 54 <= numero <= 63:
        print(f"El número {numero} está entre 54 y 63. La lectura es Media Baja.")
    elif 43 <= numero <= 53:
        print(f"El número {numero} está entre 43 y 53. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")



def clasificar_lectura_3ro(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 3ro básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 112:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 100 <= numero <= 111:
        print(f"El número {numero} está entre 100 y 111. La lectura es Rápida.")
    elif 88 <= numero <= 99:
        print(f"El número {numero} está entre 88 y 99. La lectura es Media Alta.")
    elif 76 <= numero <= 87:
        print(f"El número {numero} está entre 76 y 87. La lectura es Media Baja.")
    elif 64 <= numero <= 75:
        print(f"El número {numero} está entre 64 y 75. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")


def clasificar_lectura_4to(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 4to básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 140:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 125 <= numero <= 139:
        print(f"El número {numero} está entre 125 y 139. La lectura es Rápida.")
    elif 111 <= numero <= 124:
        print(f"El número {numero} está entre 111 y 124. La lectura es Media Alta.")
    elif 97 <= numero <= 110:
        print(f"El número {numero} está entre 97 y 110. La lectura es Media Baja.")
    elif 85 <= numero <= 96:
        print(f"El número {numero} está entre 85 y 96. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")


def clasificar_lectura_5to(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 5to básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 168:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 150 <= numero <= 167:
        print(f"El número {numero} está entre 150 y 167. La lectura es Rápida.")
    elif 136 <= numero <= 149:
        print(f"El número {numero} está entre 136 y 149. La lectura es Media Alta.")
    elif 120 <= numero <= 135:
        print(f"El número {numero} está entre 120 y 135. La lectura es Media Baja.")
    elif 104 <= numero <= 119:
        print(f"El número {numero} está entre 104 y 119. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")


def clasificar_lectura_6to(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 6to básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 196:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 178 <= numero <= 195:
        print(f"El número {numero} está entre 178 y 195. La lectura es Rápida.")
    elif 161 <= numero <= 177:
        print(f"El número {numero} está entre 161 y 177. La lectura es Media Alta.")
    elif 143 <= numero <= 160:
        print(f"El número {numero} está entre 143 y 160. La lectura es Media Baja.")
    elif 125 <= numero <= 142:
        print(f"El número {numero} está entre 125 y 142. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")


def clasificar_lectura_7mo(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 7mo básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 218:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 200 <= numero <= 217:
        print(f"El número {numero} está entre 200 y 217. La lectura es Rápida.")
    elif 182 <= numero <= 199:
        print(f"El número {numero} está entre 182 y 199. La lectura es Media Alta.")
    elif 164 <= numero <= 181:
        print(f"El número {numero} está entre 164 y 181. La lectura es Media Baja.")
    elif 146 <= numero <= 163:
        print(f"El número {numero} está entre 146 y 163. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")
    

def clasificar_lectura_8vo(numero):
    """
    Esta función determina las palabras leídas por minuto de un estudiante de 8vo básico
    """
    # Clasificación de acuerdo con el número de palabras leídas por minuto.
    if numero > 239:
        print(f"El número {numero} es una lectura Muy Rápida.")
    elif 221 <= numero <= 238:
        print(f"El número {numero} está entre 221 y 238. La lectura es Rápida.")
    elif 203 <= numero <= 220:
        print(f"El número {numero} está entre 203 y 220. La lectura es Media Alta.")
    elif 185 <= numero <= 202:
        print(f"El número {numero} está entre 185 y 202. La lectura es Media Baja.")
    elif 167 <= numero <= 184:
        print(f"El número {numero} está entre 167 y 184. La lectura es Lenta.")
    else:
        print(f"El número {numero} es una lectura Muy Lenta.")


    """
    Esta función asocia un numero al curso de 1ro a 8vo Básico.
    """
#Números y grados
def clasificar_lectura(numero, curso):
    if curso == 1:
        clasificar_lectura_1ro(numero)
    elif curso == 2:
        clasificar_lectura_2do(numero)
    elif curso == 3:
        clasificar_lectura_3ro(numero)
    elif curso == 4:
        clasificar_lectura_4to(numero)
    elif curso == 5:
        clasificar_lectura_5to(numero)
    elif curso == 6:
        clasificar_lectura_6to(numero)
    elif curso == 7:
        clasificar_lectura_7mo(numero)
    elif curso == 8:
        clasificar_lectura_8vo(numero)
    else:
        print("Curso no válido.")


    """
    Esta función clasificará el curso al que el o la estudiante pertenece.
    """
#Cursos
def seleccionar_curso():
    # Menú de selección de curso
    while True:
        try:
            print("Selecciona el curso:")
            print("1. 1ro Básico")
            print("2. 2do Básico")
            print("3. 3ro Básico")
            print("4. 4to Básico")
            print("5. 5to Básico")
            print("6. 6to Básico")
            print("7. 7mo Básico")
            print("8. 8vo Básico")
            curso = int(input("Ingresa el número correspondiente al curso: "))
            if 1 <= curso <= 8:
                return curso
            else:
                print("Por favor, ingresa un número válido entre 1 y 8.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


# Función principal
def main():
    curso = seleccionar_curso()
    numero = cantidad_palabras_leidas_por_minuto()
    clasificar_lectura(numero, curso)

# Ejecutamos el programa
if __name__ == "__main__":
    main()