class Vidas:
    def __init__(self, vidas_iniciales=3):
        self.vidas = vidas_iniciales
        self.game_over = False
    
    def perder_vida(self):
        self.vidas -= 1
        if self.vidas <= 0:
            self.game_over = True
    
    def reiniciar(self):
        self.vidas = 3
        self.game_over = False
    
    def obtener_vidas(self):
        return self.vidas
    
    def esta_game_over(self):
        return self.game_over
