# Geo-Explorer

## 1. O que é o Geo-Explorer

Geo-Explorer é uma ferramenta de linha de comando (CLI) em Python para exploração de trilhas de aprendizado em tecnologia. A aplicação permite consultar planos de estudo, gerar desafios de código e emitir certificados fictícios de conclusão, tudo a partir de um dataset local em JSON.

---

## 2. Como executar o projeto

**Pré-requisitos:** Python 3.8 ou superior.

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd IBM_BOB_Projeto_final

# Execute a aplicação
python app.py --help
```

Nenhuma dependência externa é necessária — a aplicação utiliza apenas a biblioteca padrão do Python.

---

## 3. Como usar os comandos

### `trilha`

Exibe o plano de estudos (módulos e nível) de uma tecnologia disponível no dataset.

```bash
python app.py trilha <tecnologia>
```

**Exemplo:**
```bash
python app.py trilha Python
# Trilha: Python — Nível: Iniciante
# Módulos:
#   1. Introdução ao Python
#   2. Estruturas de Dados
#   3. Funções e Módulos
```

---

### `desafio`

Gera um desafio de código fictício formatado em ASCII para a tecnologia e nível informados.

```bash
python app.py desafio <tecnologia> <nivel>
```

**Exemplo:**
```bash
python app.py desafio Python Iniciante
```

---

### `certificado`

Emite um certificado fictício de conclusão para o nome e tecnologia informados.

```bash
python app.py certificado "<nome>" <tecnologia>
```

**Exemplo:**
```bash
python app.py certificado "Ada Lovelace" Python
```

---

## 4. Como executar os testes

Os testes utilizam o módulo `unittest` da biblioteca padrão do Python.

```bash
python -m unittest discover -s tests -v
```

Os testes verificam:
- Se o arquivo `data/trilhas.json` carrega corretamente e possui a chave `trilhas`.
- Se a tecnologia `Python` está presente no dataset.

---

## 5. Melhorias realizadas

- **Estrutura modular:** funções separadas por responsabilidade (`carregar_trilhas`, `listar_trilha`, `gerar_desafio`, `gerar_certificado`), facilitando manutenção e extensão.
- **CLI com subcomandos:** uso de `argparse` com `subparsers`, tornando a interface clara e auto-documentada via `--help`.
- **Dataset desacoplado:** dados armazenados em `data/trilhas.json`, separados da lógica da aplicação, permitindo adicionar novas trilhas sem alterar código.
- **Testes automatizados:** cobertura da camada de dados com `unittest`, garantindo integridade do JSON a cada execução.
- **Compatibilidade:** sem dependências externas, rodando com Python puro em qualquer ambiente.

---

## 6. O que foi aprendido durante o desafio

Durante o desenvolvimento deste projeto com suporte do **IBM Bob**, foram consolidados os seguintes aprendizados:

- **Economia de tokens:** ao formular prompts objetivos e bem delimitados, é possível obter respostas precisas sem iterações desnecessárias, reduzindo significativamente o consumo de tokens. Prompts com contexto cirúrgico — escopo claro, exemplos concretos e restrições explícitas — geram saídas mais úteis na primeira tentativa.
- **Engenharia de prompts com IBM Bob:** aprendemos a estruturar instruções em camadas (o que fazer, como fazer, o que não fazer), aproveitar o contexto acumulado da conversa para evitar repetições, e usar comandos de modo (agente, plano, ask) de acordo com a natureza da tarefa.
- **Fluxo assistido por IA:** o uso do IBM Bob acelerou decisões de arquitetura, geração de testes e documentação, demonstrando como um assistente de IA integrado ao ambiente de desenvolvimento agrega produtividade real em projetos de software.
