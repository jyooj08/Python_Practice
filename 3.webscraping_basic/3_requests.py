import requests
res = requests.get("http://google.com")
#res = requests.get("http://nadocoding.tistory.com")
print("응답코드: ",res.status_code)

# if res.status_code == requests.codes.ok:
#     print("ok")
# else:
#     print("Error occur", res.status_code)

res.raise_for_status()

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)