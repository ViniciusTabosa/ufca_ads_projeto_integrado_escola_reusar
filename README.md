# Escola Reusar

## Universidade: Universidade Federal do Cariri (UFCA)
### Polo: Itapipoca-Ce
### Semestre: 2025.2
### Disciplina: Projeto Integrado
## Equipe 9
- SARAH OLIVEIRA LUCAS DIÓGENES (2025013808)
- SAULO VICTO SOARES (2025013853)
- PABLO HENRIQUE LIMA DE ARAUJO (2025013700)
- VINICIUS TABOSA DOS SANTOS (2025013890)


## 🏫 Escola Reusar e possíveis usos da nossa solução

O projeto Escolar Reusar tem como objetivo principal conectar pessoas que desejam doar materiais escolares a indivíduos ou instituições que necessitam desses itens e que estejam na mesma cidade ou bairros em volta do doador.
Facilitando qualquer usuário na busca por locais de doação de maneira rápida e no descobrimento de novas entidades que precisam de materiais escolares.

A aplicação web segue o seguinte fluxo: o usuário acessa a plataforma, que solicita a identificação do seu perfil, doador ou recebedor, e em seguida, o direciona para o formulário de cadastro correspondente. Caso o usuário seja um recebedor, ele poderá criar uma publicação descrevendo seu pedido de doação, que será listado em feed com outros pedidos de outros usuários. Os doadores, ao acessar a plataforma, verão todos as publicações de pedidos e decidirá qual entidade ajudar.

## 👥 Público-alvo

A plataforma atende dois perfis de usuário, que se encontram dentro do sistema:

- **Doadores**: famílias, estudantes e ex-estudantes que têm material escolar em bom estado sem uso em casa, além de empresas, papelarias e igrejas que queiram destinar material a quem precisa.
- **Recebedores**: estudantes e responsáveis em situação de vulnerabilidade, professores de reforço escolar, projetos sociais, associações de bairro, bibliotecas comunitárias e escolas públicas com falta de material.

O recorte é **local**: a solução prioriza doador e recebedor na mesma cidade ou em bairros vizinhos, para que a entrega seja viável sem custo de frete.

## Exemplo de uso

Um professor que oferece aulas de reforço em matemática está precisando de livros de matemática, então ele acessa o site Escola Reusar e cria um pedido de doação.
No bairro do lado, um jovem que acabou de sair do ensino médio, deseja repassar os livros da escola por ocuparem muito espaço e entra no site Escola Reusar, ao indicar sua localização, o site mostra que no bairro vizinho tem alguém precisando de livros de matemática.
Os dois usuários entram em contato e realizam a doação.

## 🧰 Tecnologias utilizadas

| Tecnologia | Onde é usada | Por que foi escolhida |
|---|---|---|
| **Python 3.13** | Toda a lógica do servidor | Linguagem da disciplina, com biblioteca padrão ampla e leitura simples |
| **FastAPI** | Servidor web e rotas da aplicação | Escreve pouco código para expor uma rota, valida os dados recebidos automaticamente e gera documentação interativa em `/docs` sem configuração |
| **Uvicorn** | Servidor que executa a aplicação | Servidor ASGI recomendado pelo próprio FastAPI, com recarregamento automático durante o desenvolvimento |
| **SQLite** | Banco de dados | Banco embarcado: o banco inteiro é um único arquivo, sem servidor para instalar nem senha para configurar. Isso permite que qualquer pessoa clone o repositório e execute o projeto com um comando. Já vem embutido no Python |
| **HTML e CSS** | Todas as telas da interface | Base da Web; o CSS foi organizado com um arquivo compartilhado (`base.css`) e arquivos específicos por tela |
| **python-multipart** | Leitura dos formulários HTML | Necessário para o FastAPI interpretar dados enviados por `<form>` |
| **Figma** | Wireframes e protótipo de alta fidelidade | Permitiu validar a experiência do usuário antes de escrever código |
| **Git e GitHub** | Versionamento e colaboração | Uma branch por desenvolvedor, com merge na branch principal |
| **Visual Studio Code / PyCharm** | Edição de código | Ambientes usados pela equipe |
| **DBeaver** | Inspeção do banco de dados | Permite abrir o arquivo `.db` e conferir visualmente as tabelas e os registros |

