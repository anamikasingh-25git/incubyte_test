import re  # USe Regular expression


class Calculator:
    def Calculate_Sum(self, numbers):
        if not numbers:  # input empty return 0
            return 0

        negative_numbers = []
        # string starts with "//"
        if numbers.startswith("//"):
            delimiter = numbers[2:3]  # extract
            numbers = numbers[4:]  # remove delimiter

            # split numbers or newline
            numbers_list = re.split(f"[{delimiter}\n]", numbers)

            # check negative value
            for num in numbers_list:
                num = int(num)

                if num < 0:
                    negative_numbers.append(num)  # add negative_numbers list

            if negative_numbers:
                raise ValueError(
                    f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}"
                )

            # Return sum numbers
            return sum(map(int, numbers_list))

        else:
            # split numbers
            numbers_list = re.split("[,\n]", numbers)

            for num in numbers_list:
                num = int(num)
                if num < 0:
                    negative_numbers.append(num)

            if negative_numbers:
                raise ValueError(
                    f"Negative numbers not allowed: {', '.join(map(str, negative_numbers))}"
                )

            return sum(map(int, numbers_list))
        

if __name__ == "__main__":
    cal = Calculator()

    print(cal.Calculate_Sum(""))  # returns 0
    print(cal.Calculate_Sum("1"))  # returns 1
    print(cal.Calculate_Sum("1,2,3"))  # returns 6
    print(cal.Calculate_Sum("1\n2,3"))  # returns 6
    print(cal.Calculate_Sum("//;\n1;2"))  # returns 3

    try:
        print(cal.Calculate_Sum("1,2,-3,4"))
    except ValueError as e:
        print(e)  # negative numbers not allowed: -3
