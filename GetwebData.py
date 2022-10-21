from importlib.resources import path
from bs4 import BeautifulSoup
import requests

url = "http://127.0.0.1:8000/blog/"
req = requests.get(url)


req.encoding = "utf-8"
soup = BeautifulSoup(req.text,'html.parser')
courses = soup.find_all()

courses_list = []
for course in courses:

    courses_list.append(course.int)
    print(courses_list)