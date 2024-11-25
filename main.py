#Esta parte La creo Adrian
import tkinter as tk
from tkinter import messagebox
#Esta parte La creo Adrian

# Datos de películas y horarios
peliculas = [
    {"nombre": "Venom el último baile", "hora": "2:00 PM"},
    {"nombre": "Sonríe 2", "hora": "5:00 PM"},
    {"nombre": "Gladiador (ReEstreno)", "hora": "8:00 PM"}
]
#Esta parte La creo Adrian

# Inicialización de la venta de boletos y asientos
asientos_disponibles = {
    "Venom el último baile": [[True for _ in range(4)] for _ in range(4)],
    "Sonríe 2": [[True for _ in range(4)] for _ in range(4)],
    "Gladiador (ReEstreno)": [[True for _ in range(4)] for _ in range(4)]}
#Esta parte La creo Adrian

# Lista para almacenar ventas
ventas = []
#Esta parte La creo Adrian

# Función para mostrar el reporte general
def mostrar_reporte_general():
    reporte = "Reporte General de Ventas\n"
    total_boletos = 0
    total_ganancia = 0
    for venta in ventas:
        reporte += f"{venta['nombre_cliente']} - {venta['pelicula']} - Asiento {venta['asiento']} - ${venta['precio']}\n"
        total_boletos += 1
        total_ganancia += venta['precio']
    reporte += f"\nCantidad de boletos vendidos: {total_boletos}\nTotal Ganancia: ${total_ganancia}"
    messagebox.showinfo("Reporte General", reporte)

#Esta parte La creo AlanOGodoy

# Función para mostrar reporte por función
def mostrar_reporte_funcion(pelicula_seleccionada):
    total_boletos = 0
    total_ganancia = 0
    for venta in ventas:
        if venta["pelicula"] == pelicula_seleccionada:
            total_boletos += 1
            total_ganancia += venta["precio"]
    reporte = f"Reporte de la Función - {pelicula_seleccionada}\n"
    reporte += f"Cantidad de boletos vendidos: {total_boletos}\n"
    reporte += f"Total Ganancia: ${total_ganancia}\n"
    messagebox.showinfo(f"Reporte de {pelicula_seleccionada}", reporte)
#Esta parte La creo AlanOGodoy

# Función para realizar la venta
def vender_boleto(pelicula_seleccionada, asientos_seleccionados, ventana_seleccion_asientos):
    cliente = nombre_cliente_entry.get()
    if not cliente:
        cliente = "Cliente Anónimo"
    #Esta parte La creo AlanOGodoy

    precio = 10  # Precio fijo por ahora, puedes adaptarlo según tu lógica
    for asiento_seleccionado in asientos_seleccionados:
        fila = (asiento_seleccionado - 1) // 4
        columna = (asiento_seleccionado - 1) % 4

        if asientos_disponibles[pelicula_seleccionada][fila][columna]:
            asientos_disponibles[pelicula_seleccionada][fila][columna] = False
            ventas.append({"nombre_cliente": cliente, "pelicula": pelicula_seleccionada, "asiento": asiento_seleccionado, "precio": precio})
        else:
            messagebox.showwarning("Asiento Ocupado", f"El asiento {asiento_seleccionado} ya está ocupado.")
    #Esta parte La creo AlanOGodoy
    
    # Muestra un mensaje de confirmación con los detalles de la venta
    messagebox.showinfo("Venta Exitosa", f"Venta realizada para {cliente}\nPelicula: {pelicula_seleccionada}\nAsientos: {', '.join(map(str, asientos_seleccionados))}\nPrecio total: ${len(asientos_seleccionados) * precio}")
    #Esta parte La creo AlanOGodoy
    # Destruir la ventana de selección de asientos
    ventana_seleccion_asientos.destroy()
    #Esta parte La creo AlanOGodoy
