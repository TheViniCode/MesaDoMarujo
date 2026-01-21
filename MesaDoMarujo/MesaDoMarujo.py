import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#FUNCIONÁRIOS

usuarios = [
    "Marlon Brendon Pellense", "Gizeli Dias Wanzeler", "Vinicius Henrique Anastácio", "Artur Santos Palheta"
]

nomeCliente = "-"

senhas = [
    "Marlon1", "Gizeli2", "Vinicius3", "Artur4"
]

cargosFunc = [
    "Dono", "Chefe", "Garçom", "Estoquista"
]

cargosTotal = [
    "Dono", "Chefe", "Garçom", "Estoquista"
]

funcionarios = []

for i in range(len(usuarios)):
    funcionarios.append((f"{usuarios[i]}", f'{senhas[i]}', f'{cargosFunc[i]}'))

#ESTOQUE

itens = [
    "Cenoura", "Arroz", "Feijão", "Alface"
]

fornecedores = [
    "Agroboa", "Agrolimpo", "Agrosujo", "Agroruim"
]

quantidade = [
    12, 34, 56, 78 
]

medidaIng = [
    "kg", "kg", "kg", "un"
]

medidaTotal = [
    "kg", "un", "L"
]

ingredientes = []

for i in range(len(itens)):
    ingredientes.append((f"{itens[i]}", f'{fornecedores[i]}', f'{quantidade[i]} {medidaIng[i]}'))

estoqueMin = 10

#MESAS

mesas = {int():""}

for j in range (1, 21):
    mesas[j] = "-"

mesasDispo = []

histPedidos = {int():""}

for j in range (1, 21):
    histPedidos[j] = "-"
    numMesa = -1

def soNum(char):
        return char.isdigit()

# PRATOS

nomePrato = [
    "Macarronada", "Estrogonoffe de Frango", "Iscas de Peixe"
]

ingPrato = [
    "Macarrão, Carne Bovina Moída, Milho e Molho Vermelho.", "Arroz Branco, Filé de Frango em Cubos ao molho de Creme de Leite e Molho Vermelho.", "Filé de Peixe em Cubos à Milanesa."
]

preco = [
    18.90, 22.89, 12.25
]

precoT = float(0.0)

pratos = []

for i in range(len(nomePrato)):
    pratos.append((f"{nomePrato[i]}", preco[i], f"{ingPrato[i]}"))

