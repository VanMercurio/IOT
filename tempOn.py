import requests

# URL de requisição da API


def obter_temperatura(cidade):
    url = "https://weather-api99.p.rapidapi.com/weather"

    querystring = {"city": cidade}

    headers = {
        "X-RapidAPI-Key": "e4ec702a75msh06cb430c8f487abp16119ajsnc005c091e8f0",
        "X-RapidAPI-Host": "weather-api99.p.rapidapi.com"
    }
    # código
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        temperatura_kelvin = data['main']['temp']
        temperatura_celsius = temperatura_kelvin - 273.15
        return temperatura_celsius
    else:
        print("Erro ao obter temperatura:", response.text)
        return None


def main():
    cidade = input("Digite o nome da cidade para verificar a temperatura: ")
    temperatura = obter_temperatura(cidade)
    if temperatura is not None:
        print(f"A temperatura em {cidade} é {temperatura:.2f}°C.")
    else:
        print("Não foi possível obter a temperatura.")


if __name__ == "__main__":
    main()
