class RobustValidator:

    @staticmethod
    def validate(model):

        try:
            solid = model.val()

            volume = solid.Volume()

            if volume <= 0:
                return False, "Zero volume model"

            if volume > 1e9:
                return False, "Model too large"

            return True, "OK"

        except Exception as e:
            return False, str(e)