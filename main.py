from petstablished_finder import PetstablishedFinder
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



	# Print all dogs seen across sites available for adoption
	print(json.dumps(dogs, indent=4, sort_keys=True))
	print(len(dogs))


if __name__ == "__main__":
    # execute only if run as a script
    main()