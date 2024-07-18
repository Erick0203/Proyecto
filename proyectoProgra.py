import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkcalendar import DateEntry  # Importar el widget DateEntry de tkcalendar
import re

# Función para conectar a la base de datos MySQL
def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="localhost",    # Dirección del servidor MySQL (puede ser localhost si es local)
            user="admin",        # Nombre de usuario de MySQL
            password="12345",    # Contraseña del usuario de MySQL
            database="citas"     # Nombre de la base de datos que quieres utilizar
        )
        return conexion
    except mysql.connector.Error as error:
        messagebox.showerror("Error de conexión", f"Error al conectar a la base de datos: {error}")
        return None

# Función para validar que el texto contiene solo letras y espacios
def validar_letras(texto):
    patron = re.compile(r'^[a-zA-Z áéíóúÁÉÍÓÚñÑüÜ]+$')  # Permitir letras con tildes y caracteres especiales
    return patron.match(texto)

# Función para validar que el texto contiene solo números
def validar_numeros(texto):
    return texto.isdigit()

# Función para agregar una cita a la base de datos
def agregar_cita():
    nombre = entry_nombre.get()
    fecha = cal_fecha.get_date()  # Obtener la fecha seleccionada del widget DateEntry
    hora = combo_hora.get()
    telefono = entry_telefono.get()
    descripcion = entry_descripcion.get()

    # Validación básica
    if nombre == "" or fecha == "" or hora == "":
        messagebox.showwarning("Datos incompletos", "Por favor completa todos los campos.")
        return
    
    # Validación de nombre (solo letras)
    if not validar_letras(nombre):
        messagebox.showwarning("Formato incorrecto", "El nombre solo puede contener letras.")
        return

    # Validación de teléfono (solo números)
    if not validar_numeros(telefono):
        messagebox.showwarning("Formato incorrecto", "El teléfono solo puede contener números.")
        return

    # Conectar a MySQL
    conexion = conectar_mysql()
    if conexion is None:
        return

    # Crear cursor
    cursor = conexion.cursor()

    # Insertar datos en la tabla citas
    insert_query = "INSERT INTO citas (nombre, fecha, hora, telefono, descripcion) VALUES (%s, %s, %s, %s, %s)"
    datos_cita = (nombre, fecha, hora, telefono, descripcion)

    try:
        cursor.execute(insert_query, datos_cita)
        conexion.commit()
        messagebox.showinfo("Cita Agregada", "La cita ha sido agendada correctamente.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error al agregar cita", f"No se pudo agregar la cita: {error}")
    finally:
        # Cerrar conexión y cursor
        cursor.close()
        conexion.close()

# Función para validar ingreso de caracteres en el campo de nombre
def validar_ingreso_nombre(event):
    char = event.char
    # Permitir solo letras y la tecla de retroceso (Backspace)
    if not char.isalpha() and char != ' ' and char != '\b':
        return 'break'  # Detener la propagación del evento

# Función para validar ingreso de caracteres en el campo de teléfono
def validar_ingreso_telefono(event):
    char = event.char
    # Permitir solo números y la tecla de retroceso (Backspace)
    if not char.isdigit() and char != '\b':
        return 'break'  # Detener la propagación del evento

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Sistema de Agendamiento de Citas")
root.geometry("460x380")  # Tamaño de la ventana

root.configure(bg='khaki')  # Color de fondo
label_font = ('Algerian', 12)  # Fuente y tamaño para las etiquetas

# Título de la ventana
titulo_label = tk.Label(root, text="Sistema de Agendamiento de Citas", font=('Algerian', 16, 'bold'), bg='#E0E0E0')
titulo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Etiquetas y campos de entrada para nombre, fecha, hora, teléfono y descripción
label_nombre = tk.Label(root, text="Nombre:", font=label_font, bg='#E0E0E0')
label_nombre.grid(row=1, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(root, font=label_font, width=30)
entry_nombre.grid(row=1, column=1, padx=10, pady=10)

label_fecha = tk.Label(root, text="Fecha:", font=label_font, bg='#E0E0E0')
label_fecha.grid(row=2, column=0, padx=10, pady=10)

# Widget DateEntry para seleccionar la fecha
cal_fecha = DateEntry(root, font=label_font, width=27, background='darkblue', foreground='white', borderwidth=2)
cal_fecha.grid(row=2, column=1, padx=10, pady=10)

label_hora = tk.Label(root, text="Hora:", font=label_font, bg='#E0E0E0')
label_hora.grid(row=3, column=0, padx=10, pady=10)

# Combo box para seleccionar la hora
horas = [f"{i:02}:00" for i in range(0, 24)]  # Generar opciones de hora de 00:00 a 23:00
combo_hora = ttk.Combobox(root, values=horas, font=label_font, width=27)
combo_hora.grid(row=3, column=1, padx=10, pady=10)
combo_hora.current(0)  # Establecer la primera opción como la seleccionada por defecto

label_telefono = tk.Label(root, text="Teléfono:", font=label_font, bg='#E0E0E0')
label_telefono.grid(row=4, column=0, padx=10, pady=10)
entry_telefono = tk.Entry(root, font=label_font, width=30)
entry_telefono.grid(row=4, column=1, padx=10, pady=10)
entry_telefono.bind('<Key>', validar_ingreso_telefono)

label_descripcion = tk.Label(root, text="Descripción:", font=label_font, bg='#E0E0E0')
label_descripcion.grid(row=5, column=0, padx=10, pady=10)
entry_descripcion = tk.Entry(root, font=label_font, width=30)
entry_descripcion.grid(row=5, column=1, padx=10, pady=10)

# Botón para agregar la cita
boton_agregar = tk.Button(root, text="Agregar Cita", font=label_font, command=agregar_cita)
boton_agregar.grid(row=6, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