### 📌 Decisão técnica: por que SQLite e não PostgreSQL

O planejamento inicial previa PostgreSQL. Para a entrega do MVP, a equipe optou por **SQLite** pelos seguintes motivos:

1. **Execução imediata por terceiros.** Com PostgreSQL, qualquer pessoa que quisesse rodar o projeto precisaria instalar um servidor de banco, criar usuário, senha e base. Com SQLite, basta executar a aplicação.
2. **Zero dependência externa.** O módulo `sqlite3` já faz parte da biblioteca padrão do Python.
3. **Mesma linguagem SQL.** As tabelas, chaves primárias, chaves estrangeiras e restrições de integridade são escritas em SQL padrão, o que preserva todo o trabalho de projeto físico do banco.

A limitação conhecida do SQLite é permitir apenas uma escrita por vez, o que é irrelevante no escopo deste MVP. Como todo o SQL está isolado nas camadas `src/config/` e `src/repositories/`, a migração para PostgreSQL em uma versão futura exige alterar apenas esses arquivos, sem tocar nas rotas nem na interface.

## 📁 Estrutura do projeto

```
ufca_ads_projeto_integrado_escola_reusar/
├── README.md                            # Documentação do projeto
├── requirements.txt                     # Dependências Python (pip install -r)
├── escola_reusar.db                     # Banco SQLite - GERADO automaticamente, não versionado
├── exemplo-uso/                         # Prints do sistema usados neste README
├── src/
│   ├── main.py                          # Servidor FastAPI: todas as rotas da aplicação
│   ├── index.html                       # Página inicial (landing)
│   ├── config/
│   │   ├── database.py                  # Onde o banco fica e como abrir a conexão
│   │   └── schema.sql                   # Projeto físico: criação das tabelas em SQL
│   ├── repositories/
│   │   └── usuario_repository.py        # Único lugar com SQL da tabela usuario
│   ├── utils/
│   │   └── seguranca.py                 # Geração e verificação de hash de senha
│   ├── models/                          # Classes de domínio do sistema
│   │   ├── usuario.py
│   │   ├── doador.py
│   │   ├── recebedor.py
│   │   ├── doacao.py
│   │   ├── material_escolar.py
│   │   ├── pedido_doacao.py
│   │   └── pedido_material.py
│   ├── paginas/                         # Demais telas da aplicação
│   │   ├── login.html                   # Login
│   │   ├── cadastro.html                # Cadastro de usuário
│   │   ├── lista-pedidos.html           # Feed geral de pedidos
│   │   ├── meus-pedidos.html            # Pedidos do usuário logado
│   │   ├── criacao-pedidos.html         # Criação de pedido de doação
│   │   ├── detalhe-pedido.html          # Detalhe de um pedido
│   │   └── perfil.html                  # Perfil do usuário
│   ├── css/
│   │   ├── base.css                     # Estilos COMPARTILHADOS: reset, cabeçalho e rodapé
│   │   ├── index.css                    # Estilos da landing
│   │   ├── login-cadastro.css           # Estilos das telas de login e cadastro
│   │   ├── pedidos.css                  # Estilos das telas de pedidos
│   │   ├── detalhe-criacao-pedidos.css  # Estilos do detalhe e da criação de pedido
│   │   └── perfil.css                   # Estilos da tela de perfil
│   └── imgs/                            # Logo e ilustrações
└── tests/                               # Testes das classes de domínio
    ├── teste_usuario.py
    └── teste_doacao.py
```

### 🧱 Organização em camadas

O código está separado por responsabilidade. Uma requisição percorre este caminho:

```
Navegador (HTML/CSS)
   │  envia o formulário
   ▼
src/main.py                 camada de rotas: recebe, valida e trata erros
   │  chama uma função
   ▼
src/repositories/           camada de dados: o ÚNICO lugar onde existe SQL
   │  abre a conexão
   ▼
src/config/database.py      camada de conexão: sabe onde o banco está
   │
   ▼
escola_reusar.db            banco de dados
```

