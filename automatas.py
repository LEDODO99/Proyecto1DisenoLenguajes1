from automataBuilder import *
estados=[]
transiciones=[]
contador=0

def create_subautomata(exp):
    global contador
    global estados
    global transiciones
    print("Inicial:",exp)
    for i in range(len(exp)):
        if(exp[i]=="("):
            c=0
            i=i+1
            a=i
            while ((exp[i]!=")")or(c>0)):
                if(exp[i]=="("):
                    c=c+1
                if(exp[i]==")"):
                    c=c-1
                i=i+1
            print("i:",i)
            print("a:",a)
            create_subautomata(exp[a:i])
        elif(exp[i]=="|"):
            pass
        elif(exp[i]=="*"):
            pass
        elif(exp[i]=="+"):
            pass
        elif(exp[i]=="?"):
            pass
        else:
            create_transition(exp[i])
    print("Final:",exp)
    return 0
def create_or(automata_iz,inicial_iz,final_iz,automata_de,inicial_de,final_de):
    global contador
    global estados
    global transiciones
    pass
def create_clean(automata,inicial,finalizacion):
    global contador
    global estados
    global transiciones
    pass
def create_plus(automata,inicial,finalizacion):
    global contador
    global estados
    global transiciones
    pass
def create_quest(automata,inicial,finalizacion):
    global contador
    global estados
    global transiciones
    pass
def create_transition(value):
    global contador
    global estados
    global transiciones
    pass

estados.append("q"+str(contador))
contador = contador+1
exp=input("Ingrese la expresión regular: ")
ver=input("Ingrese la expresión a evaluar: ")
#create_subautomata(exp)
a=Node()
a.define_name("A")
print(a.get_node_name())
