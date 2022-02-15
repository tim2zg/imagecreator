# An example to get the remaining rate limit using the Github GraphQL API. # FROM https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
import os
from dotenv import load_dotenv
import requests

load_dotenv()

headers = {"Authorization": "Bearer " + str(os.getenv("GITHUB_TOKEN"))}


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = """
{
            user(login:"tim2zg") {
                contributionsCollection(from: "2022-01-01T00:00:00Z", to:"2022-12-31T23:59:59Z") {
                  	contributionYears 
                }
            }
        }
"""

result = run_query(query)  # Execute the query
print(result["data"]["user"]["contributionsCollection"]["contributionYears"])

years = {}

for i in result["data"]["user"]["contributionsCollection"]["contributionYears"]:
    query = """
    {
                user(login:"tim2zg") {
                    contributionsCollection(from: "%d-01-01T00:00:00Z", to:"%d-12-31T23:59:59Z") {
                        contributionCalendar {
                            totalContributions
                            weeks {
                                contributionDays {
                                contributionCount
                                date
                                }
                            }
                        }
                    }
                }
    }
"""%(i,i)

    years[i] = run_query(query)["data"]["user"]["contributionsCollection"]["contributionCalendar"]  # Execute the query

print(reversed(years))

dates = {}

for i in reversed(years):
    for j in years[i]["weeks"]:
        print(j["contributionDays"])
        for k in j["contributionDays"]:
            dates[k["date"]] = k["contributionCount"]

reihenvolge = sorted(dates, key=lambda x: x[1], reverse=True)

totalcontributes = 0


for i in reihenvolge:
    totalcontributes += dates[i]

print(totalcontributes)
