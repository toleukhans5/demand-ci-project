from demand import total_sales, average_sales, demand_level


def test_total_sales():
    sales = [10, 20, 30]
    assert total_sales(sales) == 60


def test_average_sales():
    sales = [20, 40, 60]
    assert average_sales(sales) == 40


def test_demand_level():
    sales = [100, 120, 110]
    assert demand_level(sales) == "Жоғары"
