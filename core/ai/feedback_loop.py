from core.ai.error_analyzer import ErrorAnalyzer
from core.cad.robust_validator import RobustValidator


class FeedbackLoopEngine:

    def __init__(self, context):

        self.context = context
        self.max_attempts = 3

    ########################################################

    def execute(self, ai_func, prompt):

        """
        Runs AI → CAD → Validate → Repair loop
        """

        attempt = 0

        last_error = None

        while attempt < self.max_attempts:

            attempt += 1

            self.context.logger.info(
                f"AI-CAD Attempt {attempt}"
            )

            try:

                # ----------------------------
                # STEP 1: AI GENERATION
                # ----------------------------

                data = ai_func(prompt, error=last_error)

                # ----------------------------
                # STEP 2: CAD BUILD
                # ----------------------------

                model = self.context.cad_builder.build(data)

                # ----------------------------
                # STEP 3: VALIDATION
                # ----------------------------

                ok, msg = RobustValidator.validate(model)

                if ok:

                    self.context.logger.info("CAD VALID ✔")

                    return {
                        "success": True,
                        "model": model,
                        "data": data,
                        "attempts": attempt
                    }

                # ----------------------------
                # FAILURE → FEEDBACK LOOP
                # ----------------------------

                self.context.logger.warning(f"Validation failed: {msg}")

                last_error = {
                    "validation_error": msg,
                    "data": data
                }

            except Exception as e:

                last_error = ErrorAnalyzer.analyze(
                    e,
                    prompt
                )

                self.context.logger.error(f"CAD Error: {e}")

        return {
            "success": False,
            "error": last_error
        }