def get_country_codes(param):
    # Your code here. Maybe try pseudocoding this one out?
    countries_with_number = prices.split()
    country_list = []
    for country in countries_with_number:
        country_list.append(country[:2])
    return ", ".join(country_list)
