class AveVoadora:
    def voar(self):
        pass

class AveTerrestre:
    def andar(self):
        pass
        
class AveAquatica:
    def nadar(self):
        pass

class Pato:
    def __init__(self):
        self.aerial_ability = AveVoadora()
        self.aquatic_ability = AveAquatica()

    def voar(self):
        self.aerial_ability.voar()

    def nadar(self):
        self.aquatic_ability.nadar()

class Pinguim(AveTerrestre):
    def andar(self):
        pass