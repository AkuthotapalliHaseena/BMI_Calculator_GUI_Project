class BMIService:
    def calculate_bmi(self, weight, height_cm):
        height_m=height_cm/100
        return weight / (height_m* height_m)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
