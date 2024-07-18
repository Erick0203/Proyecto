import tkinter as tk
from tkinter import messagebox, Toplevel, Label
from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel
from PIL import Image, ImageTk


# Colores
c_blanco = '#F4F6F6'
c_azul = '#3498DB'
c_verde = '#2ECC71'
c_tomate = '#9A7D0A'

# Diccionario para almacenar usuarios registrados
usuarios_registrados = {}

# Función para iniciar sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        # Si las credenciales coinciden, mostrar la ventana de bienvenida
        ventana_bienvenida = VentanaBienvenida(usuario)
        # Limpiar los campos de entrada
        entry_usuario.delete(0, tk.END)
        entry_contraseña.delete(0, tk.END)
    else:
        # Si las credenciales no coinciden, mostrar un mensaje de error
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos")

# Ventana de bienvenida
class VentanaBienvenida(Toplevel):
    def __init__(self, nombre):
        super().__init__()
        self.title("¡Bienvenido!")
        self.config(bg=c_blanco)

        # Lista de imágenes (solo para ejemplo, ajusta según tus imágenes)
        self.imagenes = ['F:\\Proyecto\\Proyecto\\images\\salud.png']
        self.imagen_index = 0

        # Crear un Canvas que ocupe todo el espacio disponible en la ventana
        self.canvas = tk.Canvas(self, bg=c_blanco, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Cargar y mostrar la imagen inicial como fondo del Canvas
        self.imagen = None
        self.cargar_imagen()

        # Mensaje de bienvenida
        mensaje_bienvenida = Label(self, text=f"Bienvenido, {nombre}!", bg=c_blanco, font=('Algerian', 18))
        mensaje_bienvenida.pack(pady=20)

        # Botones de navegación
        bt_anterior = CTkButton(self, text='ANTERIOR', border_color=c_azul, fg_color=c_azul, bg_color=c_blanco, hover_color=c_verde, corner_radius=12, border_width=2, command=self.anterior_imagen)
        bt_anterior.configure(font=('Algerian', 15))
        bt_anterior.pack(pady=10, side="left", padx=(20, 10))

        bt_siguiente = CTkButton(self, text='SIGUIENTE', border_color=c_azul, fg_color=c_azul, bg_color=c_blanco, hover_color=c_verde, corner_radius=12, border_width=2, command=self.siguiente_imagen)
        bt_siguiente.configure(font=('Algerian', 15))
        bt_siguiente.pack(pady=10, side="left", padx=(10, 20))

        # Botón para abrir ventana de rol de pagos
        bt_rol_pagos = CTkButton(self, text='INGRESAR A ROL DE PAGOS', border_color=c_azul, fg_color=c_azul, bg_color=c_blanco, hover_color=c_verde, corner_radius=12, border_width=2, command=self.abrir_rol_pagos)
        bt_rol_pagos.configure(font=('Algerian', 15))
        bt_rol_pagos.pack(pady=10, side="right", padx=(10, 20))

        # Vincular la función resize_image al evento <Configure> del Canvas
        self.canvas.bind("<Configure>", self.resize_image)

    def cargar_imagen(self):
        # Simplemente cargar una imagen de ejemplo para el Canvas
        imagen_pil = Image.open(self.imagenes[self.imagen_index])
        self.imagen = ImageTk.PhotoImage(imagen_pil)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagen)

    def resize_image(self, event):
        # Redimensionar la imagen al cambiar el tamaño de la ventana
        imagen_pil = Image.open(self.imagenes[self.imagen_index]).resize((event.width, event.height))
        self.imagen = ImageTk.PhotoImage(imagen_pil)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagen)

    def siguiente_imagen(self):
        # Avanzar al siguiente índice de imagen
        self.imagen_index += 1
        if self.imagen_index >= len(self.imagenes):
            self.imagen_index = 0
        self.cargar_imagen()

    def anterior_imagen(self):
        # Retroceder al índice anterior de imagen
        self.imagen_index -= 1
        if self.imagen_index < 0:
            self.imagen_index = len(self.imagenes) - 1
        self.cargar_imagen()

    def abrir_rol_pagos(self):
        # Función para abrir la ventana de ingreso al rol de pagos
        VentanaRolPagos()

