import requests

url = "https://api.hubspot.com/crm/v3/objects/contacts"

querystring = {"limit":"20","properties":"firstname,email","after":"121"}

payload = ""
headers = {
    "cookie": "__cf_bm=4uj6OY1dnMQKSd0wapB1oWUKJOQRI5d8mD8_JPFOugE-1722532017-1.0.1.1-mFiTCmoGFP4oDRs6yuqjXtZoDMPnXq1ghw6.ioy5HC2oHAxELgLW16kOpTNT9GYJD739kEm8b8AdgZnUWA0UWQ; _cfuvid=JIncPmm3VdRTsC1zb6vE0bq_BFHTdF81uSx6_5NbrxU-1722530551499-0.0.1.1-604800000",
    "User-Agent": "insomnia/9.3.3",
    "Authorization": "Bearer pat-na1-5ff98a29-f5d0-4378-a930-5a939760419f"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
