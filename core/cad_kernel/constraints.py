class ConstraintSolver:

    def solve(self, sketch):

        """
        Applies basic geometric constraints
        """

        for c in sketch.constraints:

            if c["type"] == "horizontal":

                self._horizontal(sketch, c)

            elif c["type"] == "vertical":

                self._vertical(sketch, c)

            elif c["type"] == "equal":

                self._equal(sketch, c)

        return sketch

    ########################################################

    def _horizontal(self, sketch, c):

        # force y coordinates equal
        pass

    ########################################################

    def _vertical(self, sketch, c):

        pass

    ########################################################

    def _equal(self, sketch, c):

        pass