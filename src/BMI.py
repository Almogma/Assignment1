class Bmi_test:


    @staticmethod
    def Bmi_calc(weight, height):
        if height == 0:
            return 0
        return weight / pow(height,2)