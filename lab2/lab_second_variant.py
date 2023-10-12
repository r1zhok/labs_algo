def min_width(n: int, w: int, h: int) -> int:
    if 1 <= n <= 1012 and 1 <= w <= 109 and 1 <= h <= 109:
        my_number = n * w * h
        result = 0
        variable1 = 0

        while True:
            variable = result // h
            if variable != 0:
                if n % variable == 0:
                    variable1 = (n // variable)
                else:
                    variable1 = (n // variable) + 1
            if result * result >= my_number and result // variable1 >= w:
                return result
            result += 1


print(min_width(8, 7, 1))
