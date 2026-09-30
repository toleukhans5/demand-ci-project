def total_sales(sales):
    return sum(sales)


def average_sales(sales):
    if not sales:
        return 0
    return sum(sales) / len(sales)


def demand_level(sales):
    average = average_sales(sales)

    if average >= 100:
        return "Жоғары"
    elif average >= 50:
        return "Орташа"
    else:
        return "Төмен"
