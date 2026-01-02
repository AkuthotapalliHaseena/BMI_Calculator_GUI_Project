class BMIUtils:
    @staticmethod
    def validate_input(weight, height):
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
