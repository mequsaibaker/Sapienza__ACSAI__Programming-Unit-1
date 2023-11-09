# the AnimalBites dataset, stored in the file Health_AnimalBites.csv,
# includes information on over 9,003 animal bites which occurred near
# Louisville, Kentucky from 1985 to 2017 and includes information on
# whether the animal was quarantined after the bite occurred and
# whether that animal was rabid

# each line of the files contains several information about an animal bite:
#     • bite_date: The date the bite occurred
#     • SpeciesIDDesc: The species of animal that did the biting
#     • BreedIDDesc: Breed (if known)
#     • GenderIDDesc: Gender (of the animal)
#     • color: color of the animal
#     • vaccination_yrs: how many years had passed since the last vaccination
#     • vaccination_date: the date of the last vaccination
#     • victim_zip: the zipcode of the victim
#     • AdvIssuedYNDesc: whether advice was issued
#     • WhereBittenIDDesc: Where on the body the victim was bitten
#     • quarantine_date: whether the animal was quarantined
#     • DispositionIDDesc: whether the animal was released from quarantine
#     • headsentdate: the date the animal’s head was sent to the lab
#     • release_date: the date the animal was released
#     • ResultsIDDesc: results from lab tests (for rabies)

# the single information are separated by commas, so for example the line:
# 1985-05-05 00:00:00,DOG,,FEMALE,LIG. BROWN,1,1985-06-20 00:00:00,40229,NO,BODY,1985-05-05 00:00:00,UNKNOWN,,,UNKNOWN
# corresponds to the following bite event:
#     • bite_date: 1985-05-05 00:00:00
#     • SpeciesIDDesc:  DOG
#     • BreedIDDesc:
#     • GenderIDDesc:  FEMALE
#     • color:  LIG. BROWN
#     • vaccination_yrs: 1
#     • vaccination_date:  1985-06-20 00:00:00
#     • victim_zip:  40229
#     • AdvIssuedYNDesc: NO
#     • WhereBittenIDDesc: BODY
#     • quarantine_date:  1985-05-05 00:00:00
#     • DispositionIDDesc:  UNKNOWN
#     • headsentdate:
#     • release_date:
#     • ResultsIDDesc:  UNKNOWN

# write a function to reads the file and returns a tuple (cbe, brs, epy):
# cbe - the total number of cat bite events (1568)
# brs - the list of breeds (['DOG', 'CAT', 'BAT', ...])
# epy - a dictionary containing the number of events per year ({1985: 1, 2009: 14, ...})


def findColCSV(col_num: int, line: str) -> (int, int):
  start_ind = 0
  end_ind = line.find(',')
  for col_ind in range(col_num):
    start_ind = end_ind
    end_ind = line.find(',', start_ind + 1)
  return start_ind, end_ind


def getColData(col_num: int, line: str) -> str:
  start, end = findColCSV(col_num, line)
  return line[start:end].replace(',', '')


#species field number is 1
def totalNumSpeciesBite(species: str, file_path):
  file_r = open(file_path, 'r', encoding='utf8')
  species_bites_count = 0
  for line in file_r:
    if getColData(1, line) == species:
      species_bites_count += 1
  file_r.close()
  return species_bites_count


def findSpeciesList(file_path):
  file_r = open(file_path, 'r', encoding='utf8')
  species_list = []
  for line in file_r:
    species = getColData(1, line)
    if species not in species_list and species != '' and species != 'SpeciesIDDesc':
      species_list.append(species)
  file_r.close()
  return species_list


def extractYear(str_date):
  return str_date[0:4]


def countEventsPerYear(file_path):
  file_r = open(file_path, 'r', encoding='utf8')
  year_dict = {}
  for line in file_r:
    year = extractYear(getColData(0, line))
    if year != '' and year != 'bite_date':
      if year not in year_dict.keys():
        year_dict[year] = 0
      else:
        year_dict[year] += 1
  file_r.close()
  return year_dict


def AnimalBites(dbFile):
  # your code goes here
  pass


if __name__ == "__main__":
  str_line = '1985-05-05 00:00:00,DOG,,FEMALE,LIG. BROWN,1,1985-06-20 00:00:00,40229,NO,BODY,1985-05-05 00:00:00,UNKNOWN,,,UNKNOWN'
  col_num = 4
  start, end = findColCSV(col_num, str_line)
  print(start, end)
  print(str_line[start:end].replace(',', ''))
  print(getColData(col_num, str_line))
  print(totalNumSpeciesBite('CAT', "Health_AnimalBites.csv"))
  print(findSpeciesList("Health_AnimalBites.csv"))
  print(extractYear('1985-06-20 00:00:00'))
  print(AnimalBites("Health_AnimalBites.csv"))
