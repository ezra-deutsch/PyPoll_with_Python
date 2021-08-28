""" x = 0
while x <= 5:
        print(x)
        x = x +1 """

""" numbers = [0,1,2,3,4]
for num in numbers:
    print(num) """

""" counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)
 """
""" if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.") """



""" score = int(input("What is the test score?"))
if score >= 90:
    print("Your grade is an A.")
else:
    if score >= 80:
        print("Your grade is a B.")
    else:
        if score >= 70:
            print("Your grade is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print("Your grade is a F.")
 """
""" if score >= 90:
    print("Your grade is an A.")
elif score >= 80:
    print("Your grade is a B.")
elif score >= 70:
    print("Your grade is a C.")
elif score >= 60:
    print("Your grade is a D.")
else:
    print("Your grade is a F.") """

""" counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.") """



candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

""" voting_data = [{'county':'Arapahoe', 'registered_voters': 422829},
                {'county':'Denver', 'registered_voters': 463353},
                {'county':'Jefferson', 'registered_voters': 432438}]
for county_dict in voting_data:
    print(f"{county_dict.keys} county has {county_dict.values:,} registered voters.") """

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)