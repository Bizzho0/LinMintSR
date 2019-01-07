#Agenda_BZO.py

from tkinter  import *
from tkinter  import messagebox 

lista=[]

def guardar():
	n=nombre.get()
	ap=app.get()
	am=apm.get()
	t=telefono.get()
	c=correo.get()
	lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
	escribirContacto()
	messagebox.showinfo("GUARDADO","El Contacto se a guardado en  la Agenda.")
	nombre.set("")
	app.set("")
	apm.set("")
	telefono.set("")
	correo.set("")
	consultar()

def eliminar():
	eliminado= conteliminar.get()
	removido= False
	for elemento in lista:
		arreglo= elemento.split("$")
		if conteliminar.get() == arreglo[3]:
			lista.remove(elemento)
			removido= True 
	escribirContacto()
	consultar()
	if removido:
		messagebox.showinfo("ELIMINADO","El Contacto  se a Eliminado correctamente."+eliminado)

def consultar():
	r= Text(vp, width=80, height=15)
	lista.sort()
	valores=[]
	r.insert(INSERT,"Nombre\t\tApellido P\t\tApellido M\t\tTelefono\t\tCorreo\n")
	for elemento in lista:
		arreglo=elemento.split("$")
		valores.append(arreglo[3])
		r.insert(INSERT,arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
	r.place(x=20,y=230)


	spinTelefono=Spinbox(vp,value=(valores),textvariable=conteliminar).place(x=450,y=50)

	if lista == []:
		spinTelefono=Spinbox(vp,value=(valores)).place(x=450,y=50)
	r.config(state=DISABLED)

def iniciarArchivo():
	archivo=open("ag.txt","a")
	archivo.close()

def cargar():
	archivo=open("ag.txt","r")
	linea=archivo.readline()
	if linea:
		while linea:
			if linea[-1] == '\n':
				linea=linea[:-1]
			lista.append(linea)
			linea=archivo.readline()
	archivo.close()

def escribirContacto():
	archivo=open("ag.txt","w")
	lista.sort()
	for elemento in lista:
		archivo.write(elemento+"\n")
	archivo.close()

vp= Tk()

nombre= StringVar()
app= StringVar()
apm= StringVar()
correo= StringVar()
telefono= StringVar()
conteliminar= StringVar()

colorFondo= "#069"
colorLetra="#DEF"

vp.title("Agenda")
vp.geometry("690x510")
vp.configure(background=colorFondo)

iniciarArchivo()
cargar()
consultar()


etiquetaTitulo= Label(vp,text="Agenda", bg=colorFondo,fg=colorLetra,font=("Helvetica",18)).place(x=230,y=10)
etiquetaN= Label(vp, text="Nombre: ",bg=colorFondo,fg=colorLetra).place(x=50,y=50)
etiquetaApp= Label(vp, text="Apellido Paterno: ",bg=colorFondo,fg=colorLetra).place(x=50,y=80)
etiquetaApm= Label(vp, text="Apellido Materno: ",bg=colorFondo,fg=colorLetra).place(x=50,y=110)
etiquetaTel= Label(vp, text="Telefono: ",bg=colorFondo,fg=colorLetra).place(x=50,y=140)
etiquetaCorreo= Label(vp, text="Correo: ",bg=colorFondo,fg=colorLetra).place(x=50,y=170)
etiquetaEliminar= Label(vp,text="Eliminar Tel: ",bg=colorFondo,fg=colorLetra).place(x=370,y=50)

cajaN = Entry(vp,textvariable=nombre).place(x=150,y=50)
cajaApp= Entry(vp,textvariable=app).place(x=150,y=80)
cajaApm = Entry(vp,textvariable=apm).place(x=150,y=110)
cajaTel = Entry(vp,textvariable=telefono).place(x=150,y=140)
cajaCorreo = Entry(vp,textvariable=correo).place(x=150,y=170)

spinTelefono= Spinbox(vp,textvariable=conteliminar).place(x=450,y=50)

botonGuardar= Button(vp,text="Guardar",command=guardar,bg="#25A",fg="white",relief="ridge",bd=3).place(x=180,y=200)
botonEliminar= Button(vp,text="Eliminar",command=eliminar,bg="#508",fg="white",relief="ridge",bd=3).place(x=470,y=80)
botonSalir= Button(vp,text="SALIR",command=vp.quit,bg="#F00",fg="white",relief="ridge",bd=3).pack(side=BOTTOM)#lace(x=470,y=200)
mainloop()