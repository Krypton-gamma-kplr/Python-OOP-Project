class Product :
    def __init__(self,cost, price,marque):
        self.cost = cost
        self.price=price
        self.marque=marque

class Meubles(Product):
    def __init__(self, cost, price, marque, matériaux,couleur ,dimensions):
        super().__init__(cost, price, marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions

class Canape(Product):
    def __init__(self, cost, price, marque, matériaux,couleur ,dimensions):
        super().__init__(cost, price, marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions

class Chaise(Product):
    def __init__(self, cost, price, marque, matériaux,couleur ,dimensions):
        super().__init__(cost, price, marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions

class Table(Product):
    def __init__(self, cost, price, marque, matériaux,couleur ,dimensions):
        super().__init__(cost, price, marque)
        self.matériaux = matériaux
        self.couleur = couleur
        self.dimensions = dimensions
   

# Créer une instance de la classe Canape avec les paramètres cost=1000, price=2000, marque="OKLM", matériaux="Cuir", couleur="Blanc", dimensions=(200, 100, 80).
canape1 = Canape(1000, 2000, "OKLM", "Cuir", "Blanc", (200, 100, 80))

# Créer une instance de la classe Canape avec les paramètres cost=800, price=1600, marque="SIESTA", matériaux="Tissu", couleur="Bleu", dimensions=(150, 90, 70)".
canape2 = Canape(800, 1600, "SIESTA", "Tissu", "Bleu", (150, 90, 70))

# Créer une instance de la classe Chaise avec les paramètres cost=50, price=100, marque="PEPOUSE", matériaux="Plastique", couleur="Rouge", dimensions=(50, 50, 70).
chaise1 = Chaise(50, 100, "PEPOUSE", "Plastique", "Rouge", (50, 50, 70))

# Créer une instance de la classe Chaise avec les paramètres cost=75, price=150, marque="PEPOUSE", matériaux="Métal", couleur="Gris", dimensions=(60, 60, 80).
chaise2 = Chaise(75, 150, "PEPOUSE", "Métal", "Gris", (60, 60, 80))

# Créer une instance de la classe Table avec les paramètres cost=250, price=500, marque="TEX", matériaux="Bois", couleur="Chêne", dimensions=(150, 80, 75).
table2 = Table(250, 500, "TEX", "Bois", "Chêne", (150, 80, 75))

# Créer une instance de la classe Table avec les paramètres cost=350, price=700, marque="TEX", matériaux="Verre", couleur="Transparent", dimensions=(120, 60 ,75).
table1 = Table(350 ,700 , "TEX" , "Verre" , "Transparent" , (120 ,60 ,75))
print(table1.marque)
print(chaise1.couleur)