from core.copilot.intent_parser import IntentParser
from core.copilot.feature_generator import FeatureGenerator
from core.copilot.manufacturing_rules import ManufacturingRules


class DesignBrain:

    def __init__(self, context):

        self.context = context

        self.intent_parser = IntentParser()
        self.feature_generator = FeatureGenerator()
        self.rules = ManufacturingRules()

    ########################################################

    def design(self, prompt):

        self.context.logger.info("Design Brain activated")

        # STEP 1: Understand intent
        intent = self.intent_parser.parse(prompt)

        # STEP 2: Generate features
        features = self.feature_generator.generate(intent)

        # STEP 3: Validate manufacturing rules
        warnings = self.rules.validate(features, intent)

        # STEP 4: Base parameters
        params = self._default_params(intent)

        return {
            "name": intent["object"],
            "parameters": params,
            "features": features,
            "warnings": warnings,
            "intent": intent
        }

    ########################################################

    def _default_params(self, intent):

        if intent["object"] == "phone_holder":

            return {
                "Width": 80,
                "Depth": 90,
                "Height": 120
            }

        if intent["object"] == "container":

            return {
                "Width": 100,
                "Depth": 100,
                "Height": 50
            }

        return {
            "Width": 100,
            "Depth": 100,
            "Height": 20
        }