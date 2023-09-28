import requests
import json

# Мой токен
trainer_token = "f7843bd6d929364365b252f979cefe70"

# URL для создания покемона
url = "https://api.pokemonbattle.me:9104/pokemons"

# Заголовки запроса
headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

# JSON-тело запроса для создания покемона
pokemon_data = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

# Выполнение POST-запроса
response = requests.post(url, headers=headers, json=pokemon_data)

# Проверка статуса ответа
if response.status_code == 200:
    # Парсинг JSON-ответа
    created_pokemon = response.json()
    print("Покемон успешно создан:")
    print("Имя покемона:", created_pokemon.get("name"))
    print("Фото:", created_pokemon.get("photo"))
    # Другие свойства покемона можно вывести аналогичным образом
else:
    print("Ошибка при создании покемона. Статус код:", response.status_code)
    print("Текст ошибки:", response.text)

import requests
import json

# Мой токен
trainer_token = "f7843bd6d929364365b252f979cefe70"

# URL для изменения имени покемона
url = "https://api.pokemonbattle.me:9104/pokemons"

# Заголовки запроса
headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

# JSON-тело запроса для изменения имени покемона
update_data = {
    "pokemon_id": "11449",  # ID вашего покемона, который вы хотите изменить
    "name": "Skanzas",    # Новое имя покемона
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"  # Новая фотография покемона
}

# Выполнение PUT-запроса
response = requests.put(url, headers=headers, json=update_data)

# Проверка статуса ответа
if response.status_code == 200:
    # Парсинг JSON-ответа
    updated_pokemon = response.json()
    print("Покемон успешно изменен:")
    print("Имя покемона:", updated_pokemon.get("name"))
    print("Фото:", updated_pokemon.get("photo"))
    # Другие свойства покемона можно вывести аналогичным образом
else:
    print("Ошибка при изменении покемона. Статус код:", response.status_code)
    print("Текст ошибки:", response.text)

import requests
import json

# Мой токен
trainer_token = "f7843bd6d929364365b252f979cefe70"

# URL для поймать покемона в покебол
url = "https://api.pokemonbattle.me:9104/trainers/add_pokeball"

# Заголовки запроса
headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

# JSON-тело запроса для поймать покемона в покебол
catch_data = {
    "pokemon_id": "11449"  # ID вашего покемона, который вы хотите поймать в покебол
}

# Выполнение POST-запроса
response = requests.post(url, headers=headers, json=catch_data)

# Проверка статуса ответа
if response.status_code == 200:
    # Парсинг JSON-ответа
    result = response.json()
    if result.get("success"):
        print("Покемон успешно пойман в покебол!")
    else:
        print("Не удалось поймать покемона. Причина:", result.get("message"))
else:
    print("Ошибка при попытке поймать покемона. Статус код:", response.status_code)
    print("Текст ошибки:", response.text)