# Función para actualizar el estado de los asientos en la interfaz
def actualizar_asientos(pelicula_seleccionada, frame_asientos):
    global botones_asientos
    botones_asientos = {}
    for i in range(4):
        for j in range(4):
            estado_asiento = "dark turquoise" if asientos_disponibles[pelicula_seleccionada][i][j] else "red"
            botones_asientos[(i, j)] = tk.Button(frame_asientos, text=f"{i*4+j+1}", width=10, height=3, 
                                                  command=lambda i=i, j=j, pelicula=pelicula_seleccionada: seleccionar_asiento(i, j, pelicula),
                                                  bg=estado_asiento)
            botones_asientos[(i, j)].grid(row=i, column=j)
#Esta parte La creo AlanOGodoy
# Función para manejar la selección de asientos
def seleccionar_asiento(i, j, pelicula):
    asiento_num = i * 4 + j + 1
    if asientos_disponibles[pelicula][i][j]:
        if asiento_num not in seleccionados[pelicula]:
            seleccionados[pelicula].append(asiento_num)#Esta parte La creo AlanOGodoy
            botones_asientos[(i, j)].config(bg="red")  # Asiento seleccionado en rojo
        else:
            seleccionados[pelicula].remove(asiento_num)#Esta parte La creo AlanOGodoy
            botones_asientos[(i, j)].config(bg="dark turquoise")  # Asiento deseleccionado, vuelve a verde
    else:
        messagebox.showwarning("Asiento Ocupado", f"El asiento {asiento_num} ya está ocupado.")
#Esta parte La creo Adrian

# Función que abre la ventana de selección de asientos para una película
def abrir_ventana_seleccion(pelicula_seleccionada):
    global seleccionados
    seleccionados = {pelicula: [] for pelicula in asientos_disponibles}  
    #Esta parte La creo Adrian

    # Resetear los asientos seleccionados
    ventana_seleccion_asientos = tk.Toplevel(ventana)
    ventana_seleccion_asientos.title(f"Seleccionar Asientos - {pelicula_seleccionada}")

    frame_asientos = tk.Frame(ventana_seleccion_asientos)
    frame_asientos.pack()

    actualizar_asientos(pelicula_seleccionada, frame_asientos)
    #Esta parte La creo Adrian

    # Botón para vender boletos
    boton_vender = tk.Button(ventana_seleccion_asientos, text="Vender Boletos", 
                             command=lambda: vender_boleto(pelicula_seleccionada, seleccionados[pelicula_seleccionada], ventana_seleccion_asientos))
    boton_vender.pack()
#Esta parte La creo Adrian

# Función para cambiar la película seleccionada y actualizar la vista
def cambiar_funcion(*args):
    pelicula_seleccionada = pelicula_var.get()
    abrir_ventana_seleccion(pelicula_seleccionada)
#Esta parte La creo Adrian

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Venta de Boletos - Sala VIP")
#Esta parte La creo Adrian

# Título principal
titulo_label = tk.Label(ventana, text="Bienvenidos a Cinegga", font=("Arial", 24, "bold"))
titulo_label.pack(pady=10)
#Esta parte La creo Adrian

# Selector de película
pelicula_var = tk.StringVar(value=peliculas[0]['nombre'])
pelicula_menu = tk.OptionMenu(ventana, pelicula_var, *[p['nombre'] for p in peliculas], command=cambiar_funcion)
pelicula_menu.pack()
#Esta parte La creo AlanOGodoy

# Selector de nombre del cliente
nombre_cliente_label = tk.Label(ventana, text="Nombre del Cliente (Opcional):")
nombre_cliente_label.pack()
nombre_cliente_entry = tk.Entry(ventana)
nombre_cliente_entry.pack()
#Esta parte La creo Adrian

# Botón para mostrar reporte general
reporte_button = tk.Button(ventana, text="Reporte General", command=mostrar_reporte_general)
reporte_button.pack()
#Esta parte La creo AlanOGodoy

# Botones para mostrar el reporte de cada función
for pelicula in peliculas:
    boton_reporte_funcion = tk.Button(ventana, text=f"Reporte {pelicula['nombre']}", 
                                      command=lambda p=pelicula['nombre']: mostrar_reporte_funcion(p))
    boton_reporte_funcion.pack()
#Esta parte La creo AlanOGodoy

# Iniciar la ventana principal
ventana.mainloop()