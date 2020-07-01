import apiai, json

def textMessage(s):
    request = apiai.ApiAI('c68289d50fc143efa8fa4b4f61812894').text_request()
    request.lang = 'ru'
    request.session_id = 'Small-Talk'
    request.query = s
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']

    if response:
        return response
    else:
        return 'Я вас не понял'

a = ''
while(a!='Выход'):
    s = input('Введите ваше сообщение:')
    print(textMessage(s))
