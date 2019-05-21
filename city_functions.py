def get_full_name(city, country, population = 0):
    """Display city and country as a string"""
    
    if population:
        full_name = city.title() + ", " + country.title() + " - population " + str(population)
    else:
        full_name = city.title() + ", " + country.title()

    return full_name