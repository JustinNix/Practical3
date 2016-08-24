import random
def main():
    INITIAL_POPULATION = 1000
    MAX_BIRTH = 0.2
    MIN_BIRTH = 0.1
    MAX_DEATH = 0.25
    MIN_DEATH = 0.05
    YEAR = 1

    population = INITIAL_POPULATION
    print("Welcome to the Gopher Population Simulator! \n Starting population: {}".format(INITIAL_POPULATION))

    while YEAR < 11:
        growth_Factor = random.uniform(MIN_BIRTH,MAX_BIRTH)
        growth = population * (1+ growth_Factor) - population
        shrink_Factor = random.uniform(MIN_DEATH,MAX_DEATH)
        shrink = population * (1+shrink_Factor) - population
        population *= (1 + (growth_Factor - shrink_Factor))
        print("Year {} \n ***** \n {:.0f} gophers were born. {:.0f} died. \n Population: {:.0f}".format(YEAR, growth, shrink, population))
        YEAR = YEAR + 1

main()