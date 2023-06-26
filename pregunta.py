"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    
    with open("clusters_report.txt",'r') as file:
        raw_file = file.readlines()
    data = list()
    head = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    raw_file = raw_file[4:]
    
    for line in raw_file:
        words = line.split()
        if len(words) != 0:
            if words[0].isdigit():
                data.append(words[0:3])
                data[-1].append(' '.join(words[4:]))
                data[-1][-1] += ' '
            else:
                data[-1][-1] += ' '.join(words)
                data[-1][-1] += ' '
        
    for line in data:
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[2] = line[2].replace(',','.')
        line[2] = float(line[2])
        line[-1] = line[-1].rstrip('. ')
    
    df = pd.DataFrame(data,columns=head)

    return df


print(ingest_data())