def menuAberto():
    def addPrato():
        pratoEsc = tree.selection()
        if pratoEsc:
            pratoAdd = pratoEsc[0]
        else:
            pratoAdd = ""

        detalhePrato = tree.item(pratoAdd)
        valorColuna = detalhePrato.get("values")
        
        if valorColuna:
            nomeP = valorColuna[0]
            precoP = valorColuna[1]
            print(nomeP)

        if pratoAdd == "":
            messagebox.showwarning("Erro", "Nenhum Prato Selecionado!\nSelecione um prato clicando em seu nome na caixa abaixo.")
            
        for i in range(1,21):
            global precoT
            if histPedidos[i] == "-":
                histPedidos[i] = histPedidos[i] + "\n" + nomeP
                precoT = precoT+float(precoP)
                break
        messagebox.showinfo("Pedido", "Prato pedido com sucesso!")
        print(precoT)

        
    menu = tk.Toplevel()

    menu.geometry("700x450")
    menu.title("Menu")
    menu.configure(bg="light blue")
    menu.resizable(False, False)

    if cargoU == "Estoquista":
        LabelT = tk.Label(menu, text="Mesa do Marujo - Menu", background="#4CA2E4", fg="white", font=("Arial Black", 20), width=37, height=2)
        LabelT.grid(row=0, column=1, columnspan=2)
        frameT2 = ttk.Frame(menu, width=41)
        frameT2.grid(row=1, column=1, columnspan=2)

        frameT2.columnconfigure(0, weight=1)
        frameT2.columnconfigure(1, weight=1)
        frameT2.rowconfigure(1, weight=1)
        frameT2.columnconfigure(2, weight=1)
        frameT2.columnconfigure(3, weight=1)

        LabelT2 = tk.Label(master=frameT2, background="#9CCBEF", fg="white", font=("Harlow Solid Italic", 20), width=41, height=1)
        LabelT2.grid(row=1, column=1, columnspan=6)

        buttonArm = tk.Button(master=frameT2, text="Armazém", width=10, font=("Arial Black", 8), command=lambda: [estoqueAberto(), menu.destroy()])

        buttonArm.grid(row=1, column=1, sticky="w", padx=70)

    if cargoU == "Garçom":
        LabelT = tk.Label(menu, text="Mesa do Marujo - Menu", background="#4CA2E4", fg="white", font=("Arial Black", 20), width=37, height=2)
        LabelT.grid(row=0, column=1, columnspan=2)
        frameT2 = ttk.Frame(menu, width=41)
        frameT2.grid(row=1, column=1, columnspan=2)

        frameT2.columnconfigure(0, weight=1)
        frameT2.columnconfigure(1, weight=1)
        frameT2.rowconfigure(1, weight=1)
        frameT2.columnconfigure(2, weight=1)
        frameT2.columnconfigure(3, weight=1)

        LabelT2 = tk.Label(master=frameT2, background="#9CCBEF", fg="white", font=("Harlow Solid Italic", 20), width=41, height=1)
        LabelT2.grid(row=1, column=1, columnspan=6)

        buttonRes = tk.Button(master=frameT2, text="Reservas", width=10, font=("Arial Black", 8), command=lambda: [reservaAberto(), menu.destroy()]) 

        buttonRes.grid(row=1, column=1, sticky="w", padx=70)

    if cargoU == "Chefe":
        LabelT = tk.Label(menu, text="Mesa do Marujo - Menu", background="#4CA2E4", fg="white", font=("Arial Black", 20), width=37, height=2)
        LabelT.grid(row=0, column=1, columnspan=2)
        frameT2 = ttk.Frame(menu, width=41)
        frameT2.grid(row=1, column=1, columnspan=2)

        frameT2.columnconfigure(0, weight=1)
        frameT2.columnconfigure(1, weight=1)
        frameT2.rowconfigure(1, weight=1)
        frameT2.columnconfigure(2, weight=1)
        frameT2.columnconfigure(3, weight=1)

        LabelT2 = tk.Label(master=frameT2, background="#9CCBEF", fg="white", font=("Harlow Solid Italic", 20), width=41, height=1)
        LabelT2.grid(row=1, column=1, columnspan=6)

        buttonRes = tk.Button(master=frameT2, text="Reservas", width=10, font=("Arial Black", 8), command=lambda: [reservaAberto(), menu.destroy()])
        buttonArm = tk.Button(master=frameT2, text="Armazém", width=10, font=("Arial Black", 8), command=lambda: [estoqueAberto(), menu.destroy()])

        buttonRes.grid(row=1, column=1, sticky="w", padx=70)
        buttonArm.grid(row=1, column=2, sticky="w", padx=70)

    
    if cargoU == "Dono":
        LabelT = tk.Label(menu, text="Mesa do Marujo - Menu", background="#4CA2E4", fg="white", font=("Arial Black", 20), width=37, height=2)
        LabelT.grid(row=0, column=1, columnspan=2)
        frameT2 = ttk.Frame(menu, width=41)
        frameT2.grid(row=1, column=1, columnspan=2)

        frameT2.columnconfigure(0, weight=1)
        frameT2.columnconfigure(1, weight=1)
        frameT2.rowconfigure(1, weight=1)
        frameT2.columnconfigure(2, weight=1)
        frameT2.columnconfigure(3, weight=1)

        LabelT2 = tk.Label(master=frameT2, background="#9CCBEF", fg="white", font=("Harlow Solid Italic", 20), width=41, height=1)
        LabelT2.grid(row=1, column=1, columnspan=6)

        buttonFunc = tk.Button(master=frameT2, text="Funcionários", width=10, font=("Arial Black", 8), command=lambda: [funcionariosAberto(), menu.destroy()])
        buttonRes = tk.Button(master=frameT2, text="Reservas", width=10, font=("Arial Black", 8), command=lambda: [reservaAberto(), menu.destroy()])
        buttonArm = tk.Button(master=frameT2, text="Armazém", width=10, font=("Arial Black", 8), command=lambda: [estoqueAberto(), menu.destroy()])

        buttonFunc.grid(row=1, column=3, sticky="w", padx=70)
        buttonRes.grid(row=1, column=1, sticky="w", padx=70)
        buttonArm.grid(row=1, column=2, sticky="w", padx=70)

    if cargoU == "Cliente":
        LabelT = tk.Label(menu, text="Mesa do Marujo - Menu", background="#4CA2E4", fg="white", font=("Arial Black", 20), width=37, height=2)
        LabelT.grid(row=0, column=1, columnspan=2, padx=(0,270))
        cardapio = tk.Label(menu, text="Cardápio", font=("Arial Black", 12), bg="#9CCBEF", fg="white")
        cardapio.grid(row=0, column=2, sticky="w", padx=(150,0))

        framePratos = tk.Frame(menu, bg="light blue", height=100, width=100)
        framePratos.grid(row=1,column=1)

        buttonAdicionar = tk.Button(framePratos, text="Adicionar", command=lambda: [addPrato()], width=15, font=("Arial Black", 8))
        buttonAdicionar.grid(row=0, column=0, padx=(0, 550), pady=(0,50))

        buttonSaida = tk.Button(framePratos, text="Sair", width=10, font=("Arial Black", 8), command=lambda: [menu.destroy(), loginAberto()])
        buttonSaida.grid(row=0, column=0, padx=(550,0), pady=(70,120))

        tree = ttk.Treeview(framePratos, columns=['nome', 'rs', "ing"], show="headings")
        tree.heading('nome', text="Prato")
        tree.heading('rs', text="Preço")
        tree.heading('ing', text="Ingredientes")
        i = 0
        for item in pratos:
            i = i + 1
            tree.insert(parent="", index=i, iid=i, values=item)
            print(item)

        scrollV = ttk.Scrollbar(tree, orient='vertical', command=tree.yview())
        tree.configure(yscrollcommand=scrollV.set)

        tree.grid(row=1, column=0, sticky="nsew", padx=(0,33), pady=(0,0))
        scrollV.grid(row=2, column=0, sticky=tk.NS, pady=(0,100), padx=(673,0), rowspan=3)
        scrollV.configure(command=tree.yview)


    buttonSaida = tk.Button(menu, text="Sair", width=10, font=("Arial Black", 8), command=lambda: [loginAberto(), menu.destroy()])
    buttonSaida.grid(row=2, column=2, sticky="NE", padx=40, pady=290)

