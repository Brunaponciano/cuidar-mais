# Testes realizados no CUIDAR+

## Sobre os testes

Durante o desenvolvimento do CUIDAR+, realizei alguns testes para verificar se as funcionalidades estavam funcionando corretamente. Também testei situações em que o usuário poderia digitar informações erradas, para verificar se o programa mostrava mensagens de erro e impedia o cadastro quando necessário.

Os testes foram feitos manualmente, executando o programa no Python pelo VS Code.

## 1. Testes de cadastro de medicamentos

Testei o cadastro de medicamentos para verificar se o programa estava aceitando os dados corretamente.

- Testei deixar campos obrigatórios vazios e o programa impediu o cadastro.
- Digitei letras no campo de intervalo entre doses e o programa mostrou uma mensagem de erro.
- Digitei zero no intervalo entre as doses e o programa não permitiu continuar.
- Digitei um horário inválido, como `25:90`, e o programa identificou o erro.
- Digitei uma data inválida e o programa impediu o cadastro.
- Coloquei a data de término anterior à data de início e o programa mostrou uma mensagem de erro.

**Resultado:** os testes realizados passaram e as validações funcionaram como esperado.

## 2. Testes de edição de medicamentos

Também testei a edição dos medicamentos já cadastrados.

- Fiz uma edição com dados válidos e o programa salvou as alterações.
- Tentei colocar zero no intervalo entre as doses e o programa não permitiu salvar.
- Digitei um horário inválido e o programa mostrou uma mensagem de erro.
- Coloquei uma data de término anterior à data de início e o programa impediu a edição.
- Depois de editar um medicamento, fechei e abri o programa novamente para verificar se as alterações continuavam salvas.

**Resultado:** os testes realizados passaram. As alterações válidas foram salvas e os dados inválidos foram rejeitados.

## 3. Testes de cadastro de consultas

Realizei testes no cadastro de consultas para verificar se os campos obrigatórios e as datas e horários estavam sendo validados.

- Tentei cadastrar uma consulta deixando um campo obrigatório vazio e o programa impediu o cadastro.
- Digitei uma data inválida e o programa mostrou uma mensagem de erro.
- Digitei um horário inválido, como `25:90`, e o programa não permitiu cadastrar a consulta.
- Cadastrei uma consulta com dados válidos e depois reiniciei o programa para verificar se ela continuava salva.

**Resultado:** os testes realizados passaram e a consulta cadastrada continuou disponível depois que o programa foi reiniciado.

## 4. Testes do histórico de doses

Testei o registro e a consulta do histórico de doses dos medicamentos.

- Registrei uma dose tomada e verifiquei se o programa mostrava a data e o horário do registro.
- Consultei o histórico para verificar se a dose aparecia corretamente.
- Fechei e abri o programa novamente para conferir se o histórico continuava salvo.

**Resultado:** o histórico de doses permaneceu salvo depois que o programa foi reiniciado.

## 5. Testes de exclusão de medicamentos

Também verifiquei se a exclusão de medicamentos estava funcionando corretamente.

- Excluí um medicamento de teste e reiniciei o programa para conferir se ele continuava excluído.
- Tentei excluir um medicamento, mas cancelei a operação. Depois, verifiquei se ele continuava cadastrado.

**Resultado:** a exclusão foi mantida depois que o programa foi reiniciado, e o medicamento permaneceu cadastrado quando cancelei a operação.

## 6. Testes de salvamento dos dados

Como o CUIDAR+ utiliza arquivos JSON para guardar as informações, também verifiquei se os dados continuavam disponíveis depois de fechar e abrir o programa.

Testei o salvamento de:
- Medicamentos cadastrados e editados.
- Consultas cadastradas.
- Histórico de doses.
- Exclusão de medicamentos.

**Resultado:** nos testes realizados, os dados foram mantidos corretamente depois que o programa foi reiniciado.

## Considerações finais

Os testes me ajudaram a encontrar erros, corrigir partes do código e entender melhor como funcionam as validações e o salvamento de dados em Python.

O CUIDAR+ ainda está em desenvolvimento e sei que existem melhorias que podem ser feitas futuramente. Pretendo continuar aprendendo e aprimorando o projeto conforme avançar nos estudos de Análise e Desenvolvimento de Sistemas.