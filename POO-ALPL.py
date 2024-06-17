medicos = [{"mednome": "André", "medcpf": "772928", "medrg": "287263", "medcrm": "88888", "medtelefone": "(55)98990", "medendereco": "Granjeiro", "medsexo": "Masculino", "senha": "Larissandp98"}]
pacientes = [{"pacnome": "Pedro Leo ", "paccpf": "999999", "pacrg": "000009", "pactelefone": "(88)7778", "pacendereco": "Varzea Alegre", "pacsexo": "Masculino", "convenio": "Amil"}]
convenios = [{"convnome": "Amil", "convtelefone": "(66)9890", "convendereco": "Barbalha", "convcnpj": "38888889", "planos": "Plano XTR, Plano SESC"}]
consultas = [{"mednome": "André ", "pacnome":"Pedro Leo", "data" : "25/09/2024", "horainicial" : "17:00", "horafinal" : "18:00", "descricao" : "Atendimento psiquiatrico"}]
compromissos = [{"data": "25/09/2024", "hora inicial": "10:00", "hora final": "11:00", "descricao": "Pescar"}]

def cadastrarMedicos():
        print("Iniciar cadastro do médico.")
        print("Insira o nome do médico: ")
        mednome = input("")
       
        print("Insira o CPF do médico: ")
        medcpf = input("")
        
        print("Insira o RG do médico: ")
        medrg = input("")

        print("Insira o telefone do médico:")
        medtelefone = input("")
        
        print("Insira o endereço do médico :")
        medendereco = input("")

        print("Insira o sexo do médico: ")
        medsexo = input("")
        
        print("Insira o CRM do médico: ")
        medcrm = input("")
        
        print("Insira uma senha para o médico:")
        senha = input("")
        
        print("Deseja salvar as informações? (S/N)")
        salvar = input("").upper()
        if salvar == "S":
            print("Médico cadastrado com sucesso!")
            medicos.append({
                "mednome": mednome,
                "medcpf": medcpf,
                "medrg": medrg,
                "medtelefone": medtelefone,
                "medendereco": medendereco,
                "medsexo": medsexo,
                "medcrm": medcrm,
                "senha": senha
            })
            print(medicos)
        else:
            print("Operação cancelada!")
            
