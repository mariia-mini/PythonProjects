import requests

#регистрация тренера:
trainers_reg_response = requests.post('https://pokemonbattle.me:9104/trainers/reg', 
                                      headers = {'Content-Type': 'application/json'}, 
                                      json = {"trainer_token": "4b7784aec44c7a11b668d2dc99cbf8f7", 
                                              "email": "vesirah305@kaudat.com", 
                                              "password": "Iloveqa1"})
print(trainers_reg_response.text)

#активация тренера:
trainers_confirm_email_response = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', 
                                                headers = {'Content-Type': 'application/json'}, 
                                                json = {"trainer_token": "4b7784aec44c7a11b668d2dc99cbf8f7"})
print(trainers_confirm_email_response.text)

#создание покемона:
add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                                     headers = {'trainer_token':'4b7784aec44c7a11b668d2dc99cbf8f7', 
                                                'Content-Type': 'application/json'}, 
                                     json = {"name": "Albert", 
                                             "photo": "https://dolnikov.ru/pokemons/albums/001.png"})
print(add_pokemon_response.text)

#изменение имени покемона:
pokemons_response = requests.put('https://pokemonbattle.me:9104/pokemons',
                                 headers = {'trainer_token':'4b7784aec44c7a11b668d2dc99cbf8f7', 
                                            'Content-Type': 'application/json'}, 
                                 json = {"pokemon_id": 6295,
                                         "name": "Albert_2",
                                         "photo": ""})
print(pokemons_response.text)

#ловим покемона в покебол:
trainers_add_pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
                                 headers = {'trainer_token':'4b7784aec44c7a11b668d2dc99cbf8f7', 
                                            'Content-Type': 'application/json'}, 
                                 json = {"pokemon_id": 6295})
print(trainers_add_pokeball_response.text)