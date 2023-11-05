import math
import matplotlib.pyplot as plt
print("c = Circle( )")
class Circle(object):
    def __init__(self):
        print("Radius eingeben:")
        self.radius = float(input())
        print("Bitte die x-Koordinate des Mittelpunktes eintragen:")
        self.centerx = float(input())
        print("Bitte die y-Koordinate des Mittelpunktes eintragen:")
        self.centery = float(input())
    def center(self):
        print("[", self.centerx,",", self.centery,"]")
    def change_center(self):
        print("Bitte die neue x-Koordinate des Mittelpunktes eintragen:")
        self.centerx = float(input())
        print("Bitte die neue y-Koordinate des Mittelpunktes eintragen:")
        self.centery = float(input())
    def draw(self):
        x = [0, 10, 20, 30, 40, 50]
        y = [0, 10, 20, 30, 40, 50]
        plt.figure()
        help = plt.plot(x, y, color="white")
        plt.xlabel("X-Achse")
        plt.ylabel("Y-Achse")
        plt.title("Kreis")
        plt.grid(True)
        circle = plt.Circle((self.centerx, self.centery), self.radius, fill=False, color="blue")
        plt.gca().add_patch(circle)
        plt.show()
    def diameter(self):
        self.diameter_value = self.radius * 2
        print("Der Durchmesser ist:", self.diameter_value,"m.")
    def circumference(self):
        self.circumference_value = 2 * math.pi * self.radius
        print("Der Umfang ist:", self.circumference_value,"m.")
    def space(self):
        self.space_value = math.pi * self.radius ** 2
        print("Die Flaeche des Kreises betraegt:", self.space_value,"m^2.")
    def change_radius(self):
        self.radius = float(input())
        print("Der neue Radius ist:", self.radius, "m.")
    def help(self):
        print("change_radius(): c.Radius aendern\n c.change_center(): Mittelpunkt verschieben\n c.center(): Mittelpunkt anzeigen \n c.draw(): Kreis zeichnen\n c.diameter(): Durchmesser errechnen\n c.circumference(): Umfang errechnen\n c.space(): Flaecheninhalt errechnen\n c.help(): Hilfe")
c = Circle()

        
        
