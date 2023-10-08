# Distribuição de verbas da Secom para canais jornalísticos por assinatura

## O projeto:

De que forma a Secom (Secretaria de Comunicação) do governo federal distribuiu verbas publicitárias públicas para os três canais jornalísticos por assinatura (Globonews, CNN Brasil e Jovem Pan News TV) entre 2019 e 2023.

A escolha 

### Contexto:

Com a eleição de Jair Bolsonaro, em 2018, um dos pontos abordados em sua campanha presidencial foi a revisão para renovar a concessão do Grupo Globo e seus canais de televisão - entre eles, a Globonews, exclusivo de jornalismo 24 horas.

A partir de 2020, a CNN Brasil inicia suas transmissões. A Jovem Pan News TV, tradicional em outras mídias, como rádio e internet, começa a transmitir sua programação em 2021.

Esta última traz uma linha editorial claramente de apoio ao governo eleito. A Globonews coloca-se como contraponto. A CNN Brasil ora pende para um lado, ora para outro.

No início de 2020, a OMS decreta pandemia mundial por conta da Covid-19. O então presidente Bolsonaro ganha protagonismo ao defender ideias negacionistas sobre a pandemia, além de difundir notícias falsas e discursos de ódio contra minorias e oposicionistas.

A Jovem Pan não só apenas repercute estes discursos como também os chancela a partir de seu grupo de analistas.

Neste contexto, a Globonews faz o contraponto nas diversas áreas comentadas pelo então presidente (saúde, segurança, pauta de costumes, entre outras).

A distribuição por verbas federais via Secom mostram, no gráfico final, o claro favorecimento da Jovem Pan, sobretudo no ano de 2022 (ano de eleições majoritárias), e consequente diminuição de destinações para a Globonews. A CNN Brasil mostrou uma certa estabilidade.

Em que pese, também, o contexto da pandemia, em que vultosos valores tiveram que ser destinados à pasta da Saúde, o gráfico final mostra o grande corte publicitário para a Globonews, e consequente aumento para a Jovem Pan.

Os três canais (Globonews, CNN Brasil e Jovem Pan News TV) foram escolhidos para o projeto de comparação devido aos números apresentados em suas audiências, conforme o portal de notícias **Poder 360**, de 4 de julho de 2023. As outras duas emissoras (Band News e Record News) apresentaram baixas audiências e, portanto, não tiveram verbas consideradas interessantes para o projeto.

[TVs de notícias têm audiência conjunta de 248,4 mil pessoas](https://www.poder360.com.br/midia/tvs-de-noticias-tem-audiencia-conjunta-de-2484-mil-pessoas/)

## Objetivo:

A partir dos dados disponíveis no site da Secom, analisar como os valores foram distribuídos para os canais por assinatura. E se estes valores guardam relação com o direcionamento político/ideológico do governo Bolsonaro.

## Estrutura do repositório:

* **dados:** arquivos **.csv** baixados no site da Secom;
* **img:** capturas de tela e gráficos do projeto;
* **códigos:** estrutura dos códigos para **Jupyter Notebook** (.ipynb) e **VSCode** (.py);
* **english version:** a translate of **reademe.md** (.pdf).

## Linguagem utilizada:

* **Python**

## Bibliotecas:

* **Pandas**
* **Plotly**

## Metodologia:

Após importar as bibliotecas necessárias, foi feita a leitura do dataset .csv baixado do site da Secom.

<img src="/img/dataset.png">

###
Em seguida, foi realizada a filtragem do dataset para:

* Obter apenas os canais Globonews, CNN Brasil e Jovem Pan News TV;
* Tratar os valores monetários para excluir os símbolos de Real (R$);
* Converter os mesmos valores para float, uma vez que seria necessário agrupar e somar os mesmos para cada ano (2019 a 2023);
* definir um novo dataset com os filtros e valores;
* preencher as variáveis nulas com valores 0 (zero), uma vez que CNN Brasil e Jovem Pan News TV não haviam iniciado suas respectivas transmissões.

<img src="/img/dataset_valores_zero.png">

###
Após ter o dataset com todas as informações necessárias, a escolha do gráfico foi a de colunas agrupadas em função dos anos (2019, 2020, 2021, 2022 e 2023) e dos canais (Globonews, CNN Brasil e Jovem Pan News TV).

<img src="/img/secom_tv_assinatura.png">
