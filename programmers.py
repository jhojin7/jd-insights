# programmers
import requests
import json
import pandas as pd
import os
from bs4 import BeautifulSoup

prog_url = "https://career.programmers.co.kr/api/v1/career/job_positions"
headers = {"Cookie": os.getenv("PROGRAMMERS_COOKIE")}
resp = requests.get(prog_url, headers=headers)
# data = resp.json()["jobPositions"]
# json.dump(data, open("programmers.json", "w", encoding="utf-8"), ensure_ascii=False)

jobs = json.loads(open("programmers.json", "r", encoding="utf-8").read())
# print(jobs[0])

job_url = lambda job_id: f"https://career.programmers.co.kr/api/job_positions/{job_id}"
resp = requests.get(job_url(jobs[0]["id"]), headers=headers)
jd = resp.json()
print()
print(jd)
print(jd["jobPosition"].keys())


tmp = [
    jd["jobPosition"]["additionalInformation"],
    jd["jobPosition"]["description"],
    jd["jobPosition"]["preferredExperience"],
    jd["jobPosition"]["requirement"],
]
job_description = []

for x in tmp:
    bs = BeautifulSoup(x, "lxml")
    t = bs.get_text()
    job_description.append(t)

print("".join(job_description))
