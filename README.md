# Proposito do projeto
#### 1 realizar o download das imagens/wallpaper a partir de um Json
#### 2 fazer a consulta ao Json via Curl, urllib ou alguma coisa do tipo (nao consegui ainda wtf)
#### 3 identificar cor principal do wallpaper(img baixada)

-- essas anotacoes sao pra consulta pessoal. Nao tentem compreender kk
---------------------------------
# Mind trick (//TODO)
- done - avaliar json de retorno com as informacoes
- done - encontrar o link da imagem
- grepar todos (fiz a consulta navegando entre a estrutura de dado fornecida, nao foi necessario usar o ferramental de texto, mudança de perpectiva) -> consulto o arquivo completo
- done - acessar corretamente a tupla com o valor de download
- done - baixar encaminhando pro path indicado

- ao inves de consultar arquivo, fazer o get direto na url ??? *urllib* -> ainda nao consegui isso
- explorar mais a estrutura, json recebida (por arquivo ou request http) [
	-> formato
	-> tamanho/resolucao
	-> ???
]

- done - identificar a cor dominante ali (obs¹)
- ...
- ...
- ...
- ...

## exemplo do curl
	$ curl https://unsplash.com/napi/search/photos\?query\=desktop%20background\&xp\=\&per_page\=20\&page\=2 >> full.json


******
## processamento de imagem 
- Aqui o proposito é identificar a cor predominante da imagem p/ classificar.
### encontrar cores dominantes em cada 
        R   G   B
	   218,150,149