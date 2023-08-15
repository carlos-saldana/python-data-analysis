# -*- coding: utf-8 -*-

#Importamos la librería a emplear
import csv

#Función principal
def read_csv(path):
    
  with open(path, 'r') as csvfile:
      
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    
    for row in reader:
        
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
      
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