def funcionariosAberto():

    def removerFunc():
        funcRemovido = tree.selection()
        if funcRemovido:
            funcDemitido = funcRemovido[0]
        else:
            funcDemitido = ""

        detalheFunc = tree.item(funcDemitido)
        valorColuna = detalheFunc.get("values")
        
        if valorColuna:
            nomeFunc = valorColuna[0]

        quantDonos = 0
        for cargo in cargosFunc:
            if cargo == "Dono":
                quantDonos = quantDonos + 1
        if len(usuarios) > 1:
            if funcDemitido == "":
                messagebox.showwarning("Erro", "Nenhum Funcionário Selecionado!\nSelecione um funcionário clicando em seu nome na caixa abaixo.")
            for i in range(len(usuarios)):
                if nomeFunc == usuarios[i]:
                    numFunc = i
                    break
            if cargosFunc[numFunc] != "Dono":
                del usuarios[numFunc]
                del senhas[numFunc]
                del cargosFunc[numFunc]
                del funcionarios[numFunc]
                tree.delete(funcRemovido)
                messagebox.showinfo("Funcionário Removido", "Funcionário Removido com Sucesso!")

            else:
                if quantDonos > 1:
                    del usuarios[numFunc]
                    del senhas[numFunc]
                    del cargosFunc[numFunc]
                    del funcionarios[numFunc]
                    tree.delete(funcRemovido)
                    messagebox.showinfo("Dono Removido", "Dono Removido com Sucesso!")

                elif quantDonos <= 1:
                    messagebox.showwarning("Erro", "Não pode haver menos que 1 (um) Dono!")
        elif len(usuarios) <= 1:
            messagebox.showwarning("Erro", "Não pode haver menos que 1 (um) Funcionário!")

    def adicionarFunc():
        addFunc = tk.Toplevel()
        addFunc.title("Adicionar")
        addFunc.config(bg="light blue")
        addFunc.resizable(False, False)

        addFunc.geometry("250x270")

        addFrame = tk.Frame(addFunc)
        addFrame.pack()
        addFrame.configure(bg="Light blue")

        lblNome = tk.Label(addFrame, text="Digite o Nome do Funcionário:", fg="white", font=("Arial Black", 10), bg="Light Blue")
        lblNome.pack(pady=(20,0))

        entNome = tk.Entry(addFrame)
        entNome.pack()
        entNome.focus()

        lblSenha = tk.Label(addFrame, text="Digite a Senha do Funcionário:", fg="white", font=("Arial Black", 10),bg="Light Blue")
        lblSenha.pack(pady=(20,0))

        entSenha = tk.Entry(addFrame)
        entSenha.pack()

        lblCargo = tk.Label(addFrame, text="Escolha o Cargo do Funcionário:", fg="white", font=("Arial Black", 10), bg="Light Blue")
        lblCargo.pack(pady=(20,0))

        comboCargo = ttk.Combobox(addFrame)
        comboCargo["values"] = cargosTotal
        comboCargo.state(["readonly"])
        comboCargo.pack()

        confirmButton = tk.Button(addFrame, text="Confirmar", command=lambda: [Confirmar(entNome, comboCargo, entSenha)], height=1, width=10)
        confirmButton.pack(pady=(10, 0))
        cancellButton = tk.Button(addFrame, text="Cancelar", command=lambda: [addFunc.destroy()], height=1, width=10)
        cancellButton.pack(pady=(10, 0))

        def Confirmar(nomeCaixa, cargoCaixa, senhaCaixa):   
            nome = nomeCaixa.get()
            cargo = cargoCaixa.get()
            senha = senhaCaixa.get()
            proceder = True
        
            if nome and cargo and senha:
                for i in range(len(usuarios)):
                    if nome == usuarios[i]:
                        proceder = False
                        break
                
                if proceder:
                    usuarios.append(nome)
                    cargosFunc.append(cargo)
                    senhas.append(senha)
                    ultimo_usuario = usuarios[-1]
                    ultimo_senha = senhas[-1]
                    ultimo_cargo = cargosFunc[-1]
                    funcionarios.append((ultimo_usuario, ultimo_senha, ultimo_cargo))
                    tree.insert("", "end", values=(ultimo_usuario, ultimo_senha, ultimo_cargo))
                    messagebox.showinfo("Cadastrado", "Funcionário Cadastrado com Sucesso!")
                    addFunc.destroy()  # Se a janela addFunc for válida
                else:
                        messagebox.showwarning("Erro", "Funcionário já Cadastrado!")
            else:
                messagebox.showwarning("Erro", "Houve algum erro no cadastro!\nTente novamente.")

    func = tk.Toplevel()

    func.title("Funcionários")
    func.configure(bg="Light Blue")
    func.geometry("690x350")
    func.resizable(False, False)

    FrameFunc = tk.Frame(func)
    FrameFunc.grid(row=0, column=0)
    FrameFunc.configure(bg="Light Blue")

    LabelT = tk.Label(FrameFunc, text="Mesa do Marujo - Funcionários", background="#4CA2E4", fg="white", font=("Arial Black", 20), width=32, height=2)
    LabelT.grid(row=0, column=0, columnspan=2, ipadx=50)

    buttonDeletar = tk.Button(FrameFunc, text="Remover", command=lambda: removerFunc(), width=15, font=("Arial Black", 8))
    buttonDeletar.grid(row=1, column=0, padx=(0, 550), pady=(20,30))

    buttonAdicionar = tk.Button(FrameFunc, text="Adicionar", command=lambda: adicionarFunc(), width=15, font=("Arial Black", 8))
    buttonAdicionar.grid(row=1, column=0, padx=(0, 550), pady=(70,0))

    buttonSaida = tk.Button(FrameFunc, text="Sair", width=10, font=("Arial Black", 8), command=lambda: [menuAberto(), func.destroy()])
    buttonSaida.grid(row=1, column=0, padx=(550,0), pady=(30, 0))

    tree = ttk.Treeview(FrameFunc, columns=['nome', 'senha', 'cargo'], show="headings")
    tree.heading('nome', text="Funcionário")
    tree.heading('senha', text="Senha")
    tree.heading('cargo', text="Cargo")
    i = 0
    for item in funcionarios:
        i = i + 1
        tree.insert(parent="", index=i, iid=i, values=item)

    scroll = ttk.Scrollbar(tree, orient='vertical', command=tree.yview())
    tree.configure(yscrollcommand=scroll.set)

    tree.grid(row=2, column=0, sticky="nsew", pady=(22,0))
    scroll.grid(row=2, column=0, sticky=tk.NS, pady=(0,100), padx=(673,0), rowspan=3)
    scroll.configure(command=tree.yview)

