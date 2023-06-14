class Metodos():
    def ingreso_elementos(self,List,tam):
        i=0
        while(i<tam):
            print("ingrese la Lis[",i,"]")
            num=int(input("numero "))
            List.append(num)
            i=i+1
    def imprimir_elementos(self,List,tam):
        for i in range(tam):
            print(List[i])