
import csv

class Nodo_Circular_Usuarios:
    def __init__ (self, Codigo = None, Nombre = None):
        self.codigo = Codigo
        self.nombre = Nombre
        self.siguiente = None
        self.anterior = None

class Circular_Doble:
    def __init__ (self):
        self.inicio = None
        self.fin = None

    def insertar(self, codigo, nombre):
        nuevo = Nodo_Circular_Usuarios(codigo, nombre)

        if estavacia():
            nuevo.siguiente = self.inicio
            nuevo.anterior = self.inicio
            self.inicio = nuevo            
        else:
            if self.inicio.siguiente==self.inicio:
                nuevo.siguiente = self.inicio
                nuevo.anterior = self.inicio
                self.inicio.siguiente = nuevo
                self.inicio.anterior = nuevo
            else:
                self.fin.siguiente = nuevo
                nuevo.anterior = self.fin
                nuevo.siguiente = self.inicio
                self.inicio.anterior = nuevo
        self.fin = nuevo

    def imprimir(self):
            """NodoCircularDoble temp = inicio;
            #print("digraph{");
            String cod = "digraph{\n";
            do{
                #print(temp.getID()+" [shape=oval, label=\"id: "+temp.getID()+" Nombre:"+temp.getNombre()+" Apellido: "+temp.getApellido()+"\"];\n");
            #print(temp.getID() +"->"+temp.getSiguiente().getID());
                
                cod+= temp.getID()+" [shape=oval, label=\"id: "+temp.getID()+" Nombre:"+temp.getNombre()+" Apellido: "+temp.getApellido()+"\"];\n";
                cod+=" ";
                cod+=temp.getID() +"->"+temp.getAnterior().getID()+"\n\n";
                cod+=temp.getID() +"->"+temp.getSiguiente().getID()+"\n\n";
                temp = temp.getSiguiente();
            }while(temp != inicio);
            #print("\n}");
            cod+="}";     
            #GraficarW g = new GraficarW();
            #g.grafica(cod);"""

    def imprimir(self):
        aux = self.inicio
        while aux != None:
            print(str(aux.codigo) +" "+ aux.nombre)
            aux = aux.siguiente

    def estavacia(self):
        return self.inicio == None

class Graficar:
    def grafica(self):
    #def grafica(String codigoAgenerar):
        """try 
            String ruta = "C:\\Users\\argue\\OneDrive\\Documents\\NetBeansProjects\\[EDD]VacasJunio2019\\TareaPractica2.dot";
            File file = new File(ruta);

#             Si el archivo no existe es creado
            if !file.exists()
                file.createNewFile();
            

                FileWriter f = new FileWriter(file);
                BufferedWriter bw = new BufferedWriter(f);
                bw.write(codigoAgenerar);
                bw.close();
                Runtime.getRuntime().exec("cmd /k start cmd.exe /K \"cd C:\\Program Files (x86)\\Graphviz2.38\\bin " + 
                        " && dot.exe -Tjpg C:\\Users\\argue\\OneDrive\\Documents\\NetBeansProjects\\[EDD]VacasJunio2019\\TareaPractica2.dot -o C:\\Users\\argue\\OneDrive\\Documents\\NetBeansProjects\\[EDD]VacasJunio2019\\TareaPractica2.jpg\""+
                        " && C:\\Users\\argue\\OneDrive\\Documents\\NetBeansProjects\\[EDD]VacasJunio2019\\TareaPractica2.jpg"+
                        " && exit");"""
                #Runtime.getRuntime().exec("cmd /k start cmd.exe");
                cmd
        #except:
    


class Carga:    
    def cargarArchivo(self):
        #ruta = "D:\\Trabajos\\U\\USAC\\Cursos\\12vo Semestre\\EDD\\201404334_EDD2S19\\EDD_1S2019_P1_201404334\\Practica 1\\p.txt"
        ruta = "D:\\Trabajos\\U\\USAC\\Cursos\\12vo Semestre\\EDD\\201404334_EDD2S19\\EDD_1S2019_P1_201404334\\Practica 1\\prueba1.csv"
        
        #Abrir un archivo .csv
        with open(ruta) as File:  
            reader = csv.reader(File)
            for row in reader:
                print(row)

        #Abrir un archivo de forma 'normal'
        #a=open(ruta,'r')
        #print(a.read())

class Menu:
    def __init__ (self):
        print("corrio el constructor")
    def menuP(self):
        print("\n 1.Play (Jugar)\n 2.Scoreboard (Puntuaciones)\n 3.User selection (Usuarios)\n 4.Reports (Reportes)\n 5.Bulk loading (Carga masiva)\n")
        
#Metodo main
if __name__ == "__main__":
    #m = Menu()
    #m.menuP()
    #c = Carga()
    #c.cargarArchivo()

    g = Graficar()
    g.grafica

    """a=1
    if a==1:
        print("es igual a "+str(a))
    else:
        print("no es igual a "+str(a))"""
