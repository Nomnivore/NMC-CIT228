def city_country(city, country, population=None):
    formatted = f"{city.title()}, {country.title()}"

    if population is not None:
        formatted = f"{formatted} - population {population}"

    return formatted
