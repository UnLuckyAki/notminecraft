#Добавляем игровой движок Ursina
from ursina import *
#Добавляем из движка возможность управления игроком, там находятся такие параметры как прыжок, гравитация, привязка к клавишам
from ursina.prefabs.first_person_controller import FirstPersonController
#Создание процесса игры с названием app
app = Ursina()

#Создание класса
class Voxel(Button):
    #Функция создания объекта класса - куба
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            color=color.color(0,0,random.uniform(0.9,1)),#случайный оттенок серого у создаваемого куба
        )
    #Функция ответственная за создание новых кубов на правую клавишу мыши и удаления на левую клавишу
    def input(self, key):
        if self.hovered:
            if key =='right mouse down': voxel = Voxel(position= self.position+ mouse.normal)
            if key == 'left mouse down': destroy(self)



for z in range(64):
    for x in range(64):
        voxel = Voxel(position=(x, 0, z))
player = FirstPersonController()




app.run()
