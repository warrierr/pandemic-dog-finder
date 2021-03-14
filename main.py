from petstablished_finder import PetstablishedFinder
from petango_finder import PetangoFinder
from animal_sanctuary_society_finder import AnimalSanctuarySocietyFinder
from home_at_last_finder import HomeAtLastFinder
from morris_animal_refuge_finder import MorrisAnimalRefugeFinder
from providence_finder import ProvidenceFinder
from shelterluv_finder import ShelterluvFinder
import json


def main():
	# List of all unique dogs available for adoption
	dogs = []
	dog_counts = {}
	# import pdb; pdb.set_trace()

	######### ALL DOG SHELTER SITES #########


	# Matchdog Rescue
	mdrf = PetstablishedFinder('https://petlover.petstablished.com/organization/243592?page=')
	mdrf.run()
	dogs.extend(mdrf.dogs)
	dog_counts['Matchdog Rescue'] = len(mdrf.dogs)

	# PawzAbilitiesPA
	pawzabilities = PetstablishedFinder('https://petlover.petstablished.com/organization/666923?page=')
	pawzabilities.run()
	dogs.extend(pawzabilities.dogs)
	dog_counts['PawzAbilitiesPA'] = len(pawzabilities.dogs)

	# Saved Me Rescue
	savedmerescue = PetangoFinder('https://www.petango.com/shelter_pets?shelterId=2399#page-')
	savedmerescue.run()
	dogs.extend(savedmerescue.dogs)
	dog_counts['Saved Me Rescue'] = len(savedmerescue.dogs)

	# all4pawsrescue
	allpawsrescue = PetangoFinder('https://www.petango.com/shelter_pets?shelterId=2027#page-')
	allpawsrescue.run()
	dogs.extend(allpawsrescue.dogs)
	dog_counts['all4pawsrescue'] = len(allpawsrescue.dogs)

	# animal adoption center nj
	aacnj = PetangoFinder('https://www.petango.com/shelter_pets?shelterId=3986&speciesId=1#page-')
	aacnj.run()
	dogs.extend(aacnj.dogs)
	dog_counts['animal adoption center nj'] = len(aacnj.dogs)

	# animal sanctuary society
	assf = AnimalSanctuarySocietyFinder('https://www.animalsanctuarysociety.org/adopt', multiple_pages=False)
	assf.run()
	dogs.extend(assf.dogs)
	dog_counts['animal sanctuary society'] = len(assf.dogs)

	# Home at last dog rescue
	half = HomeAtLastFinder('https://www.homeatlastdogrescue.com/adoptable/', multiple_pages=False)
	half.run()
	dogs.extend(half.dogs)
	dog_counts['Home at last'] = len(half.dogs)

	# Morris Animal Refuge
	marf = MorrisAnimalRefugeFinder('https://www.morrisanimalrefuge.org/adopt?type_id=1&gender=&age_id=&size_id=', multiple_pages=False)
	marf.run()
	dogs.extend(marf.dogs)
	dog_counts['Morris Animal Refuge'] = len(marf.dogs)

	# Providence Animal Center
	pac = ProvidenceFinder('https://providenceac.org/adopt/dogs/', multiple_pages=False)
	pac.run()
	dogs.extend(pac.dogs)
	dog_counts['Providence Animal Center'] = len(pac.dogs)

	# Delaware SPCA
	dspca = ShelterluvFinder('https://www.shelterluv.com/api/v3/available-animals/3534?species=Dog&embedded=1&iframeId=shelterluv_wrap_1602619237598&columns=1')
	dspca.run()
	dogs.extend(dspca.dogs)
	dog_counts['Delaware SPCA'] = len(dspca.dogs)

	# Print all dogs seen across sites available for adoption
	print(json.dumps(dogs, indent=4, sort_keys=True))
	print(len(dogs))
	print(dog_counts)


if __name__ == "__main__":
    # execute only if run as a script
    main()
