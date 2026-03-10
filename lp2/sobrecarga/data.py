from datetime import date

class Data:
    def __init__(self, data):
        if isinstance(data, str):
            self._data = date.fromisoformat(data)
        elif isinstance(data, date):
            self._data = data
    def __str__(self):
        return f'{self._data.day}/{self._data.month}/{self._data.year}'

dia_prova = Data('2026-03-24')

print(dia_prova)

dia_hoje = Data(date.today())
print(dia_hoje)

