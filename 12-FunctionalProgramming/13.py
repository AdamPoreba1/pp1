def tolerance_percentage(per):
    def ml_check(ml):
        if per == 2:
            if 490 <= (ml) <= 510:
                return f"{ml}: {True}"
            else:
                return f"{ml}: {False}"
        if per == 3:
            if 970 <= (ml) <= 1030:
                return f"{ml}: {True}"
            else:
                return f"{ml}: {True}"
        if per == 5:
            if 1425 <= (ml) <= 1575:
                return f"{ml}: {True}"
            else:
                return f"{ml}: {False}"

        
    

    