class Bmi_test:


    @staticmethod
    def bmi_calc(weight, height):
        if type(weight) != int and type(weight) != float:
            return "Worng Type"
        if height <= 0 :
            return "Invalid height"
        if weight <= 0:
            return "Invalid weight"
        return weight / pow(height,2)

    def bmi_check(bmi):
        if(bmi > 18.5 and bmi < 25):
            return "A proper bmi"
        elif (bmi > 25):
            return "Overweight"
        elif (bmi < 18):
            return "Underweight"