def estoqueAberto():
     
    def novoIngrediente():
        addIng = tk.Toplevel()
        addIng.title("Adicionar")
        addIng.config(bg="light blue")
        addIng.resizable(False, False)

        addIng.geometry("250x280")

        addFrame = tk.Frame(addIng)
        addFrame.pack()
        addFrame.configure(bg="Light blue")
    
        lblNome = tk.Label(addFrame, text="Digite o Nome do ingrediente:", fg="white", font=("Arial Black", 10), bg="Light Blue")
        lblNome.pack(pady=(20,0))

        entNome = tk.Entry(addFrame)
        entNome.pack()
        entNome.focus()

        lblForn = tk.Label(addFrame, text="Digite o nome do Fornecedor:", fg="white", font=("Arial Black", 10),bg="Light Blue")
        lblForn.pack(pady=(20,0))

        entForn = tk.Entry(addFrame)
        entForn.pack()

        lblQuant = tk.Label(addFrame, text="O estoque do ingrediente:", fg="white", font=("Arial Black", 10), bg="Light Blue")
        lblQuant.pack(pady=(20,0))

        validation = addIng.register(soNum)

        frameQuant = tk.Frame(addFrame)
        frameQuant.pack()

        entQuant = tk.Entry(frameQuant, validate="key", validatecommand=(validation, '%S'), width=13)
        entQuant.pack(side="left")

        ingCombo = ttk.Combobox(frameQuant, width=3)
        ingCombo["values"] = medidaTotal
        ingCombo.state(["readonly"])
        ingCombo.pack(side="right")

        confirmButton = tk.Button(addFrame, text="Confirmar", command=lambda: [Confirmar(entNome, entForn, entQuant, ingCombo)], height=1, width=10)
        confirmButton.pack(pady=(20, 0))
        cancellButton = tk.Button(addFrame, text="Cancelar", command=lambda: [addIng.destroy()], height=1, width=10)
        cancellButton.pack(pady=(10, 0))

        def Confirmar(nomeCaixa, fornecedorCaixa, quantCaixa, medidaCaixa):  
            nome = nomeCaixa.get()
            fornecedor = fornecedorCaixa.get()
            quant = quantCaixa.get()
            medida = medidaCaixa.get()
            proceder = True
            if nome != "" and fornecedor != "" and quant != "" and medida != "":
                for i in range(len(itens)):
                    if nome == itens[i]:
                        proceder = False
                        break
                if proceder == True:
                    itens.append(nome)
                    fornecedores.append(fornecedor)
                    quantidade.append(quant)
                    medidaIng.append(medida)
                    ingredientes.append((f"{itens[len(itens)-1]}", f"{fornecedores[len(fornecedores)-1]}", f"{quantidade[len(quantidade)-1]} {medidaIng[len(medidaIng)-1]}"))
                    tree.insert("", "end", values=(f"{itens[len(itens)-1]}", f"{fornecedores[len(fornecedores)-1]}", f"{quantidade[len(quantidade)-1]} {medidaIng[len(medidaIng)-1]}"))
                    messagebox.showinfo("Cadastrado", "Ingrediente Cadastrado com Sucesso!")
                    addIng.destroy()
                else:
                    messagebox.showwarning("Erro", "Ingrediente já Cadastrado!\nTente editar o ingrediente clicando nele e depois em 'Editar'")
            else:
                messagebox.showwarning("Erro", "Houve algum erro no cadastro!\nTente novamente.")

    def removerItem():
        numIng = 0
        ingRemovido = tree.selection()
        if ingRemovido:
            itemRemovido = ingRemovido[0]
        else:
            itemRemovido = ""

        detalheFunc = tree.item(itemRemovido)
        valorColuna = detalheFunc.get("values")
        
        if valorColuna:
            nomeIng = valorColuna[0]

        if itemRemovido == "":
            messagebox.showwarning("Erro", "Nenhum Ingrediente Selecionado!\nSelecione um ingrediente clicando em seu nome na caixa abaixo.")

        for i in range(len(itens)):
            if nomeIng == itens[i]:
                numIng = i
                break

        del itens[numIng]
        del fornecedores[numIng]
        del quantidade[numIng]
        del medidaIng[numIng]
        del ingredientes[numIng]
        tree.delete(ingRemovido)
        messagebox.showinfo("Ingrediente Removido", "Ingrediente Removido com Sucesso!")

    def editarEstoque(MMCombo, itemCaixa, novoEstoqueCaixa):
        def adicionarEstoque():
            estoqueAdicionado = itemCaixa.get()
            if len(itens) > 1:
                for i in range(len(itens)):
                    if estoqueAdicionado == itens[i]:
                        numItem = i 
                        break
            valorNovo = novoEstoqueCaixa.get()
            quantidade[numItem] = int(quantidade[numItem]) + int(valorNovo)
            messagebox.showinfo("Adicionado", "Valor Adicionado ao Estoque.")
            for i in range(len(itens)):
                ingredientes[i] = (f"{itens[i]}", f'{fornecedores[i]}', f'{quantidade[i]} {medidaIng[i]}')
            for i in tree.get_children():
                tree.delete(i)
            i = 0
            for ing in ingredientes:
                i = i + 1
                tree.insert(parent="", index=i, iid=i, values=ing)

        def retirarEstoque():
            estoqueRetirado = itemCaixa.get()
            if len(itens) > 1:
                for i in range(len(itens)):
                    if estoqueRetirado == itens[i]:
                        numItem = i 
                        break
            valorRetirado = novoEstoqueCaixa.get()
            if int(valorRetirado) <= int(quantidade[numItem]):
                quantidade[numItem] = int(quantidade[numItem]) - int(valorRetirado)
                messagebox.showinfo("Removido", "Valor Removido do Estoque.")
                print(quantidade[numItem])
                for i in range(len(itens)):
                    ingredientes[i] = (f"{itens[i]}", f'{fornecedores[i]}', f'{quantidade[i]} {medidaIng[i]}')
                for i in tree.get_children():
                    tree.delete(i)
                i = 0
                for ing in ingredientes:
                    i = i + 1
                    tree.insert(parent="", index=i, iid=i, values=ing)
            else:
                messagebox.showwarning("Erro", "O valor mencionado é maior do que a quantidade em estoque.")
            if quantidade[numItem] <= estoqueMin:
                messagebox.showwarning("Aviso!", f"Estoque de {itens[numItem]} está quase acabando!\nConsidere reabastecer o estoque!")

        comboV = MMCombo.get()

        if comboV == "+":
            adicionarEstoque()
        elif comboV == "-":
            retirarEstoque()
        else:
            messagebox.showwarning("Erro", "Algo deu errado\nTente denovo.")

    def editarAberto():
        edit = tk.Toplevel()
        edit.title("Editar")
        edit.geometry("200x240")
        edit.config(bg="light blue")
        edit.resizable(False, False)

        validation = edit.register(soNum)

        editFrame = tk.Frame(edit)
        editFrame.pack()
        editFrame.configure(bg="Light blue")

        lblIng = tk.Label(editFrame, text="Escolha o Ingrediente:", fg="white", font=("Arial Black", 10), bg="Light Blue")
        lblIng.pack(pady=(20,0))

        ingCombo = ttk.Combobox(editFrame)
        ingCombo["values"] = itens
        ingCombo.state(["readonly"])
        ingCombo.pack()
        ingCombo.focus()

        lblQuant = tk.Label(editFrame, text="Digite a Quantidade:", fg="white", font=("Arial Black", 10), bg="Light Blue")
        lblQuant.pack(pady=(20,0))

        frameQuant = tk.Frame(editFrame, bg="light blue")
        frameQuant.pack()

        entQuant = tk.Entry(frameQuant, validate="key", validatecommand=(validation, '%S'), width=16)
        entQuant.pack(side="right", padx=(0,15))

        MMCombo = ttk.Combobox(frameQuant, width=3)
        MMCombo["values"] = ["+", "-"]
        MMCombo.state(["readonly"])
        MMCombo.pack(side="left", padx=(12,0), pady=(1,0))

        confirmButton = tk.Button(editFrame, text="Confirmar", command=lambda: [editarEstoque(MMCombo, ingCombo, entQuant)], height=1, width=10)
        confirmButton.pack(pady=(30, 0))
        cancellButton = tk.Button(editFrame, text="Cancelar", command=lambda: [edit.destroy()], height=1, width=10)
        cancellButton.pack(pady=(10, 0))

    estoque = tk.Toplevel()

    estoque.title("Armazém")
    estoque.configure(bg="Light Blue")
    estoque.geometry("690x360")
    estoque.resizable(False, False)

    FrameEstoque = tk.Frame(estoque)
    FrameEstoque.grid(row=0, column=0)
    FrameEstoque.configure(bg="Light Blue")

    LabelT = tk.Label(FrameEstoque, text="Mesa do Marujo - Armazém", background="#4CA2E4", fg="white", font=("Arial Black", 20), width=32, height=2)
    LabelT.grid(row=0, column=0, columnspan=2, ipadx=50)

    buttonDeletar = tk.Button(FrameEstoque, text="Remover", width=15, font=("Arial Black", 8), command=lambda: removerItem())
    buttonDeletar.grid(row=1, column=0, padx=(0, 550), pady=(0,30))

    buttonAdicionar = tk.Button(FrameEstoque, text="Adicionar", width=15, font=("Arial Black", 8), command=lambda: novoIngrediente())
    buttonAdicionar.grid(row=1, column=0, padx=(0, 550), pady=(30,0))

    buttonEditar = tk.Button(FrameEstoque, text="Editar", width=15, font=("Arial Black", 8), command=lambda: editarAberto())
    buttonEditar.grid(row=1, column=0, padx=(0, 550), pady=(90,0))

    buttonSaida = tk.Button(FrameEstoque, text="Sair", width=10, font=("Arial Black", 8), command=lambda: [menuAberto(), estoque.destroy()])
    buttonSaida.grid(row=1, column=0, padx=(550,0), pady=(30, 0))

    tree = ttk.Treeview(FrameEstoque, columns=['nome', 'fornecedor', 'quantAt'], show="headings")
    tree.heading('nome', text="Ingrediente")
    tree.heading('fornecedor', text="Fornecedor")
    tree.heading('quantAt', text="Quantidade")

    scroll = ttk.Scrollbar(tree, orient='vertical', command=tree.yview())
    tree.configure(yscrollcommand=scroll.set)

    tree.grid(row=2, column=0, sticky="nsew", pady=(22,0))
    scroll.grid(row=0, column=0, sticky=tk.NS, pady=(0,100), padx=(673,0))
    scroll.configure(command=tree.yview)

    i = 0
    for ing in ingredientes:
        i = i + 1
        tree.insert(parent="", index=i, iid=i, values=ing)

