'''
Author: Joel Rubio
Date: 5-july-2022
'''

'''
Clase que representa el objeto a ser
mandado como payload de una solicitud HTTP.
'''
class EmployeeRequest(object):
    def __init__(self, firstname, surname, country, language, airport):
        self.__firstname = firstname
        self.__surname   = surname
        self.__country   = country
        self.__language  = language
        self.__airport  = airport

    def serialize(self):
        return {
            'firstname': self.__firstname,
            'surname': self.__surname,
            'country': self.__country,
            'language': self.__language,
            'airport': self.__airport
        }


'''
Clase que obtiene los empleados de
un archivo de texto.
'''
class EmployeeFile:
    
    __filepath = "Empleados.txt"
    __encoding = "utf-8"

    def getEmployees(self):
        employees = []
        
        try:
            with open(EmployeeFile.__filepath, "rt", encoding = EmployeeFile.__encoding) as write_obj:

                for line in write_obj.readlines():
                    result = line.split(",")

                    employees.append(EmployeeRequest(result[0].strip(), 
                                                     result[1].strip(),
                                                     result[2].strip(),
                                                     result[3].strip(),
                                                     result[4].strip()))
        except IOError as error:
            print(error)

        return employees