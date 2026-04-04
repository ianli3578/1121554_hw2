import requests
import json

access_key = '86b806e4d1cc7ee026c0e04b70747359'
phone_number = '14158586273'
url = f"http://apilayer.net/api/validate?access_key={access_key}&number={phone_number}"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Success")
    else:
        print(f"Error: {response.status_code}")

except Exception as e:
    print(f"Exception: {e}")
