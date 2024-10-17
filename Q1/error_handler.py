# Custom error for translation
class TranslationError(Exception):
    pass

# Error handler to handle different types of errors in the future
class ErrorHandler:
    def handle(self, error_message):
        print(f"Error: {error_message}")

class AdvancedErrorHandler(ErrorHandler):
    # Example of method overriding
    def handle(self, error_message):
        print(f"Advanced Error: {error_message}")