A vantagem prática dessa separação é que nenhuma tela conhece o banco, e nenhuma consulta SQL está espalhada pelo código.

## 📲 Instalação e execução

### Pré-requisitos

- **Python 3.11 ou superior** (o projeto foi desenvolvido na versão 3.13)
- **Git**

Não é necessário instalar nenhum servidor de banco de dados.

### 1. Clonar o repositório

```bash
git clone https://github.com/ViniciusTabosa/ufca_ads_projeto_integrado_escola_reusar.git
cd ufca_ads_projeto_integrado_escola_reusar
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

O ambiente virtual mantém as dependências do projeto separadas das do sistema.

```bash
python -m venv .venv
```

Ativar no **Windows**:
```bash
.venv\Scripts\activate
```

Ativar no **Linux / macOS**:
```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python -m uvicorn src.main:app --reload
```

> **Windows:** se o comando `python` abrir a Microsoft Store, use `py` no lugar dele:
> `py -m uvicorn src.main:app --reload`

O comando deve ser executado **na raiz do projeto** (a pasta onde está o `requirements.txt`).
A opção `--reload` reinicia o servidor automaticamente a cada alteração no código.

Saída esperada:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

### 5. Acessar o sistema

Abra no navegador: **http://127.0.0.1:8000**

Para encerrar o servidor, pressione `Ctrl+C` no terminal.

### 📎 Sobre o banco de dados

**Não é necessário criar o banco manualmente.** Na primeira execução, a própria
aplicação cria o arquivo `escola_reusar.db` a partir do script
[`src/config/schema.sql`](src/config/schema.sql).

O arquivo `.db` não é versionado no Git (está no `.gitignore`), porque é um arquivo
binário e cada desenvolvedor tem os seus próprios dados de teste. O que é versionado
é o `schema.sql`, que descreve a estrutura das tabelas.

Para inspecionar o banco visualmente, abra o arquivo `escola_reusar.db` no DBeaver.

## ⚙️ Processo de desenvolvimento
O processo de desenvolvimento foi divido por classes e telas junto com seus respectivos arquivos CSS e adaptação para diferentes telas, a edição do readme do projeto é responsabilidade de toda a equipe.

### 👥 Divisão de tarefas:
 - Pablo:
   - Telas: lista-pedidos.html e meus-pedidos.html
   - CSS: base.css e pedidos.css
   - Classes: usuario.py, doador.py, recebedor.py
 - Sarah:
   - Telas: login.html e cadastro.html
   - CSS: login-cadastro.css
   - Classes: doacao.py
 - Saulo:
   - Telas: detalhe-pedido.html e criacao-pedidos.html
   - CSS: detalhe-criacao-pedidos.css
   - Classes: material_escolar.py
 - Vinicius:
   - Telas: index.html e perfil.html
   - CSS: index.css e perfil.css
   - Classes: pedido_material.py e pedido_doacao.py

### 🔧 Sprint 3 - implementação do back-end

Nesta sprint o projeto deixou de ser um conjunto de telas estáticas e passou a ter servidor e banco de dados. As tarefas foram distribuídas assim:

- **Pablo:** modelagem e criação do banco de dados (`src/config/schema.sql`), camada de conexão (`src/config/database.py`), camada de repositório (`src/repositories/usuario_repository.py`) e proteção de senha por hash (`src/utils/seguranca.py`)
- **Saulo:** servidor FastAPI e rotas da aplicação (`src/main.py`), incluindo o serviço das páginas estáticas e os endpoints de cadastro e login
- **Sarah:** ligação dos formulários de login e cadastro às rotas do servidor, com campos obrigatórios e seleção de perfil
- **Vinicius:** integração das branches, revisão da documentação e validação do fluxo completo na aplicação em execução


### 🌿 Versionamento

Sobre o versionamento e o uso do repositório no GitHub, cada desenvolvedor tinha criou uma branch própria para suas modificações e mantinha seus arquivos versionados com o Git. Commits e pushs também são de responsabilidade de cada desenvolvedor em suas respectivas branchs, exceto pelo merge e commit para a branch principal que era realizado pelo dev Vinicius Tabosa com auxílio da equipe, para resolução de possíveis conflitos de merge.

## 📦 MVP

### 🔨 Principais funcionalidades implementadas

- **Cadastro de usuário com gravação em banco de dados** - o formulário da tela de cadastro envia os dados ao servidor, que grava o usuário na tabela `usuario`
- **Escolha de perfil** entre Doador e Recebedor no momento do cadastro
- **Login com verificação de senha** - a senha digitada é conferida contra o hash guardado no banco
- **Proteção de senha por hash com salt** (PBKDF2-SHA256, 200.000 iterações) - a senha nunca é armazenada nem devolvida em texto puro
- **Validação de e-mail único** - garantida pelo próprio banco de dados, por meio da restrição `UNIQUE`
- **Validação de campos obrigatórios** - no navegador (atributo `required`) e no servidor (o FastAPI responde `422` quando falta um campo)
- **Tratamento de erros** - e-mail já cadastrado responde `400`, credenciais inválidas respondem `401`
- **Consulta dos usuários cadastrados** pela rota `/usuarios`, sem expor senhas
- **Documentação automática da API** disponível em `/docs`
- **Interface web responsiva** com 7 telas e navegação entre elas
- **Classes de domínio** representando cada componente do sistema

### 🔌 Rotas (endpoints) da aplicação

| Método | Endereço | O que faz | Respostas possíveis |
|---|---|---|---|
| `GET` | `/` | Entrega a página inicial | `200` |
| `GET` | `/paginas/<arquivo>.html` | Entrega as demais telas | `200`, `404` |
| `GET` | `/css/...` e `/imgs/...` | Entrega folhas de estilo e imagens | `200`, `404` |
| `POST` | `/cadastro` | Recebe o formulário de cadastro e grava o usuário | `303` redireciona ao perfil, `400` e-mail já cadastrado, `422` campo obrigatório ausente |
| `POST` | `/login` | Confere e-mail e senha | `303` redireciona à lista de pedidos, `401` credenciais inválidas, `422` campo ausente |
| `GET` | `/usuarios` | Lista os usuários cadastrados, sem as senhas | `200` |
| `GET` | `/status` | Informa se o servidor está no ar | `200` |
| `GET` | `/docs` | Documentação interativa gerada automaticamente | `200` |

O redirecionamento após um envio de formulário usa o código **303 See Other** de
propósito: ele faz o navegador buscar a página seguinte com `GET`, evitando que
atualizar a página reenvie o formulário e crie um cadastro duplicado.

### ⛵ Fluxo de navegação
```
├── Página inicial
|   ├── Login / Cadastro 
|   ├── Feed de pedidos 
|       ├── Detalhes do pedido 
|   ├── Criar novo pedido
|   ├── Meus pedidos
|   ├── Perfil
```

### 🖼️ Imagens do sistema
 - Tela inicial
![Tela inicial](/exemplo-uso/img1.png)

 - Tela de login
![Tela de login](/exemplo-uso/img2.png)

 - Tela de lista de pedidos
![Tela de lista de pedidos](/exemplo-uso/img3.png)

 - Tela de detalhes do pedido
![Tela de detalhes do pedido](/exemplo-uso/img4.png)

 - Tela de perfil do usuário
![Tela de perfil do usuário](/exemplo-uso/img5.png)



## 🤝 Como utilizar a aplicação

### Como qualquer pessoa pode acessar o sistema

A Escola Reusar é uma aplicação web: funciona no navegador, sem instalar nada no
celular ou no computador. Para executar o projeto localmente, basta seguir os passos da
seção Instalação e execução e abrir `http://127.0.0.1:8000`. Quando a aplicação estiver
publicada em um servidor, o acesso será apenas pelo endereço do site, o que também
permite o uso pelo celular.