def reservaAberto():
    def mostrarLista(clienteCombo):
        cliente = clienteCombo.get()
        listaPedidos = ""
        for i in range(1,21):
            if histPedidos[i] != "-":
                listaPedidos = listaPedidos + "\n" + histPedidos[i]
        if cliente == "":
            messagebox.showwarning("Erro", "Selecione um cliente!")
        else:
            for i in range(1,21):
                if cliente == mesas[i]:
                    global precoT
                    messagebox.showwarning("Lista de Pedidos", f"O cliente {cliente} pediu:\n{listaPedidos}\n\nTotal: R${precoT}")
                    break

    reserva = tk.Toplevel()

    reserva.title("Reserva")
    reserva["bg"] = "light blue"
    reserva.resizable(False, False)

    frameReserva = tk.Frame(reserva, bg="light blue")
    frameReserva.grid(row=0, column=0)

    LabelT = tk.Label(frameReserva, text="Mesa do Marujo - Reserva", background="#4CA2E4", fg="white", font=("Arial Black", 17), height=2)
    LabelT.grid(row=0, column=0, columnspan=2, ipadx=50)

    clientes = [""]

    for i in range(1,21):
        if mesas[i] != "-":
            clientes.append(mesas[i])

    clientesCombo = ttk.Combobox(frameReserva, values=clientes, width=30)
    clientesCombo.grid(row=1, column=1, padx=(0, 70), pady=(40,0))

    btnBuscar = tk.Button(frameReserva, text="Verificar", command=lambda: [mostrarLista(clientesCombo)], width=25)
    btnBuscar.grid(row=2, column=1, pady=(20, 40), padx=(0,65))

