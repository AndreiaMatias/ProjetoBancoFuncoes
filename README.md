#Projeto Banco - Funções

Evolução do projeto anterior com a inclusão de métodos para as funcionalidades já existentes e novas funcionalidades:

 - A função saque deve receber os argumentos apenas por nome. 
   - sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
   - retorno: saldo, extrato.
 - A função depósito deve receber os argumentos por posição.
   - sugestão de argumentos: saldo, valor, extrato.
   - retorno: saldo e extrato.
 - A função extrato deve receber os argumentos por posição e por nome.
   - argumentos posicionais: saldo
   - argumentos nomeados: extrato.

##Novas funções

- criar usuário:
  - usuários devem ser armazenados em uma lista;
  - usuário é composto de nome, data de nascimento, cpf e endereço (logradouro, nº - bairro -cidade/sigla do estado);
  - devem ser armazenados apenas os número do CPF;
  - o CPF é único.
- criar conta corrente:
  - armazena contas em uma lista;
  - uma conta é composta de agência, número e usuário;
  - o número da conta é sequencial iniciando-se em 1;
  - o número da agência é fixo "0001";
  - o usuário pode ter mais de uma conta, mas uma conta tem apenas um usuário.
