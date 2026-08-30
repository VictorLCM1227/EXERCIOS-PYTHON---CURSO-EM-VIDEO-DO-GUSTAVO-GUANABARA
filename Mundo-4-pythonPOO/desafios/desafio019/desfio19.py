from rich import print
from rich.panel import Panel

class Livro:

    def __init__(self, titulo, paginas):
        self.titilo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":book: [blue]Você acabou de abrir o livro '[/][red]{self.titilo}[/][blue]' que tem [/][green]{self.paginas} paginas[/] [blue] no total. Você agora está na [/][yellow]página 1[/]")

    def avancar_paginas(self, avanco):
        avancos = 0
        for pagina in range(avanco):
            teste = self.pagina_atual
            if teste == self.paginas:
                print(f"[red]Você chegou ao final do livro '{self.titilo}'")
                break
            else:
                print(f'Pag{pagina}', end=' ▶ ')
                avancos += 1
                self.pagina_atual += 1
        print(f'[blue]Você avançou {avancos} páginas e agora está na [/][yellow]página {self.pagina_atual}[/]')


l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
from rich import print
from rich.panel import Panel

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f":book: [blue]Você acabou de abrir o livro '[/][red]{self.titulo}[/][blue]' que tem [/][green]{self.paginas} paginas[/] [blue] no total. Você agora está na [/][yellow]página 1[/]")

    def avancar_paginas(self, avanco):
        avancos = 0
        for pagina in range(avanco):
            teste = self.pagina_atual
            if teste == self.paginas:
                print(f"[red]Você chegou ao final do livro '{self.titulo}'")
                break
            else:
                print(f'Pag{pagina}', end=' ▶ ')
                avancos += 1
                self.pagina_atual += 1
        self.pagina_atual += avancos
        print(f'[blue]Você avançou {avancos} páginas e agora está na [/][yellow]página {self.pagina_atual}[/]')


l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)