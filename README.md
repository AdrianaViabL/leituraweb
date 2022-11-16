# leituraweb
atividade extra

Projeto para empresa

Esse codigo recebe UM arquivo .txt com uma lista de urls, que serão 
varridos e trazido uma resposta em JSON com as urls dos logos, telefones

# IMPORTANTE
O arquivo deve ser adicionado a pasta 'file' no projeto, com a extensão .txt existindo

## Formato do JSON de retorno 
``` bash
{
    'logo':'https:xxxxxx',
    'phone':['123456789', '123456798'],
    'website':'https:xxxxxx',
}
``` 

### ativando ambiente virtual
``` bash
source venv/local/bin/activate
```

### Usando o Docker
instalando o docker-compose

``` bash
sudo apt-get install docker-compose
```

Para a montagem do docker
``` bash
sudo docker build url_read .
```

Para executar:
``` bash
sudo docker run url_read
``` 