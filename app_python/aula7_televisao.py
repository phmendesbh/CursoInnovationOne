class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        self.ligada = not self.ligada

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

print(__name__)

#__main__ é o nome da origem da execução
if __name__ == '__main__':
    televisao = Televisao()

    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    print(televisao.canal)
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(televisao.canal)
    televisao.diminui_canal()
    print(televisao.canal)
    televisao.power()
    print(televisao.ligada)
