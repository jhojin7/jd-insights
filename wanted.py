# wanted
import requests
import json
import pandas as pd
import os
from bs4 import BeautifulSoup
import dotenv

dotenv.load_dotenv(".env")

bookmarks_url = "https://www.wanted.co.kr/api/chaos/bookmarks/v1?limit=20"
headers = {"Cookie": os.getenv("WANTED_COOKIE")}
jobs = json.loads(open("wanted.json", "r", encoding="utf-8").read())

job_url = lambda job_id: f"https://www.wanted.co.kr/api/v4/jobs/{job_id}"
resp = requests.get(job_url(jobs[0]["wd_id"]), headers=headers)
print(resp.url)
jd = resp.json()
print()
# print(jd)
print(jd["job"].keys())

tmp = [
    jd["job"]["detail"]["requirements"],
    jd["job"]["detail"]["main_tasks"],
    jd["job"]["detail"]["intro"],
    jd["job"]["detail"]["benefits"],
]
job_description = []

for x in tmp:
    bs = BeautifulSoup(x, "lxml")
    t = bs.get_text()
    job_description.append(t)

print("".join(job_description))
