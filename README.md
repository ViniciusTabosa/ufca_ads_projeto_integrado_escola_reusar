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

### 📌 O que é?
O projeto físico de banco de dados é a etapa na qual transformamos o modelo do sistema em estruturas reais dentro do banco. Em termos mais técnicos, é o processo de escolha de estruturas específicas e caminhos de acesso para os arquivos do banco de dados, visando um bom desempenho. Nessa etapa são definidos:
- 📊 Tabelas e colunas;
- 🔤 Tipos de dados;
- 🔑  Chaves primárias e estrangeiras;
- ⚡Índices e regras de integridade;
- 🗂️ Estratégias de organização dos dados.

### ⚙️Como isso funciona na prática?
As diferentes formas de organizar os dados, como indexação para acelerar consultas, organização de registros em arquivos e controle de integridade dos dados, são oferecidas pelos Sistemas Gerenciadores de Banco de Dados (SGBDs). Como exemplos destes sistemas, têm-se:
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
  
  A arquitetura dita a eficiência de como os dados trafegam e como os recursos da máquina são consumidos. Decisões arquiteturais sólidas — como o uso do Node.js para processamento assíncrono e leve, somado à correta modelagem e indexação de tabelas no PostgreSQL — garantem respostas rápidas e uma experiência fluida para os usuários, mesmo em conexões de internet mais lentas. 
  
- Manutenção e Evolução do sistema:
  
  Trata-se da capacidade do sistema de receber correções e adaptar-se a novas necessidades ao longo do tempo sem perder sua estabilidade. Ao adotar uma arquitetura que isola as responsabilidades através do modelo MVC (onde a interface gráfica não se mistura com as regras de negócio ou com o banco de dados), garantimos um baixo nível de acoplamento estrutural. Na prática, isso permite que a equipe isole e corrija falhas rapidamente sem causar efeitos colaterais na aplicação, ao mesmo tempo em que prepara o sistema para receber novas funcionalidades no futuro — como novas integrações ou perfis de usuários — de maneira orgânica, segura e sem a necessidade de reescrever o código já consolidado.


### Como a arquitetura influencia diretamente a qualidade de um projeto de software?
  A arquitetura de software assegura que fatores como escalabilidade, segurança, desempenho, manutenção e evolução do sistema atendam aos requisitos apontados pelo cliente, evite retrabalho da equipe de desenvolvimento, aumenta a longevidade do software e que seja capaz de se adaptar a requisitos em constante mudança. 
