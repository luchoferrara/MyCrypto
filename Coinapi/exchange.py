import requests

apikey = '347d33e6-f7f4-4649-8b7b-973976596b5a'
server = 'https://rest.coinapi.io'
endpoint = ''
headers = {
    'X-CoinAPI-Key': apikey
}


seguir = 's'

while seguir == 's':
    # vista
    origen = input('¿Qué moneda quieres cambiar? ')
    destino = input('¿Qué moneda quieres obtener? ')
    cantidad = float(input(f'¿Cuantos {origen} quieres gastar? '))
    # /vista

    # modelo
    url = server + endpoint + '/' + origen + '/' + destino

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # respuesta OK
        exchange = response.json()
        rate = exchange.get('rate', 0)
        resultado = cantidad * rate
        # /modelo
        print(f'Un {origen} vale lo mismo que {rate} {destino}')
        print(f'{cantidad} {origen} equivalen a {resultado} {destino}')
    else:
        # error
        print('Error', response.status_code, ':', response.reason)

    seguir = ''
    while seguir.lower() not in ('s', 'n'):
        seguir = input('¿Quieres consultar de nuevo? (s/n) ').lower()

print('FIN del programa')
