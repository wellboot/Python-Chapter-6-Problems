# old MacDonald



def verses():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


def main(animal, noise):
    verses()
    print("And on that farm he had a", animal + " Ee-igh, Ee-igh, Oh!")
    print("With a", noise + ", ", noise + " here and a", noise + " ,", noise + " there")
    print("Here a", noise + " there a", noise + " , everywhere a", noise + " ,", noise)
    verses()

main("cow", "moo")