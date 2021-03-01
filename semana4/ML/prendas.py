import requests

def classify(text):
    key = "5c5eea10-7a3d-11eb-9f5c-0b7cb48a6326f18360cb-ef7a-4d67-9886-7b0eaa7b1405"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

texto=input("Dime una prenda:")
demo = classify(texto)

label = demo["class_name"]
confidence = demo["confidence"]


print ("result: '%s' with %d%% confidence" % (label, confidence))