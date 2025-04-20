import requests

# Указываем URL и параметры запроса
url = "https://api.github.com/search/repositories"
params = {
    "q": "language:html"
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Выводим статус-код ответа
print("Status Code:", response.status_code)
print(response.json())