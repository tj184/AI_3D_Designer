class Feature:

    def __init__(self, name, func, params):

        self.name = name
        self.func = func
        self.params = params


class FeatureTree:

    def __init__(self):

        self.features = []

    ########################################################

    def add(self, feature):

        self.features.append(feature)

    ########################################################

    def rebuild(self, base_model):

        model = base_model

        for f in self.features:

            model = f.func(model, f.params)

        return model