from petstablished_finder import PetstablishedFinder
from petango_finder import PetangoFinder
import json


def main():
	# List of all unique dogs available for adoption
	dogs = []
	# import pdb; pdb.set_trace()

	######### ALL DOG RESCUE SITES #########


	# Matchdog Rescue
	mdrf = PetstablishedFinder('https://petlover.petstablished.com/organization/243592?page=', multiple_pages=True)
	mdrf.run()
	dogs.extend(mdrf.dogs)

	# PawzAbilitiesPA
	pawzabilities = PetstablishedFinder('https://petlover.petstablished.com/organization/666923?page=', multiple_pages=True)
	pawzabilities.run()
	dogs.extend(pawzabilities.dogs)

	# Saved Me Rescue
	savedmerescue = PetangoFinder('https://www.petango.com/shelter_pets?shelterId=2399#page-', multiple_pages=True)
	savedmerescue.run()
	dogs.extend(savedmerescue.dogs)

	# all4pawsrescue
	allpawsrescue = PetangoFinder('https://www.petango.com/shelter_pets?shelterId=2027#page-', multiple_pages=True)
	allpawsrescue.run()
	dogs.extend(allpawsrescue.dogs)

	# animal adoption center nj
	aacnj = PetangoFinder('https://www.petango.com/shelter_pets?shelterId=3986&speciesId=1#page-', multiple_pages=True)
	aacnj.run()
	dogs.extend(aacnj.dogs)

	# Print all dogs seen across sites available for adoption
	print(json.dumps(dogs, indent=4, sort_keys=True))
	print(len(dogs))


if __name__ == "__main__":
    # execute only if run as a script
    main()
