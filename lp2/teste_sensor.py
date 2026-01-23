from sensor import Sensor

#Criar um objeto do tipo sensor

s1 = Sensor(1)

s2 = Sensor(2)

s1.registrar_leitura(10)
s1.registrar_leitura(20)
s1.registrar_leitura(30)
s1.registrar_leitura(40)
print(s1.get_media())
print(s2.get_media())