### Como usar as principais funcionalidades

1. **Entrar na plataforma.** Ao abrir o site, a pessoa encontra a apresentação do
   projeto e o menu com as opções de Cadastro e Login.
2. **Criar uma conta.** Na tela de cadastro, informa nome, e-mail e senha e escolhe se
   quer participar como **Doador** (tem material para doar) ou **Recebedor** (precisa de
   material). Essa escolha define o que a pessoa vai fazer na plataforma.
3. **Entrar na conta.** Na tela de login, informa e-mail e senha. Se estiverem corretos,
   a pessoa é levada à área de pedidos.
4. **Publicar um pedido** (recebedor). Descreve o que precisa e quais materiais está
   procurando, e o pedido passa a aparecer no feed para os doadores.
5. **Encontrar quem ajudar** (doador). Consulta o feed de pedidos, abre o detalhe do
   pedido que fizer sentido e entra em contato para combinar a entrega.
6. **Acompanhar a própria atividade.** Na área de perfil e em "Meus pedidos", a pessoa
   consulta seus dados e os pedidos que criou.

### Qual problema a aplicação busca resolver

Todo fim de ano letivo, muita gente guarda ou descarta livros, cadernos com folhas em
branco, mochilas, estojos e material de desenho em bom estado, simplesmente porque não
sabe a quem entregar. No mesmo período, e muitas vezes na mesma cidade, existem
estudantes começando o ano sem material básico.

