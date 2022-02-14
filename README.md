# extract-pdf-images
![Supported Python Version](https://img.shields.io/badge/python-3.8.0-orange.svg "Supported Python Version")

Repositório com código Python para extrair todas as imagens de um PDF


## Requisitos
* Python 3.8.0


## Instalação
Todas as dependências do projeto devem ser instaladas em um `virtualenv`. Para criar o venv e instalar todas as dependências siga os passos abaixo:

```
$ /usr/bin/python3.8 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip setuptools wheel
(venv) $ pip install --upgrade -r requirements.txt
```

## Execução
Para executar o código e extrair as imagens do PDF é necessário informar o PDF de origem e a pasta de destino das imagens:

```
$ source venv/bin/activate
(venv) $ python extract-pdf-images.py <caminho_pdf> <pasta_destino>
```


## Mantenedores
* Jônatas Trabuco Belotti - [jonatas.t.belotti@hotmail.com](jonatas.t.belotti@hotmail.com)