def loginAberto():

    login = tk.Toplevel()

    login.title("Login")
    login.configure(bg="light blue")
    login.geometry("379x244")
    login.resizable(False, False)

    def loginFunc():    
        FrameLogin = tk.Frame(login)
        FrameLogin.grid(row=0, column=0)
        FrameLogin.configure(bg="light blue")

        LabelT = tk.Label(FrameLogin, text="Mesa do Marujo - Login", background="#4CA2E4", fg="white", font=("Arial Black", 17), height=2)
        LabelT.grid(row=0, column=0, columnspan=2, ipadx=50)

        nomeL = tk.Label(FrameLogin, text="Nome: ", font=("Arial Black", 8), fg="white", bg="Light blue")
        nomeL.grid(row=1, column=0, sticky="w", pady=(30, 0), padx=20)

        senhaL = tk.Label(FrameLogin, text="Senha: ", font=("Arial Black", 8), fg="white", bg="Light blue")
        senhaL.grid(row=2, column=0, sticky="w", pady=(30, 20), padx=20)

        nomeT = tk.Entry(FrameLogin, width=40)
        nomeT.focus()
        nomeT.grid(row=1, column=1, sticky="w", pady=(30, 0), padx=20)
        
        senhaT = tk.Entry(FrameLogin, width=40, show="*")
        senhaT.grid(row=2, column=1, sticky="w", pady=(30, 20), padx=20)

        btnLogar = tk.Button(FrameLogin, text="Entrar", font=("Arial Black", 8), command=lambda: [verificarLogin(nomeT.get(), senhaT.get(), usuarios, senhas, msgErro, login)])
        btnLogar.grid(row=3, column=1, sticky=tk.E, ipadx=15, padx=(0,35), pady=(0,10))

        btnCliente = tk.Button(FrameLogin, text="Cliente", font=("Arial Black", 8), command=lambda: [loginCliente(), FrameLogin.destroy()])
        btnCliente.grid(row=3, column=0, sticky=tk.E, ipadx=15, padx=(20,0), pady=(0,10))

        msgErro = tk.Label(FrameLogin, text="", fg="red", bg="light blue", font=("Harlow Solid Italic", 12))
        msgErro.grid(row=3, column=0, sticky=tk.W, pady=(0,10), padx=(20,0), columnspan=2)

    def loginCliente():    
        FrameLogin = tk.Frame(login)
        FrameLogin.grid(row=0, column=0)
        FrameLogin.configure(bg="light blue")

        LabelT = tk.Label(FrameLogin, text="Mesa do Marujo - Cliente", background="#4CA2E4", fg="white", font=("Arial Black", 16), height=2)
        LabelT.grid(row=0, column=0, columnspan=2, ipadx=50)

        nomeL = tk.Label(FrameLogin, text="Nome: ", font=("Arial Black", 8), fg="white", bg="Light blue")
        nomeL.grid(row=1, column=0, sticky="w", pady=(30, 0), padx=20)

        mesaL = tk.Label(FrameLogin, text="Mesa: ", font=("Arial Black", 8), fg="white", bg="Light blue")
        mesaL.grid(row=2, column=0, sticky="w", pady=(30, 20), padx=20)

        nomeT = tk.Entry(FrameLogin, width=40)
        nomeT.focus()
        nomeT.grid(row=1, column=1, sticky="w", pady=(30, 0), padx=20)
        
        for i in range(1, 21):
            if mesas[i] == "-":
                mesasDispo.append(i)

        mesaU = ttk.Combobox(FrameLogin, width=37, values=mesasDispo, state="readonly", textvariable=numMesa)
        mesaU.grid(row=2, column=1, sticky="w", pady=(30, 20), padx=20)

        btnLogar = tk.Button(FrameLogin, text="Entrar", font=("Arial Black", 8), command=lambda: [criarCliente(nomeT, mesaU, login)])
        btnLogar.grid(row=3, column=1, sticky=tk.E, ipadx=15, padx=(0,35), pady=(0,10))

        btnFunc = tk.Button(FrameLogin, text="Func.", font=("Arial Black", 8), command=lambda: [loginFunc(), FrameLogin.destroy()])
        btnFunc.grid(row=3, column=0, sticky=tk.E, ipadx=15, padx=(20,0), pady=(0,10))

        msgErro = tk.Label(FrameLogin, text="", fg="red", bg="light blue", font=("Harlow Solid Italic", 12))
        msgErro.grid(row=3, column=0, sticky=tk.W, pady=(0,10), padx=(20,0), columnspan=2)

    if isFunc == True:
        loginFunc()
    else:
        loginCliente()
    
def verificarLogin(nome, senha, usuarios, senhas, msgErro, login):
    for i in range(len(usuarios)):
        if nome == usuarios[i] and senha == senhas[i] and nome != '' and senha != '':
            global cargoU
            cargoU = cargosFunc[i]
            menuAberto()
            login.destroy()
        else:
            msgErro["text"] = "Usuário ou Senha Incorretos."

def criarCliente(nome, mesaEscolhida, login):
    global numMesa
    global nomeCliente
    global cargoU
    numMesa = mesaEscolhida.get()
    nomeCliente = nome.get()
    if numMesa != "" and nomeCliente != "":
        cargoU = "Cliente"
        menuAberto()
        login.destroy()
        for i in range(1,21):
            if mesas[i] == "-":
                mesas[i] = nomeCliente
                break
    else:
        messagebox.showwarning("Erro", "Houve algum erro.\nTente novamente!")


isFunc = False
if isFunc == True:
    cargoU = ""
janela = tk.Tk()
janela.attributes("-alpha", 0.0)
loginAberto()
janela.mainloop()
