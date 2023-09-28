import requests

def test_get_trainers_status_code():
    # Замените это значением вашего токена
    trainer_token = "f7843bd6d929364365b252f979cefe70"
    
    # URL для запроса GET /trainers
    url = f"https://api.pokemonbattle.me:9104/trainers?trainer_id={trainer_token}"
    
    # Выполнение GET-запроса
    response = requests.get(url)
    
    # Проверка статуса ответа
    assert response.status_code == 200

import requests

# Замените значениями из предоставленных данных
trainer_id = "1545"
expected_trainer_name = "Саня"
trainer_token = "f7843bd6d929364365b252f979cefe70"

def test_get_trainers_name():
    # URL для запроса GET /trainers
    url = f"https://api.pokemonbattle.me:9104/trainers?trainer_id={trainer_id}"
    
    # Выполнение GET-запроса
    response = requests.get(url)
    
    # Проверка статуса ответа
    assert response.status_code == 200
    
    # Парсинг JSON-ответа
    trainer_data = response.json()
    
    # Проверка имени тренера в ответе
    assert trainer_data.get("trainer_name") == expected_trainer_name

