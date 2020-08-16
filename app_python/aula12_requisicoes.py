#pip install requests
import requests

def retorna_dados_cep(CEP):
    requisicao = 'https://viacep.com.br/ws/{}/json/'.format(CEP)
    retorno = requests.get(requisicao).json()
    if retorno['erro']:
        return 'CEP não encontrado'
    return retorno

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://globallab.org/')
    print(response)
    #print(retorna_dados_pokemon('pikachu')['sprites']['front_shiny'])
    #print(retorna_dados_cep(str(input('Informe o CEP: '))))
    # print(response.status_code)
    # print(response.text)
    # print(type(response.text))
    # print(response.json())
    # print(type(response.json()))
    # dadosCEP = response.json()
    # print(dadosCEP['logradouro'])