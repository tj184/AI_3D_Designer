class IntentParser:

    def parse(self, prompt):

        prompt_lower = prompt.lower()

        intent = {
            "object": None,
            "use_case": None,
            "constraints": [],
            "style": None
        }

        # ----------------------------
        # OBJECT DETECTION
        # ----------------------------

        if "phone" in prompt_lower:
            intent["object"] = "phone_holder"
            intent["use_case"] = "consumer_device"

        elif "box" in prompt_lower:
            intent["object"] = "container"

        elif "stand" in prompt_lower:
            intent["object"] = "support_structure"

        # ----------------------------
        # CONSTRAINT EXTRACTION
        # ----------------------------

        if "strong" in prompt_lower:
            intent["constraints"].append("high_strength")

        if "light" in prompt_lower:
            intent["constraints"].append("low_weight")

        if "print" in prompt_lower:
            intent["constraints"].append("3d_printable")

        # ----------------------------

        return intent