# Author: Diogo Gonçalves Bonofre dos Santos

from typing import List

class Funcionario():
        def __init__(self, nome, cpf, salario, departamento) -> None:
                self.nome = nome
                self.cpf = cpf
                self.salario = salario
                self.departamento = departamento
        
        def bonificar(self) -> None:
                self.salario *= 1.10

class Gerente(Funcionario):
        def __init__(self, nome, cpf, salario, departamento, senha, funcionarios) -> None:
                super().__init__(nome, cpf, salario, departamento)
                self.senha = senha
                self.funcionarios = funcionarios

        def autenticarSenha(self, senha) -> bool:
                return self.senha == senha
        
        def bonificar(self) -> None:
                self.salario *= 1.15

class Vendedor(Funcionario):
        def __init__(self, nome, cpf, salario, departamento, vendas, comissao) -> None:
                super().__init__(nome, cpf, salario, departamento)
                self.vendas = vendas
                self.comissao = comissao

        def atualizaQuantidadeVendas(self, vendas) -> None:
                self.vendas = vendas

        def calculaSalario(self) -> float:
                return self.salario + self.comissao

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def header(title: str) -> None:
        print(colors.HEADER + title.center(width(), ':') + colors.ENDC)

def notification(message: str) -> None:
        print(colors.OKGREEN + message.center(width(), '-') + colors.ENDC)

def warning(error: str) -> None:
        print(colors.FAIL + error.center(width(), ':') + colors.ENDC)

def width() -> int: 
        return 60

funcionarios: List[Funcionario] = []
gerentes: List[Gerente] = []  
vendedores: List[Vendedor] = []

def listar_funcionarios(filtro: list) -> None:
        id = 0
        print("ID".ljust(3, ' '),
              "NOME".ljust(20, ' '),
              "CPF".ljust(15, ' '),
              "SALÁRIO".ljust(10, ' '),
              "DEPARTAMENTO".ljust(20, ' '), end='')
        if (filtro == gerentes):
                print("FUNCIONÁRIOS".ljust(12, ' '), end='')
        if (filtro == vendedores):
                print("VENDAS".ljust(10, ' '),
                      "COMISSÃO".ljust(10, ' '), end='')
        print()
        for obj in filtro:
                print(str(id).ljust(3, ' '),
                      str(obj.nome).ljust(20, ' '), 
                      str(obj.cpf).ljust(15, ' '), 
                      f"{obj.salario:.2f}".ljust(10, ' '), 
                      str(obj.departamento).ljust(20, ' '), end='')
                if (filtro == gerentes):
                        print(str(obj.funcionarios).ljust(12, ' '), end='')
                if (filtro == vendedores):
                        print(str(obj.vendas).ljust(10, ' '),
                              str(obj.comissao).ljust(10, ' '), end='')
                print()
                id += 1

while (True):
        header("MENU")
        print('''
1. Cadastrar (Funcionário)
2. Cadastrar (Gerente)
3. Cadastrar (Vendedor)
4. Bonificar (Funcionário)
5. Bonificar (Gerente)
6. Autenticar senha (Gerente)
7. Atualizar quantidade de vendas (Vendedor)
8. Calcular salário (Vendedor)
9. Listar (Funcionários)
10. Listar (Gerentes)
11. Listar (Vendedores)
''')
        while (True):
                try:
                        opt = int(input("Insira um número: "))
                        break
                except ValueError:
                        warning("ERRO: Você não digitou um caractere válido para essa operação.")        
        match opt:
                case 1:
                        header("CADASTRO DE FUNCIONÁRIO")
                        f = Funcionario(
                                str(input("Nome: ")),
                                str(input("CPF: ")),
                                float(input("Salário: ")),
                                str(input("Departamento: "))
                        )
                        funcionarios.append(f)
                        notification("FUNCIONÁRIO ADICIONADO")
                        input()
                case 2:
                        header("CADASTRO DE GERENTE")
                        g = Gerente(
                                str(input("Nome: ")),
                                str(input("CPF: ")),
                                float(input("Salário: ")),
                                str(input("Departamento: ")),
                                str(input("Senha: ")),
                                int(input("Funcionários: "))
                        )
                        gerentes.append(g)
                        notification("GERENTE ADICIONADO")
                        input()
                case 3:
                        header("CADASTRO DE VENDEDOR")
                        v = Vendedor(
                                str(input("Nome: ")),
                                str(input("CPF: ")),
                                float(input("Salário: ")),
                                str(input("Departamento: ")),
                                int(input("Vendas: ")),
                                float(input("Comissão: "))
                        )
                        vendedores.append(v)
                        notification("VENDEDOR ADICIONADO")
                        input()
                case 4:
                        header("BONIFICAR FUNCIONÁRIO")
                        listar_funcionarios(funcionarios)
                        id = int(input("Insira o ID do funcionário: "))
                        funcionarios[id].bonificar()
                        notification("FUNCIONÁRIO BONIFICADO")
                        input()
                case 5:
                        header("BONIFICAR GERENTE")
                        listar_funcionarios(gerentes)
                        id = int(input("Insira o ID do gerente: "))
                        gerentes[id].bonificar()
                        notification("GERENTE BONIFICADO")
                        input()
                case 6:
                        header("AUTENTICAÇÃO DE GERENTE")
                        listar_funcionarios(gerentes)
                        id = int(input("Insira o ID do gerente: "))
                        while (True):
                                senha = str(input("Insira a senha: "))
                                if (senha == gerentes[id].senha):
                                        notification("GERENTE AUTENTICADO")
                                        break
                                else:
                                        warning("SENHA INCORRETA")
                                if (str(input("Tentar novamente (y/n)? ")).lower() == 'n'):
                                        break
                        input()
                case 7:
                        header("ATUALIZAR VENDAS")
                        listar_funcionarios(vendedores)
                        id = int(input("Insira o ID do vendedor: "))
                        vendas = int(input("Insira a nova quantidade de vendas: "))
                        vendedores[id].atualizaQuantidadeVendas(vendas)
                        notification("QUANTIDADE DE VENDAS ATUALIZADA")
                        input()
                case 8:
                        header("CALCULAR SALÁRIO DE VENDEDOR")
                        listar_funcionarios(vendedores)
                        id = int(input("Insira o ID do vendedor: "))
                        print(f"Salário: {vendedores[id].calculaSalario():.2f}")
                        input()
                case 9:
                        header("LISTA DE FUNCIONÁRIOS")
                        listar_funcionarios(funcionarios)
                        input()
                case 10:
                        header("LISTA DE GERENTES")
                        listar_funcionarios(gerentes)
                        input()
                case 11:
                        header("LISTA DE VENDEDORES")
                        listar_funcionarios(vendedores)
                        input()
                case _:
                        warning("ERRO: O caractere digitado não corresponde à nenhuma das opções.")
                        input()