# Ventana de ingreso al rol de pagos
class VentanaRolPagos(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Rol de Pagos")
        self.config(bg=c_blanco)
        self.geometry("500x400")

        # Crear campos de entrada para los datos del rol de pagos
        self.label_titulo = CTkLabel(self, text="Ingrese los datos para el rol de pagos", text_color='black')
        self.label_titulo.configure(font=('Algerian', 20))
        self.label_titulo.pack(pady=20)

        self.entry_nombre = CTkEntry(self, placeholder_text='Nombre', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco)
        self.entry_nombre.configure(font=('Algerian', 15))
        self.entry_nombre.pack(pady=10)

        self.entry_apellido = CTkEntry(self, placeholder_text='Apellido', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco)
        self.entry_apellido.configure(font=('Algerian', 15))
        self.entry_apellido.pack(pady=10)

        self.entry_sueldo = CTkEntry(self, placeholder_text='Sueldo', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco)
        self.entry_sueldo.configure(font=('Algerian', 15))
        self.entry_sueldo.pack(pady=10)

        # Botón para guardar los datos del rol de pagos
        bt_guardar = CTkButton(self, text='GUARDAR', border_color=c_azul, fg_color=c_azul, bg_color=c_blanco, hover_color=c_verde, corner_radius=12, border_width=2, command=self.guardar_datos)
        bt_guardar.configure(font=('sans serif', 15))
        bt_guardar.pack(pady=20)

    def guardar_datos(self):
        # Función para guardar los datos ingresados para el rol de pagos
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        sueldo = self.entry_sueldo.get()

        # Aquí puedes agregar la lógica para guardar los datos, por ejemplo, en una base de datos o archivo

        messagebox.showinfo("Datos Guardados", f"Datos guardados correctamente:\nNombre: {nombre}\nApellido: {apellido}\nSueldo: {sueldo}")

# Función para abrir la ventana de registro
def abrir_ventana_registro():
    VentanaRegistro()

# Ventana de registro
class VentanaRegistro(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Registro de Usuario")
        self.config(bg=c_blanco)
        self.geometry("400x580")
        ancho_widget = 300
        alto_widget = 40

        # Crear campos de entrada
        self.titulo1 = CTkLabel(self, text="Bienvenido a la ventana de Registro", text_color='black')
        self.titulo1.configure(font=('sans serif', 15))
        self.titulo1.pack(pady=5)

        self.titulo2 = CTkLabel(self, text="Ingrese su nombre:", text_color='black')
        self.titulo2.configure(font=('sans serif', 15))
        self.titulo2.pack(pady=5)

        self.entry_nombre = CTkEntry(self, placeholder_text='Nombre', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco, width=ancho_widget, height=alto_widget)
        self.entry_nombre.configure(font=('sans serif', 15))
        self.entry_nombre.pack(pady=5)

        self.titulo3 = CTkLabel(self, text="Ingrese su apellido:", text_color='black')
        self.titulo3.configure(font=('sans serif', 15))
        self.titulo3.pack(pady=5)

        self.entry_apellido = CTkEntry(self, placeholder_text='Apellido', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco, width=ancho_widget, height=alto_widget)
        self.entry_apellido.configure(font=('sans serif', 15))
        self.entry_apellido.pack(pady=5)

        self.titulo4 = CTkLabel(self, text="Ingrese un correo electrónico:", text_color='black')
        self.titulo4.configure(font=('sans serif', 15))
        self.titulo4.pack(pady=5)

        self.entry_correo = CTkEntry(self, placeholder_text='Correo', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco, width=ancho_widget, height=alto_widget)
        self.entry_correo.configure(font=('sans serif', 15))
        self.entry_correo.pack(pady=5)

        self.titulo5 = CTkLabel(self, text="Ingrese su usuario:", text_color='black')
        self.titulo5.configure(font=('sans serif', 15))
        self.titulo5.pack(pady=5)

        self.entry_usuario = CTkEntry(self, placeholder_text='Usuario', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco, width=ancho_widget, height=alto_widget)
        self.entry_usuario.configure(font=('sans serif', 15))
        self.entry_usuario.pack(pady=5)

        self.titulo6 = CTkLabel(self, text="Ingrese una contraseña:", text_color='black')
        self.titulo6.configure(font=('sans serif', 15))
        self.titulo6.pack(pady=5)

        self.entry_contraseña = CTkEntry(self, placeholder_text='Contraseña', border_color=c_tomate, fg_color='black', text_color='white', bg_color=c_blanco, show="●", width=ancho_widget, height=alto_widget)
        self.entry_contraseña.configure(font=('sans serif', 15))
        self.entry_contraseña.pack(pady=5)

        # Botón para registrar
        bt_registrar = CTkButton(self, text='REGISTRAR', border_color=c_azul, fg_color=c_azul, bg_color=c_blanco, hover_color=c_verde, corner_radius=12, border_width=2, command=self.registrar_usuario, width=ancho_widget, height=alto_widget)
        bt_registrar.configure(font=('sans serif', 15))
        bt_registrar.pack(pady=20)

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        correo = self.entry_correo.get()
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        if usuario and contraseña:
            usuarios_registrados[usuario] = contraseña
            messagebox.showinfo("Registro exitoso", f"Usuario {usuario} registrado correctamente.")
            self.destroy()  # Cerrar la ventana de registro
        else:
            messagebox.showerror("Error de registro", "Todos los campos son obligatorios.")

# Crear la ventana de inicio de sesión
ventana_login = CTk()
ventana_login.geometry('500x600+350+20')
ventana_login.title('Inicio de Sesión')

# Colores para las secciones de fondo
color_fondo_1 = '#3498DB'
color_fondo_2 = '#C0392B'

# Crear dos marcos para las secciones de fondo
frame_1 = CTkFrame(ventana_login)
frame_1.place(relwidth=0.5, relheight=1)

canvas_1 = tk.Canvas(frame_1, bg=color_fondo_1, highlightthickness=0)
canvas_1.pack(fill="both", expand=True)

frame_2 = CTkFrame(ventana_login)
frame_2.place(relx=0.5, relwidth=0.5, relheight=1)

canvas_2 = tk.Canvas(frame_2, bg=color_fondo_2, highlightthickness=0)
canvas_2.pack(fill="both", expand=True)

# Redimensionar y cargar la imagen usando PIL
logo_pil = Image.open('F:\\Proyecto\\Proyecto\\images\\logo.png')
logo_pil = logo_pil.resize((300, 300))
logo = ImageTk.PhotoImage(logo_pil)

# Crear el marco principal con fondo blanco y sin borde
frame = tk.Frame(ventana_login, bg=c_blanco)
frame.pack(expand=True)

# Superponer la imagen directamente sobre el marco principal
label_logo = tk.Label(frame, image=logo, bg=c_blanco)
label_logo.grid(columnspan=2, row=0, padx=10, pady=10)

# Obtener el ancho y alto para los widgets
ancho_widget = 300
alto_widget = 40

# Crear los campos de entrada (Entry) para usuario y contraseña
entry_usuario = CTkEntry(frame, placeholder_text='Usuario', border_color=c_tomate, fg_color='black', bg_color=c_blanco, text_color='white', width=ancho_widget, height=alto_widget)
entry_usuario.configure(font=('sans serif', 15))
entry_usuario.grid(columnspan=2, row=1, padx=10, pady=(30, 10))

entry_contraseña = CTkEntry(frame, placeholder_text='Contraseña', border_color=c_tomate, fg_color='black', bg_color=c_blanco, text_color='white', width=ancho_widget, height=alto_widget, show="●")
entry_contraseña.configure(font=('sans serif', 15))
entry_contraseña.grid(columnspan=2, row=2, padx=10, pady=(10, 20))

# Crear el botón para iniciar sesión
bt_iniciar = CTkButton(frame, border_color=c_azul, fg_color=c_azul, bg_color=c_blanco, hover_color=c_verde, corner_radius=12, border_width=2, text='INICIAR SESIÓN', width=ancho_widget, height=alto_widget, command=iniciar_sesion)
bt_iniciar.configure(font=('sans serif', 15))
bt_iniciar.grid(columnspan=2, row=3, padx=10, pady=10)

# Crear el botón para registrarse
bt_registrarse = CTkButton(frame, border_color=c_azul, fg_color=c_azul, bg_color=c_blanco, hover_color=c_verde, corner_radius=12, border_width=2, text='REGISTRARSE', width=ancho_widget, height=alto_widget, command=abrir_ventana_registro)
bt_registrarse.configure(font=('sans serif', 15))
bt_registrarse.grid(columnspan=2, row=4, padx=10, pady=10)

# Configurar el ícono de la ventana
ventana_login.iconphoto(False, logo)

# Ejecutar el bucle principal de la aplicación
ventana_login.mainloop()

