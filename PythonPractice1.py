# Dominic Muhairwe
# M23B13/024
# Python practice....5 Classes....5 Methods

# Class 1
class Intro:
    def __init__(self, my_intro):
        self.my_intro = my_intro

    # Method 1
    def show_my_intro(self):
        print("Hi, heres where i live in the", self.my_intro)

myIntro = Intro("Universe")
myIntro.show_my_intro()

# Class 2
class Galaxy:
    def __init__(self, galaxy_name):
        self.galaxy_name = galaxy_name

    # Method 2
    def show_my_galaxy(self):
        print("Galaxy: ", self.galaxy_name)

galaxyInfo = Galaxy("The Milky Way")
galaxyInfo.show_my_galaxy()


# Class 3
class System:
    def __init__(self, system_name):
        self.system_name = system_name

    # Method 3
    def show_my_system(self):
        print("System: ", self.system_name)

systemInfo = System("The Solar System")
systemInfo.show_my_system()


# Class 4
class Planet:
    def __init__(self, planet_name):
        self.planet_name = planet_name

    # Method 4
    def show_my_planet(self):
        print("Planet: ", self.planet_name)

planetInfo = Planet("Earth")
planetInfo.show_my_planet()


# Class 5
class Continent:
    def __init__(self, continent_name):
        self.continent_name = continent_name

    # Method 5
    def show_my_continent(self):
        print("Continent:", self.continent_name)

continentInfo = Continent("Africa")
continentInfo.show_my_continent()

# Class 6
class Country:
    def __init__(self, country_name):
        self.country_name = country_name

    # Method 6
    def show_my_country(self):
        print("Country:", self.country_name)

countryInfo = Country("Uganda")
countryInfo.show_my_country()