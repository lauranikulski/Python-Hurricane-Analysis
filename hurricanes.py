# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages

# write your update damages function here:

# convert strings to numbers using float 

def update_damages(damages):
  conversion = {"M": 1000000, "B": 1000000000}
  new_damages = []
  for damage in damages:
    if damage[-1]=='B':
      a = damage.strip('B')
      b = float(a) * conversion['B']
      new_damages.append(b)
    elif damage[-1]=='M':
      c = damage.strip('M')
      d = float(c) * conversion['M']
      new_damages.append(d)
    else: 
      new_damages.append(damage)
  return new_damages    

print(update_damages(damages))

# save new list in a variable so it can be passed in in the next function 

updated_damages = update_damages(damages)


# write your construct hurricane dictionary function here:
def construct_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  number_of_hurricanes = len(names)

  for i in range(number_of_hurricanes):
    hurricanes[names[i]] = {
      "Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": updated_damages[i],
      "Deaths": deaths[i]}
  return hurricanes

#print(construct_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths))

construct_hurricanes_dict = construct_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# save  the dictionary in a new variable so it can be passed into functions later on 

#print(construct_hurricanes_dict['Cuba II']['Year'])

# write your construct hurricane by year dictionary function here:
def construct_hurricane_by_year(construct_hurricanes_dict):
  zipped = zip(years, construct_hurricanes_dict.values())
  hurricanes = {key:value for key, value in zipped}
  return hurricanes

#print(construct_hurricane_by_year(construct_hurricanes_dict))

def construct_hurricane_by_year_two(construct_hurricanes_dict):
  hurricanes={}
  for hurricane in construct_hurricanes_dict:
    hurricanes[construct_hurricanes_dict[hurricane]['Year']] = construct_hurricanes_dict.values()
  return hurricanes

#print(construct_hurricane_by_year_two(construct_hurricanes_dict))

# after checking the hint

def create_year_dictionary(construct_hurricanes_dict):
  # Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary
  # in order to iterate through a dictionary, make your objecs to iterate through dictionaries also
  hurricanes_by_year= {}
  for cane in construct_hurricanes_dict:
      current_year = construct_hurricanes_dict[cane]['Year']
      current_cane = construct_hurricanes_dict[cane]
      #print(current_cane)
      #print(current_year)
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_cane]
      else:
          hurricanes_by_year[current_year].append(current_cane)
          # is ok to append here because the values are lists, so can use a list method append 
  return hurricanes_by_year
#print(create_year_dictionary(construct_hurricanes_dict))

# write your count affected areas function here:
# to count, no need to use counters, list comprehensions 
def count_areas_affected(areas_affected):
  areas_dict={}
  for areas in areas_affected:
      for area in areas:
        if area in areas_dict: 
            areas_dict[area] += 1 
        else:
          areas_dict[area] = 1
  return areas_dict

print(count_areas_affected(areas_affected))

affected_areas_dict = count_areas_affected(areas_affected)


# write your find most affected area function here:
def most_affected_area(affected_areas_dict):
  values=list(affected_areas_dict.values())
  keys=list(affected_areas_dict.keys())
  return f"The area most affected was {keys[values.index(max(values))]} and it was hit {(max(values))} times." 
  
#print(most_affected_area(affected_areas_dict))

# write your greatest number of deaths function here:

def greatest_number_of_deaths(construct_hurricanes_dict):
  values=list(construct_hurricanes_dict.values())
  keys=list(construct_hurricanes_dict.keys())
  print(values)
  print(keys)
  death_values = []
  for value in values: 
    print(value['Deaths'])
    death_values.append(value['Deaths'])
  print(death_values)
  return f"The hurricane with the most deaths was {keys[death_values.index(max(death_values))]} and there were {(max(death_values))} dead."  

print(greatest_number_of_deaths(construct_hurricanes_dict))


# write your catgeorize by mortality function here:

def mortality(construct_hurricanes_dict): 
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  mortality_dict=dict()
  for rating in mortality_scale:
    mortality_dict[rating] = []
  print(mortality_dict)
  # the keys are already in place and now you're simply appending to the lists stored as values 
  for hurricane in construct_hurricanes_dict.values():
    #print(construct_hurricanes_dict.values())
    #print(hurricane['Deaths'])
      if hurricane['Deaths'] == mortality_scale[0]:
        mortality_dict[0].append(hurricane)
      elif hurricane['Deaths'] <= mortality_scale[1] and hurricane['Deaths'] >  mortality_scale[0]:
        mortality_dict[1].append(hurricane)
      elif hurricane['Deaths'] <= mortality_scale[1] and hurricane['Deaths'] >  mortality_scale[1]:
        mortality_dict[2].append(hurricane)
      elif hurricane['Deaths'] <= mortality_scale[3] and hurricane['Deaths'] >  mortality_scale[2]:
        mortality_dict[3].append(hurricane)
      elif hurricane['Deaths'] <= mortality_scale[4] and hurricane['Deaths'] >  mortality_scale[3]:
        mortality_dict[4].append(hurricane)
  return mortality_dict

print(mortality(construct_hurricanes_dict))

# write your greatest damage function here:
def greatest_damage(construct_hurricanes_dict):
  values=list(construct_hurricanes_dict.values())
  keys=list(construct_hurricanes_dict.keys())
  damage_values = []
  for value in values: 
      damage_values.append(value['Damage'])
  for damaged_value in damage_values: 
    #if damaged_value == 'Damages not recorded': 
      #damage_values.remove(damaged_value)
    # decided to go for option that if any string present, it should be removed (to stay away from hardcoding)
    if isinstance(damaged_value, str) == True: 
      damage_values.remove(damaged_value)
  #print(damage_values)
  return f"The hurricane with the heaviest damage was {keys[damage_values.index(max(damage_values))]} and it cost ${(max(damage_values))}."  

#print(greatest_damage(construct_hurricanes_dict))



# write your catgeorize by damage function here:
def categorise_by_damage(construct_hurricanes_dict): 
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  damage_scale_dict=dict()
  for rating in damage_scale:
    damage_scale_dict[rating] = []
  print(damage_scale_dict)
  # the keys are already in place and now you're simply appending to the lists stored as values 
  for hurricane in construct_hurricanes_dict.values():
    if isinstance(hurricane['Damage'], str) == False: 
      if hurricane['Damage'] == damage_scale[0]:
        damage_scale_dict[0].append(hurricane)
      elif hurricane['Damage'] <= damage_scale[1] and hurricane['Damage'] >  damage_scale[0]:
        damage_scale_dict[1].append(hurricane)
      elif hurricane['Damage'] <= damage_scale[1] and hurricane['Damage'] >  damage_scale[1]:
        damage_scale_dict[2].append(hurricane)
      elif hurricane['Damage'] <= damage_scale[3] and hurricane['Damage'] >  damage_scale[2]:
        damage_scale_dict[3].append(hurricane)
      elif hurricane['Damage'] <= damage_scale[4] and hurricane['Damage'] >  damage_scale[3]:
        damage_scale_dict[4].append(hurricane)
  return damage_scale_dict 

#print(categorise_by_damage(construct_hurricanes_dict))

