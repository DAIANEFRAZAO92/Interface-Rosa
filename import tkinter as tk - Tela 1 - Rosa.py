import tkinter as tk
from tkinter import ttk

#  adicionar produto ao painel
def adicionar_produto():
    produto = entry_produto.get()
    tamanho = entry_tamanho.get()
    quantidade = entry_quantidade.get()
    csosn = entry_csosn.get()
    cfop = entry_cfop.get()
    unidade = entry_unidade.get()
    custo = entry_custo.get()
    Venda = entry_venda.get() 

    #  árvore de visualização
    tree.insert("", "end", values=(produto, tamanho, quantidade, csosn, cfop, unidade, custo, Venda))

    # Limpar os campos de entrada após adicionar o produto
    entry_produto.delete(0, tk.END)
    entry_tamanho.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_csosn.delete(0, tk.END)
    entry_cfop.delete(0, tk.END)
    entry_unidade.delete(0, tk.END)
    entry_custo.delete(0,tk.END)
    entry_venda.delete(0,tk.END)

# remover o produto selecionado
def remover_produto():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

# Criação da janela principal
root = tk.Tk()
root.title("Controle de Estoque")
root.configure(bg="pink")  # Define a cor de fundo da janela

# Criação dos rótulos e campos de entrada
tk.Label(root, text="Produto:", bg="pink", fg="white").grid(row=0, column=0)
entry_produto = tk.Entry(root)
entry_produto.grid(row=0, column=1)


tk.Label(root, text="Tamanho:", bg="pink", fg="white").grid(row=1, column=0)
entry_tamanho = tk.Entry(root)
entry_tamanho.grid(row=1, column=1)

tk.Label(root, text="Quantidade:", bg="pink", fg="white").grid(row=2, column=0)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=2, column=1)

tk.Label(root, text="Csosn:", bg="pink", fg="white").grid(row=3, column=0)
entry_csosn = tk.Entry(root)
entry_csosn.grid(row=3, column=1)


tk.Label(root, text="Cfop", bg="pink", fg="white").grid(row=4, column=0)
entry_cfop = tk.Entry(root)
entry_cfop.grid(row=4, column=1)

tk.Label(root, text="Unidade de Medida:", bg="pink", fg="white").grid(row=5, column=0)
entry_unidade = tk.Entry(root)
entry_unidade.grid(row=5, column=1)


tk.Label(root, text="custo:", bg="pink", fg="white").grid(row=6, column=0)
entry_custo = tk.Entry(root)
entry_custo.grid(row=6, column=1)

tk.Label(root, text="venda:", bg="pink", fg="white").grid(row=7, column=0)
entry_venda = tk.Entry(root)
entry_venda.grid(row=7, column=1)





# Botão para adicionar produto
btn_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto, bg="brown", fg="white")
btn_adicionar.grid(row=9, column=0, columnspan=2)

# Botão para remover produto
btn_remover = tk.Button(root, text="Remover Produto", command=remover_produto, bg="red", fg="white")
btn_remover.grid(row=9, column=2, columnspan=2)

# Criação do painel de visualização (Treeview)
columns = ("Produto", "Tamanho", "Quantidade", "CSOSN", "CFOP", "Unidade","custo","valor")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=8, column=0, columnspan=4)







# Executa a aplicação
root.mainloop()
