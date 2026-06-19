class Sketch:

    def __init__(self, name="Sketch"):

        self.name = name
        self.entities = []   # lines, circles, arcs
        self.constraints = []

    ########################################################

    def line(self, x1, y1, x2, y2):

        self.entities.append({
            "type": "line",
            "p1": (x1, y1),
            "p2": (x2, y2)
        })

    ########################################################

    def circle(self, x, y, r):

        self.entities.append({
            "type": "circle",
            "center": (x, y),
            "radius": r
        })

    ########################################################

    def add_constraint(self, constraint):

        self.constraints.append(constraint)

    ########################################################

    def export(self):

        return {
            "name": self.name,
            "entities": self.entities,
            "constraints": self.constraints
        }