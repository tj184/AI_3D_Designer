class GeometryValidator:

    @staticmethod
    def validate(model):
        import cadquery as cq

        try:
            volume = model.val().Volume()
            return volume > 0

        except Exception:
            return False