O problema não é falta de material nem falta de boa vontade: é **falta de encontro**.
Quem quer doar não sabe quem precisa, e quem precisa não tem como avisar que precisa.
Grupos de mensagem e redes sociais resolvem isso de forma desorganizada, em que o pedido
se perde no meio de outras conversas.

A Escola Reusar existe para organizar esse encontro em um lugar só: quem precisa
registra o pedido, quem quer doar consulta os pedidos e escolhe quem atender.

### Quem pode se beneficiar da solução

- **Estudantes e famílias em situação de vulnerabilidade**, que passam a ter um canal
  para pedir material escolar sem depender de conhecer alguém que possa ajudar.
- **Professores de reforço e educadores populares**, que costumam custear material do
  próprio bolso para manter suas aulas.
- **Projetos sociais, associações de bairro, bibliotecas comunitárias e ONGs**, que
  atendem muitas crianças e têm demanda constante de material.
- **Escolas públicas**, especialmente as de menor porte.
- **Doadores**, que ganham um destino confiável para o que sairia de casa como lixo, e
  passam a ver o resultado concreto da própria doação.
- **A comunidade e o meio ambiente**, pelo reaproveitamento de material que seria
  descartado.

### Exemplos de utilização em cenários reais

**Cenário 1 - o professor de reforço.** Um professor dá aula de reforço de matemática
para crianças do bairro e precisa de livros didáticos. Ele se cadastra como recebedor e
publica o pedido. No bairro vizinho, um jovem que acabou de terminar o ensino médio quer
liberar espaço em casa, entra na plataforma como doador, vê o pedido e combina a entrega.

**Cenário 2 - a volta às aulas.** Uma mãe percebe em janeiro que não vai conseguir
comprar a lista de material dos dois filhos. Ela se cadastra como recebedora e publica o
que falta. Uma papelaria da cidade, que tem itens de mostruário e sobras de estoque,
encontra o pedido e destina o material.

**Cenário 3 - o projeto social.** Uma associação de bairro que oferece aula de reforço
para trinta crianças precisa de cadernos e material de desenho. Publica o pedido, e
várias famílias da região contribuem com o que têm em casa, cada uma com uma parte.

**Cenário 4 - a mudança de casa.** Uma família que está se mudando encontra caixas de
material escolar dos filhos já formados. Em vez de descartar, se cadastra como doadora e
consulta os pedidos abertos na própria cidade.

### Reflexão sobre o impacto da solução

O impacto mais direto é econômico e imediato: material escolar pesa no orçamento de
famílias de baixa renda, e receber uma parte da lista pode ser a diferença entre a
criança começar o ano com o que precisa ou não. Mas existem dois efeitos menos óbvios,
que a equipe considera igualmente importantes.

O primeiro é **ambiental**. Material escolar em bom estado é descartado todos os anos por
falta de destino, e prolongar a vida útil desses itens reduz lixo e consumo. Reutilizar é
mais barato e mais sustentável do que produzir de novo.

