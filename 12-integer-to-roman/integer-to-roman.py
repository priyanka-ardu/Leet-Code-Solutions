class Solution:
    def intToRoman(self, num: int) -> str:
        rv_ref = {
            1000:"M",
            900:"CM",
            500: "D", 
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I" }

        roman_num = "" 

        if 1 <= num <= 3999:
            for key, values in rv_ref.items():
                if num == 0:
                    break
                roman_num += values * (num // key)
                num -= (num // key) * key

        return roman_num