from models.ai_model import AIModel
from error_handler import TranslationError

# Encapsulation: Wrapping AIModel functionality inside the translator class
class FilipinoTranslator:
    def __init__(self):
        self.model = AIModel()  # Assume AIModel is a simple translation model

    # Polymorphism: Different classes might implement `translate` differently
    def translate(self, text):
        # Call the AI model to translate
        try:
            result = self.model.translate(text)
            if not result:
                raise TranslationError("Translation failed. Please try again.")
            return result
        except Exception as e:
            raise TranslationError(f"An error occurred: {str(e)}")

# Using decorators to add functionality to the translator class
def log_translation(func):
    def wrapper(*args, **kwargs):
        print(f"Translating: {args[1]}")  # Logging translation attempt
        return func(*args, **kwargs)
    return wrapper

class AdvancedFilipinoTranslator(FilipinoTranslator):
    @log_translation  # Applying decorator to log translations
    def translate(self, text):
        return super().translate(text)
