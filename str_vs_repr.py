from datetime import datetime
data = datetime.now()

print('str ->', str(data))

print('repr ->', repr(data))

#-------------------------------

class vinho_string:


    def __init__(self):
        self._name = 'finca premiada'
        self._ano = 2021
        self._data_atual = datetime.now()


    def __str__(self):
        return '%s' % self._data_atual


class vinho_repr:


    def __init__(self):
        self._name = 'finca premiada'
        self._ano = 2021
        self._data_atual = datetime.now()


    def __repr__(self):
        return repr(self._data_atual)



if __name__ != '__main__':
    pass
else:
    obj1 = vinho_string()
    print('classe string', obj1)
    obj2 = vinho_repr()
    print('classe repr', obj2)