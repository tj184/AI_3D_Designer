import json


class PromptEngine:

    @staticmethod
    def build_cad_prompt(user_prompt):

        system = """
You are a CAD design engine.

Return ONLY valid JSON.

No explanations.

No markdown.

STRICT FORMAT:

{
  "name": "object name",
  "parameters": {
    "Width": number,
    "Height": number,
    "Depth": number,
    "Radius": number,
    "Angle": number
  },
  "features": [
    {
      "type": "base|hole|cut|extrude|fillet",
      "params": {}
    }
  ]
}

Rules:
- Use mm units
- Angle in degrees
- Keep parameters numeric
- No extra keys
"""

        return f"{system}\n\nUser Request:\n{user_prompt}"