O segundo é **social**. Ao aproximar doador e recebedor da mesma cidade ou de bairros
vizinhos, a plataforma cria uma relação de vizinhança em vez de uma doação anônima e
distante. A pessoa que doa sabe para onde o material foi, e quem recebe percebe que a
ajuda veio de perto. Isso fortalece o senso de comunidade, que é justamente o tipo de
vínculo que uma solução tecnológica costuma enfraquecer, e não fortalecer.

Vale registrar também um limite honesto: a plataforma organiza o encontro entre as
pessoas, mas não resolve a logística da entrega, que continua sendo combinada entre
doador e recebedor. Foi por isso que a equipe adotou o recorte local desde o início do
projeto, para que a entrega fosse viável sem custo de transporte.

## 💾 Projeto Físico de Banco de Dados

### 📌 O que é?
O projeto físico de banco de dados é a etapa na qual transformamos o modelo do sistema em estruturas reais dentro do banco. Em termos mais técnicos, é o processo de escolha de estruturas específicas e caminhos de acesso para os arquivos do banco de dados, visando um bom desempenho. Nessa etapa são definidos:
- 📊 Tabelas e colunas;
- 🔤 Tipos de dados;
- 🔑  Chaves primárias e estrangeiras;
- ⚡Índices e regras de integridade;
- 🗂️ Estratégias de organização dos dados.

### ⚙️Como isso funciona na prática?
As diferentes formas de organizar os dados, como indexação para acelerar consultas, organização de registros em arquivos e controle de integridade dos dados, são oferecidas pelos Sistemas Gerenciadores de Banco de Dados (SGBDs). Como exemplos destes sistemas, têm-se:
- 🪶 SQLite (o adotado neste projeto);
- 🐘 PostgreSQL;
- 🐬 MySQL;
- 🪟 SQL Server.

### 🚀 Por que isso é importante para quem está aprendendo programação?
O correto entendimento do projeto físico ajuda a criar sistemas mais organizados e confiáveis; evitar duplicidade ou inconsistência de dados; melhorar o desempenho das aplicações; desenvolver soluções mais próximas da realidade do mercado. Assim, entenda que a modelagem de dados define quais os dados existentes e o projeto físico define como esses dados são armazenados e acessados.

### 🎓 Exemplo prático - Escola Reusar
No projeto Escola Reusar, o projeto físico foi importante para fazer a transformação do modelo conceitual em tabelas reais. Por exemplo, a entidade usuário, virou a tabela usuário. Os perfis doador e recebedor foram implementados como especializações dessa tabela de usuário. E as chaves estrangeiras garantem que não exista doação ou pedido sem um usuário válido. Considerando tudo isso, evita-se inconsistência no sistema e ajuda a manter os dados organizados.

## 🏗️ Passo a Passo: Criação de Wireframes

Um wireframe é um esboço estrutural de baixa fidelidade, essencial no design de sites e aplicativos, que define o layout, a hierarquia de informações e a funcionalidade, sem focar em elementos estéticos como cores ou imagens. Abaixo está listado o passo a passo para prototipação de um wireframe

#### 🎯 1. Definir o Objetivo, escopo e hierarquia das páginas
- Listar as páginas: Identifica-se as páginas que estarão presentes na aplicação, para isso pode-se utilizar um sitemap, que elucida e hierarquiza as páginas.
- Identifique as metas: esse ponto tem o objetivo de identificar as ações que o usuário vai desenvolver em cada página identificada anteriormente. (Ex: Comprar, Cadastrar, Ler).
- Liste os elementos: lista os componentes que são obrigatórios. (Ex: Barra de busca, Botão de CTA, Rodapé).

#### ✍ ️ 2. Começar com Baixa Fidelidade
- Rabiscos rápidos: Desenhe versões diferentes do mesmo layout.
- Sem detalhes: Use quadrados para imagens e linhas para textos.
- Foco no fluxo: Pense em como os elementos se conectam visualmente.

#### 📐 3. Definir a Grade e a Estrutura (Grid)
- Sistema de Grids: Use colunas para alinhar os elementos.
- Zonas de Conteúdo: Bloqueie áreas grandes para cabeçalho, corpo e barra lateral.

