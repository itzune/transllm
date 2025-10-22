import requests

ENDPOINT = "http://localhost:11434/api/generate"
MODEL = "itzune/kimu:9b"


with open("common_voice_basque_dataset.txt", "r") as f:
    for line in f:
        line = line.strip()

        prompt = """Euskaratik ingelesera itzultzen duen itzultzaile automatikoa zara.
        Itzuli esandakoa ahalik eta zehatzenen, beste inolako azalpenik eman gabe eta testu hutsean.
        Ez sartu lerro salto edo hutsunerik zure erantzunaren amaieran.

        Itzuli ondorengo testua:
        {}""".format(
            line
        )
        payload = {"model": MODEL, "prompt": prompt, "stream": False}

        response = requests.post(ENDPOINT, json=payload)
        if response.ok:
            result = response.json()
            print("+ {} \n* {}".format(line, result["response"]))
        else:
            print(response.text)