def buscarMedicos():
    print("Informe o nome ou CRM do médico que deseja buscar:")
    busm = input("")
    resultados = [medico for medico in medicos if busm.lower() == medico.get('mednome', '').lower() or busm == medico.get('medcrm', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['mednome']}, Telefone: {resultado['medtelefone']}, CRM: {resultado['medcrm']}")
    else:
        print("Nenhum médico encontrado.")
        
def alterarMedicos():
  
  print("Informe o CRM do médico que deseja alterar:")
  medcrm = input("")
  medico = next((medico for medico in medicos if medico['medcrm'] == medcrm), None)
  if medico:
        print(f"Analise as informações cadastradas do médico: {medico}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        mednome = input(f"Nome ({medico['mednome']}): ") or medico['mednome']
        medcpf = input(f"CPF ({medico['medcpf']}): ") or medico['medcpf']
        medrg = input(f"RG ({medico['medrg']}): ") or medico['medrg']
        medtelefone = input(f"Telefone ({medico['medtelefone']}): ") or medico['medtelefone']
        medendereco = input(f"Endereço ({medico['medendereco']}): ") or medico['medendereco']
        medsexo = input(f"Sexo ({medico['medsexo']}): ") or medico['medsexo']
        senha = input(f"Senha ({medico['senha']}): ") or medico['senha']
        
        print("Deseja salvar as informações? (S/N)")
        salvar = input("").upper()
        if salvar == "S":
            print("As informações do médico foram alteradas com sucesso!")
            
        medico.update({
            "mednome": mednome,
            "medcpf": medcpf,
            "medrg": medrg,
            "medtelefone": medtelefone,
            "medendereco": medendereco,
            "medsexo": medsexo,
            "senha": senha
        })
        print(medicos)

def cadastrarPacientes():

    print("Insira o nome do paciente:")
    pacnome = input()
    
    print("Insira o CPF do paciente:")
    paccpf = input()
    
    print("Insira o RG do paciente:")
    pacrg = input()
    
    print("Insira o telefone do paciente: ")
    pactelefone = input()

    print("Insira o endereço do paciente: ")
    pacendereco = input()
    
    print("Insira o sexo do paciente: ")
    pacsexo = input()

    print("Insira o convenio do paciente: ")
    convenio = input()

    print("Deseja salvar as informações? (S/N)")
    salvar = input().upper()
    if salvar == "S":
        print("Paciente cadastrado com sucesso!")
        pacientes.append({
            "pacnome": pacnome,
            "paccpf": paccpf,
            "pacrg": pacrg,
            "pactelefone": pactelefone,
            "pacendereco": pacendereco,
            "pacsexo": pacsexo,
            "convenio": convenio
        })
        print(pacientes)
    else:
        print("Operação cancelada!")
        
def buscarPacientes():
    print("Informe o nome ou CPF do paciente que deseja buscar:")
    busp = input("")
    resultados = [paciente for paciente in pacientes if busp.lower() == paciente.get('pacnome', '').lower() or busp == paciente.get('paccpf', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['pacnome']}, Telefone: {resultado['pactelefone']}, CPF: {resultado['paccpf']}")
    else:
        print("Nenhum paciente encontrado.")
        
        
def alterarPacientes():

    print("Insira o CPF do paciente que deseja alterar:")
    paccpf = input("")
    paciente = next((paciente for paciente in pacientes if paciente['paccpf'] == paccpf), None)
    if paciente:
        print(f"Dados atuais: {paciente}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        pacnome = input(f"Nome ({paciente['pacnome']}): ") or paciente['pacnome']
        pacrg = input(f"RG ({paciente['pacrg']}): ") or paciente['pacrg']
        pactelefone = input(f"Telefone ({paciente['pactelefone']}): ") or paciente['pactelefone']
        pacendereco = input(f"Endereço ({paciente['pacendereco']}): ") or paciente['pacendereco']
        pacsexo = input(f"Sexo ({paciente['pacsexo']}): ") or paciente['pacsexo']
        convenio = input(f"Convênio ({paciente['convenio']}): ") or paciente['convenio']
        
        print("Deseja salvar as informações? (S/N)")
        salvar = input("").upper()
        if salvar == "S":
            print("As informações do paciente foram alteradas com sucesso!")
        paciente.update({
            "pacnome": pacnome,
            "pacrg": pacrg,
            "pactelefone": pactelefone,
            "pacendereco": pacendereco,
            "pacsexo": pacsexo,
            "convenio": convenio
        })
        
    else:
        print("Paciente não encontrado.")
        
        
def cadastrarConvenios():
        print("Insira o nome do convênio:")
        convnome = input("")
        
        print("Insira o telefone do convênio:")
        convtelefone = input("")
        
        print("Insira o endereço do convênio:")
        convendereco = input("")
        
        print("Insira o CNPJ do convênio:")
        convcnpj = input("")

        print("Insira os planos do convênio:")
        planos = input("")
        
        print("Deseja salvar as informações? (S/N)")
        salvar = input("").upper()
        if salvar == "S":
            print("Convênio cadastrado com sucesso!")
            convenios.append({
                "convnome": convnome,
                "convendereco": convendereco,
                "convtelefone": convtelefone,
                "convcnpj": convcnpj,
                "planos": planos
            })
            print(convenios)
        else:
            print("Operação cancelada!")

def buscarConvenios():
    print("Insira o nome ou CNPJ do convênio que deseja buscar:")
    busc = input("")
    resultados = [convenio for convenio in convenios if busc.lower() == convenio.get('convnome', '').lower() or busc == convenio.get('convcnpj', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['convnome']}, Telefone: {resultado['convtelefone']}, CNPJ: {resultado['convcnpj']}")
    else:
        print("Nenhum convênio encontrado.")

    
def marcarCompromisso():
        mednome = input("Insira o nome do médico: ")
        medicoencontrado = next((medico for medico in medicos if medico['mednome'] == mednome), None)
        if medicoencontrado:
         data = input("Insira a data do compromisso: ")
         horainicial = input("Insira a hora inicial do compromisso: ")
         horafinal = input("Insira a hora final do compromisso: ")
         descricao = input("Descreva o seu compromisso: ")
        
        print("Deseja salvar as informações? (S/N)")
        salvar = input("").upper()
        if salvar == "S":
            print("Compromisso agendado com sucesso!")
        compromissos.append({
            "data": data,
            "hora inicial": horainicial,
            "hora final": horafinal,
            "descrição": descricao
        })
        print(f"Analise as informações do seu compromisso agendado: {compromissos[-1]}")

def marcarConsulta():
        mednome = input("Insira o nome do médico: ")
        medicoencontrado = next((medico for medico in medicos if medico['mednome'] == mednome), None)
        if medicoencontrado:
            pacnome = input("Informe o nome do paciente: ")
            pacienteencontrado = next((paciente for paciente in pacientes if paciente['pacnome'] == pacnome), None)
            if pacienteencontrado:
                data = input("Insira a data da consulta: ")
                horainicial = input("Insira a hora inicial da consulta: ")
                horafinal = input("Insira a hora final da consulta: ")
                descricao = input("Descreva a consulta: ")
                
                print("Deseja salvar as informações? (S/N)")
                salvar = input("").upper()
                if salvar == "S":
                   print("Convênio cadastrado com sucesso!")
                consultas.append({
                    "data": data,
                    "horainicial": horainicial,
                    "horafinal": horafinal,
                    "mednome": mednome,
                    "mednome": mednome,
                    "descricao": descricao
                })

                print(f"Analise as informações da consulta agendada: {consultas[-1]}")
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")

def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome do médico: {medico['mednome']}, CPF do médico: {medico['medcpf']}, CRM do médico: {medico['medcrm']}, Telefone do médico: {medico['medtelefone']}")
            
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"Nome do paciente: {paciente['pacnome']}, CPF do paciente: {paciente['paccpf']}, Telefone do paciente: {paciente['pactelefone']}")
            
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome do convênio: {convenio['convnome']}, CNPJ do convênio: {convenio['convcnpj']}, Telefone do convênio: {convenio['convtelefone']}")
            
    elif escolha == "4":
        print("Consultas:")
        for consulta in consultas:
            print(f"Nome do paciente: {consulta['pacnome']}, Nome do médico: {consulta['mednome']}, Data da consulta: {consulta['data']},  Hora inicial da consulta: {consulta['horainicial']},  Hora final da consulta: {consulta['horafinal']},  Descrição da consulta: {consulta['descricao']}")
            
        
a = True
while a:
   
   lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?")
   match lang:
       
    case "1":
        cadastrarMedicos()
        
    case "2":
        cadastrarPacientes()

    case "3": 
        cadastrarConvenios()
        
    case "4":
        buscarMedicos()
        
    case "5":
        buscarPacientes()
        
    case "6":
        buscarConvenios()
      
    case "7":
        alterarMedicos()
        
    case "8":
        alterarPacientes()
        
    case "9":
        marcarCompromisso()
        
    case "10":
        marcarConsulta()
        
    case "11":
        emitirRelatorio()
                    
    case "12":
        a = False
        
    case _:
        print("Escolha uma opção válida")