#### 🔝 4. Estabelecer a Hierarquia Visual
- Tamanho importa: O elemento principal (ex: Título H1) deve ser o maior.
- Contraste de cinzas: Use tons de cinza mais escuros para elementos de destaque e cinza claro para o que é secundário.

#### 🔄 5. Revisar e Iterar
- Teste de usabilidade: Mostre os desenhos para outras pessoas, observe as opiniões e se a usabilidade está adequada.
- Ajustes finos: Refine os espaçamentos (padding/margin) antes de passar para a fase de UI (Cores e Fontes).

#### 💡 Design Centrado no Usuário:

O design centrado no usuário assegura que a tomada de decisões seja fundamentada nas necessidades e comportamentos do público-alvo. Essa filosofia garante que o desenvolvimento de interfaces não foque apenas na estética, mas que o projeto seja, acima de tudo, útil, utilizável e desejável. Dentro dessa tríade, a usabilidade destaca-se como o pilar fundamental: um sistema eficiente possui uma interface intuitiva, visualmente encorajadora e com baixa curva de aprendizado. Essa característica está intimamente ligada ao perfil do usuário, uma vez que o fator geracional influencia diretamente o design; enquanto pessoas da terceira idade podem demandar mais tutoriais e auxílio na navegação, as novas gerações podem sentir desânimo diante desse excesso de instruções. Quanto à utilidade, ela se manifesta plenamente quando o sistema é modelado com base nas dores reais do usuário, tornando-se uma ferramenta personalizada e funcional. Ao atender a esses requisitos de utilidade e usabilidade, o terceiro pilar — o desejo — é alcançado naturalmente, pois a vontade de utilização por parte do usuário é o resultado direto da excelente experiência obtida durante a interação com o sistema.

## ⭐ Importância da Experiência do Usuário (UX)
A Experiência do Usuário (UX) é fundamental para garantir que um sistema seja fácil, intuitivo e agradável de utilizar. Não se devendo se limitar à estética, o design centrado no usuário contribui diretamente para tornar a tecnologia mais inclusiva, permitindo que pessoas com diferentes níveis de conhecimento digital naveguem pela plataforma sem dificuldades. Interfaces bem planejadas reduzem erros, ajudando empresas e projetos sociais a alcançarem maior aceitação do público e, consequentemente, aumentando o impacto positivo da solução no mundo real.

No caso da plataforma da Escola Reusar, uma boa experiência do usuário é indispensável para facilitar ações essenciais, como o cadastro de doações, a busca por materiais e a comunicação direta entre os usuários. Por essa razão, todas as decisões de design foram focadas em simplicidade, acessibilidade e facilidade de navegação, garantindo que múltiplos perfis públicos consigam interagir com o sistema de forma autônoma.

Para viabilizar e validar essas decisões antes do desenvolvimento final, a equipe optou por criar um MVP (Produto Mínimo Viável) focado na experiência interativa. Essa estratégia permitiu manter a plataforma organizada, objetiva e eficiente, concentrando-se apenas nas funcionalidades essenciais do sistema, tais como o cadastro de usuários, a criação de pedidos de doação e a visualização de itens para doação. Ao aplicar princípios de organização visual padronizada e fluxos simples de navegação, o design destaca o que é principal, tornando a experiência mais fluida e incentivando a adoção do sistema na prática.

