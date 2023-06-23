import requests
import config
import datetime
import os
import re

url = config.URL
json = {
    "problem": {
        "problemName": "today",
        "link": "https://leetcode.com/problems/",
        "language": "Python3",
        "lastSolved": datetime.datetime.now().strftime("%m-%d-%Y"),
        "notes": ""
    }
}
headers = {
    "Content-Type": "application/json",
}

directory = '/Users/jeligooch/Desktop/git/LeetCode/Python3'

# Get the list of files in the repository directory
files = os.listdir(directory)


# Iterate through each file
for file_name in files:
    if os.path.isfile(os.path.join(directory, file_name)):
        # Extract the problem number from the file name
        problem_number = re.match(r"(\d+)", file_name).group(1)

        # Format the problem name with number and remove file extension
        problem_name = f"{problem_number}. {file_name.split('.')[0][4:].replace('_', ' ').title()}"

        # Format the link with the capitalized problem name
        link = f"https://leetcode.com/problems/{problem_name.split('.')[1][2:]}/description"

        problem_name = f"{problem_number}. {problem_name.split('.')[1][2:]}"
        problem_name = problem_name.replace("-", " ")

        # Create the JSON payload
        json = {
            "problem": {
                "problemName": problem_name,
                "link": link,
                "language": "Python3",
                # "lastSolved": datetime.datetime.now().strftime("%m-%d-%Y"),
                "lastSolved": "",
                "notes": ""
            }
        }

        # Make the API request
        response = requests.post(url=url, json=json, headers=headers)
        print(f'Renamed "{file_name}" to "{problem_name}"')
        print(response.status_code)


# response = requests.post(url=url, json=json, headers=headers)
# print(response.status_code)
# print(response.text)