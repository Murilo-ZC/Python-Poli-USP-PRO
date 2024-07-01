# Exemplo de orientação a objetos
class Point():
    def __init__(self, x=0, y= 0):
        self.x = x
        self.y = y
    def motrarPosicao(self):
        print(f"Ola! Estou em: x - {self.x} e y - {self.y}")
    def __str__(self):
        return f"Point: x = {self.x}, y = {self.y}"
        
class Point3D(Point):
    def __init__(self, x=0,y=0,z=0):
        super().__init__(x,y)
        self.z = z
    def mostrarPosicao(self):
        print(f"Ola! Estou em: x - {self.x}; y - {self.y} e z - {self.z}")
    def __str__(self):
        return super().__str__() + f", z = {self.z}"
        
p1 = Point(3,4)
p2 = Point(5,5)
p3 = Point()
p4 = Point3D(4,5,8)

print(p1)
print(p2)
print(p3)
print(p4)

