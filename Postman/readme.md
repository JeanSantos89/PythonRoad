- Sempre ao utilizar API's é necessário ler a documentação da mesmma, para entender como utilizar.

- API rest começa com https

    O que são endpoints?
        URL específica que acessa para envio ou recebimento de dados do sistema

    Com get:
        Colocamos os parâmetros que desejamos de acordo com os tipos de dados que há na response da API;
        Case Sensitive;
        Query params - Filtrar com varias informações
        Path variables - Escolher um específico, por exemplo ID

    Post:
        Para enviar algum dado, de acordo com a documentação: pode ser que seja preciso colocar em RAW para enviar como JSON;
        Alguns end points precisa ter autorização pra pegar lidar com as informações;

        {{$randomfullName}} - Gerador de dados aleatórios, há várias variáveis desse tipo.

    Postman:
        ---- Serve pra se comunicar com APIS
        Não serve para usar como se fosse User Interaction
        Não serve para Performance Testing
        Não serve para Security Testing