A ferramenta empregada foi o Figma, utilizada na criação das interfaces, no mapeamento de fluxos e no desenvolvimento do protótipo interativo de alta fidelidade. Como o projeto encontra-se atualmente nesta etapa de validação, a utilização e os testes da aplicação ocorrem de forma interativa diretamente na ferramenta. Para navegar pelo sistema e simular a experiência real da plataforma, o usuário deve acessar o link do projeto no Figma [Escola Reusar](https://www.figma.com/design/chwkya39dL4TxGpgHQ3Keo/ESCOLA-REUSAR?node-id=12-2&t=tQ774DTxH2ULADrX-1), clicar no botão de Play (Present / Apresentar) localizado no canto superior direito da tela e interagir diretamente com os botões das telas. Dessa forma, a Escola Reusar demonstra que investir em UX significa criar experiências mais humanas, eficientes e verdadeiramente acessíveis para todos.

## 📐 Arquitetura de Software

### O que é arquitetura de software?
Para os desenvolvedores do projeto “Escola Reusar”, a definição de arquitetura de software não se restringe a escolha de linguagens ou frameworks de programação. Compreende-se que essa arquitetura é um conjunto de decisões estratégicas de alto nível que definem a estrutura, o comportamento e as interações entre os componentes de um sistema computacional. Fazendo uma analogia com a construção civil, enquanto o código limpo representa os tijolos bem assentados, a arquitetura de software consiste na planta estrutural do edifício, ou seja, é ela quem garante que a edificação não caia quando novas cargas forem adicionadas e que os demais sistemas (elétricos e hidráulicos) funcionem corretamente.

### Qual sua importância no desenvolvimento de sistemas?
A arquitetura de software em um projeto, consegue se traduzir diretamente em valor de negócio, por envolver decisões estratégicas críticas para o ciclo de desenvolvimento do software. Não seguir uma arquitetura no início do desenvolvimento pode condenar toda a vida do software e os esforços para consertar os erros do passado podem sair muito caros.

### Como ela impacta:
- Escalabilidade:
  
  Permite que o sistema consiga crescer e suportar um aumento expressivo na carga de trabalho (como um pico de acessos de doadores e recebedores no início do ano letivo) sem perder qualidade. Uma boa arquitetura, como o modelo Cliente-Servidor adotado, permite que o sistema seja escalado com facilidade, seja adicionando mais recursos ao servidor ou distribuindo as requisições de forma equilibrada. 
  
- Segurança:
  
  A estruturação em camadas permite a criação de barreiras de proteção bem definidas e isoladas. Ao utilizar o modelo MVC, garantimos, por exemplo, que o banco de dados (Model) não fique exposto diretamente à internet. Toda e qualquer requisição externa passa obrigatoriamente pela validação de regras de negócio e autenticação do Backend (Controller) antes de acessar dados sensíveis. 
  
- Desempenho:
  
  A arquitetura dita a eficiência de como os dados trafegam e como os recursos da máquina são consumidos. Decisões arquiteturais sólidas — como o uso do FastAPI, que processa requisições de forma assíncrona e leve, somado à correta modelagem e indexação das tabelas no banco de dados — garantem respostas rápidas e uma experiência fluida para os usuários, mesmo em conexões de internet mais lentas. 
  
- Manutenção e Evolução do sistema:
  
  Trata-se da capacidade do sistema de receber correções e adaptar-se a novas necessidades ao longo do tempo sem perder sua estabilidade. Ao adotar uma arquitetura que isola as responsabilidades através do modelo MVC (onde a interface gráfica não se mistura com as regras de negócio ou com o banco de dados), garantimos um baixo nível de acoplamento estrutural. Na prática, isso permite que a equipe isole e corrija falhas rapidamente sem causar efeitos colaterais na aplicação, ao mesmo tempo em que prepara o sistema para receber novas funcionalidades no futuro — como novas integrações ou perfis de usuários — de maneira orgânica, segura e sem a necessidade de reescrever o código já consolidado.


### Como a arquitetura influencia diretamente a qualidade de um projeto de software?
  A arquitetura de software assegura que fatores como escalabilidade, segurança, desempenho, manutenção e evolução do sistema atendam aos requisitos apontados pelo cliente, evite retrabalho da equipe de desenvolvimento, aumenta a longevidade do software e que seja capaz de se adaptar a requisitos em constante mudança. 


## 👥 Equipe — PISociety

- Pablo Henrique ([@phpablo](https://github.com/phpablo))
- Sarah Oliveira ([@Sarah-Oliver-SOL](https://github.com/Sarah-Oliver-SOL))
- Saulo Victo ([@Saulo-victo](https://github.com/Saulo-victo))
- Vinicius Tabosa ([@ViniciusTabosa](https://github.com/ViniciusTabosa))