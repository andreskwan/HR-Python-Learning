def is_date_before(year_before, month_before, day_before, year_after, month_after, day_after):
    if year_before > year_after:
        return False
    if year_before == year_after:
        if month_before > month_after:
            return False
        if month_before == month_after:
            return day_before < day_after
    return True
