# Escola Reusar

## Universidade: Universidade Federal do Cariri (UFCA)
## Polo: Itapipoca-Ce
## Semestre: 2025.2
## Disciplina: Projeto Integrado
## Equipe 9
- SARAH OLIVEIRA LUCAS DIÓGENES (2025013808)
- SAULO VICTO SOARES (2025013853)
- PABLO HENRIQUE LIMA DE ARAUJO (2025013700)
- VINICIUS TABOSA DOS SANTOS (2025013890)

## Escola Reusar e possíveis usos da nossa solução


O projeto Escolar Reusar tem como objetivo principal conectar pessoas que desejam doar materiais escolares a indivíduos ou instituições que necessitam desses itens e que estejam na mesma cidade ou bairros em volta do doador.
Facilitando qualquer usuário na busca por locais de doação de maneira rápida e no descobrimento de novas entidades que precisam de materiais escolares.

A aplicação web segue o seguinte fluxo: o usuário acessa a plataforma, que solicita a identificação do seu perfil, doador ou recebedor, e em seguida, o direciona para o formulário de cadastro correspondente. Caso o usuário seja um recebedor, ele poderá criar uma publicação descrevendo seu pedido de doação, que será listado em feed com outros pedidos de outros usuários. Os doadores, ao acessar a plataforma, verão todos as publicações de pedidos e decidirá qual entidade ajudar.

## Exemplo de uso
Um professor que oferece aulas de reforço em matemática está precisando de livros de matemática, então ele acessa o site Escola Reusar e cria um pedido de doação.
No bairro do lado, um jovem que acabou de sair do ensino médio, deseja repassar os livros da escola por ocuparem muito espaço e entra no site Escola Reusar, ao indicar sua localização, o site mostra que no bairro vizinho tem alguém precisando de livros de matemática.
Os dois usuários entram em contato e realizam a doação.

## 💾 Projeto Físico de Banco de Dados

 📌 O que é?
O projeto físico de banco de dados é a etapa na qual transformamos o modelo do sistema em estruturas reais dentro do banco. Em termos mais técnicos, é o processo de escolha de estruturas específicas e caminhos de acesso para os arquivos do banco de dados, visando um bom desempenho. Nessa etapa são definidos:
    📊 Tabelas e colunas;
    🔤 Tipos de dados;
    🔑  Chaves primárias e estrangeiras;
    ⚡Índices e regras de integridade;
    🗂️ Estratégias de organização dos dados.

 ⚙️Como isso funciona na prática?
As diferentes formas de organizar os dados, como indexação para acelerar consultas, organização de registros em arquivos e controle de integridade dos dados, são oferecidas pelos Sistemas Gerenciadores de Banco de Dados (SGBDs). Como exemplos destes sistemas, têm-se:
    🐘 PostgreSQL;
    🐬 MySQL;
    🪟 SQL Server.

 🚀 Por que isso é importante para quem está aprendendo programação?
O correto entendimento do projeto físico ajuda a criar sistemas mais organizados e confiáveis; evitar duplicidade ou inconsistência de dados; melhorar o desempenho das aplicações; desenvolver soluções mais próximas da realidade do mercado. Assim, entenda que a modelagem de dados define quais os dados existentes e o projeto físico define como esses dados são armazenados e acessados.

 🎓Exemplo prático - Escola Reusar
No projeto Escola Reusar, o projeto físico foi importante para fazer a transformação do modelo conceitual em tabelas reais. Por exemplo, a entidade usuário, virou a tabela usuário. Os perfis doador e recebedor foram implementados como especializações dessa tabela de usuário. E as chaves estrangeiras garantem que não exista doação ou pedido sem um usuário válido. Considerando tudo isso, evita-se inconsistência no sistema e ajuda a manter os dados organizados.

