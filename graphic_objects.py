# -*- coding: utf-8 -*-


class Point(object):
    """ Classe para representar pontos """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Ball(object):
    """Uma bola """
    
    def __init__(self, center, radius,color, velocidade_x, velocidade_y, tipo = ""):
        """Inicializa a bola com um centro e um raio"""
        self.center = center
        self.radius = radius
        self.color = color
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.tipo = tipo
        self.__compute_coordinates()
        
    
    def draw(self, canvas):
        """ Recebe um canvas tkinter e se desenha nele"""
        canvas.create_oval(self.p0.x, self.p0.y,self.p1.x, self.p1.y,fill= self.color)    
        
        
    def move(self, deltax, deltay):
        """Desloca a bola uma distância deltax e deltay """
        self.center.x += deltax
        self.center.y += deltay
        self.__compute_coordinates()
        
    def update(self):
        """ Não faz nada, mas pode ser usado futuramente"""
        pass
        
    def __compute_coordinates(self):
        """Calcula os pontos dos cantos da bola"""
        self.p0 = Point()
        self.p0.x = self.center.x - self.radius
        self.p0.y = self.center.y - self.radius
        self.p1 = Point()
        self.p1.x = self.center.x + self.radius
        self.p1.y = self.center.y + self.radius


class Triangle(object):
    """ Classe triângulo"""
    
    def __init__(self, p0, p1, p2, color):
        """ Recebe três pontos e os armazena em uma lista"""
        self.p = [p0, p1, p2]
        self.color = color
        
    
    def move(self, deltax, deltay):
        """Desloca o triangulo uma distância deltax e deltay """
        for point in self.p:
            point.x += deltax
            point.y += deltay
            
    def draw(self, canvas):
        """ Recebe um canvas e nele desenha o triangulo"""
        p = self.p
        canvas.create_polygon(p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, fill= self.color)
        
    def update(self):
        pass


