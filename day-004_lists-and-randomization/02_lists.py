# Write a program for a list of the US States that chooses a State at random.
# Additionally, add a State to the list.

import random
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
# Print the full list
print(states_of_america, '\n')

# Print a random U.S. State
print(states_of_america[random.randint(0, len(states_of_america) - 1)])

# Add Puerto Rico to the Union
states_of_america.append("Puerto Rico")

# Print a random U.S. State (now including Puerto Rico!)
print(states_of_america[random.randint(0, len(states_of_america) - 1)])
