'''
Author: Joel Rubio
Date: 5-july-2022
'''

'''
Clase que representa el objeto a ser
mandado como payload de una solicitud HTTP.
'''
class ClientRequest(object):
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
Clase que obtiene los clientes de
un archivo de texto.
'''
class ClientFile:
    
    __filepath = "Clientes.txt"
    __encoding = "utf-8"

    def getClients(self):
        clients = []
        
        try:
            with open(ClientFile.__filepath, "rt", encoding = ClientFile.__encoding) as write_obj:

                for line in write_obj.readlines():
                    result = line.split(",")

                    clients.append(ClientRequest(result[0].strip(), 
                                                 result[1].strip(),
                                                 result[2].strip(),
                                                 result[3].strip(),
                                                 result[4].strip()))
        except IOError as error:
            print(error)

        return clients