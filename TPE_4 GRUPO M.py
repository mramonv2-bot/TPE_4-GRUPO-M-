import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time

class SimuladorContextoRealUNEMI:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE SIMULACIÓN DE SEÑALES U3 - UNEMI")
        self.root.state('zoomed') 
        self.root.configure(bg="#0d0e12") 
        
        self.detalles_reales = [
            {
                "ejemplo": "WHATSAPP (WI-FI)",
                "explicacion": "Los bits de tu mensaje se modulan en ondas de radio de 2.4GHz. Aquí aplicas el Subtema 1: Datos digitales viajando en señales analógicas.",
                "teoria": "Teorema de Nyquist: Define la tasa máxima de bits en el aire."
            },
            {
                "ejemplo": "NETFLIX (FIBRA ÓPTICA)",
                "explicacion": "La luz se enciende y apaga (bits) para viajar por el vidrio. Es una señal periódica (Subtema 2) de altísima frecuencia.",
                "teoria": "Ancho de Banda: Es masivo, permitiendo video en 4K sin retrasos."
            },
            {
                "ejemplo": "LLAMADA CELULAR",
                "explicacion": "Tu voz (analógica) se digitaliza para procesarse y luego vuelve a ser onda para salir por la antena.",
                "teoria": "Relación Señal/Ruido (SNR): Si hay interferencia, la calidad de voz baja."
            },
            {
                "ejemplo": "CONTROL DE TV (INFRARROJO)",
                "explicacion": "Pulsas un botón (dato discreto) y un LED emite ráfagas de luz invisible que el TV interpreta.",
                "teoria": "Codificación: Cada botón tiene una secuencia de bits única."
            },
            {
                "ejemplo": "TRANSACCIÓN CAJERO (ATM)",
                "explicacion": "Tus datos bancarios viajan encriptados por cables de cobre usando módems DSL.",
                "teoria": "Ciberseguridad: Como dice el PDF, es una vulnerabilidad compartida en redes públicas."
            }
        ]

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1) 

        header = tk.Frame(root, bg="#161920", height=70, bd=1, relief=tk.SOLID, padx=20)
        header.grid(row=0, column=0, sticky="ew")
        header.pack_propagate(False)
        
        title_frame = tk.Frame(header, bg="#161920")
        title_frame.pack(side=tk.LEFT, fill=tk.Y, pady=5)
        tk.Label(title_frame, text="UNIVERSIDAD ESTATAL DE MILAGRO", font=("Segoe UI", 12, "bold"), bg="#161920", fg="#4f83cc").pack(anchor=tk.W)
        tk.Label(title_frame, text="Materia: Comunicación de Datos | Unidad 3", font=("Segoe UI", 9), bg="#161920", fg="#8f9bb3").pack(anchor=tk.W)
        
        docente_frame = tk.Frame(header, bg="#161920")
        docente_frame.pack(side=tk.RIGHT, fill=tk.Y, pady=10)
        tk.Label(docente_frame, text="DOCENTE:", font=("Segoe UI", 8, "bold"), bg="#161920", fg="#626a7a").pack(anchor=tk.E)
        tk.Label(docente_frame, text="Ing. Alex Armando Ávila Coello, Mgtr.", font=("Segoe UI", 10, "italic"), bg="#161920", fg="#ffffff").pack(anchor=tk.E)

        body_frame = tk.Frame(root, bg="#0d0e12", padx=15, pady=10)
        body_frame.grid(row=1, column=0, sticky="nsew")
        
        body_frame.columnconfigure(0, weight=1)  
        body_frame.columnconfigure(1, weight=3)  
        body_frame.columnconfigure(2, weight=2)  
        body_frame.rowconfigure(0, weight=1)

        left_panel = tk.Frame(body_frame, bg="#161920", bd=1, relief=tk.SOLID, padx=15, pady=15)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        tk.Label(left_panel, text="PANEL DE CONTROL", font=("Segoe UI", 10, "bold"), bg="#161920", fg="#ffffff").pack(anchor=tk.W, pady=(0, 15))
        
        tk.Label(left_panel, text="Cadena de Datos (Texto/Mensaje):", font=("Segoe UI", 9), bg="#161920", fg="#8f9bb3").pack(anchor=tk.W)
        self.entry_msg = tk.Entry(left_panel, font=("Segoe UI", 11), bg="#1f232e", fg="#ffffff", insertbackground="white", bd=1, relief=tk.SOLID, justify="center")
        self.entry_msg.pack(fill=tk.X, pady=(5, 15), ipady=5)
        self.entry_msg.insert(0, "UNEMI")

        self.btn_tx = tk.Button(left_panel, text="⚡ INICIAR TRANSMISIÓN", command=self.transmitir, bg="#2e3b52", fg="#33b1ff", activebackground="#3d4e6d", activeforeground="#33b1ff", font=("Segoe UI", 9, "bold"), bd=1, relief=tk.RAISED, cursor="hand2")
        self.btn_tx.pack(fill=tk.X, pady=4, ipady=6)
        
        self.btn_reset = tk.Button(left_panel, text="🔄 REINICIAR SISTEMA", command=self.reset, bg="#262930", fg="#ff4d4d", activebackground="#333740", activeforeground="#ff4d4d", font=("Segoe UI", 9), bd=1, relief=tk.RAISED, cursor="hand2")
        self.btn_reset.pack(fill=tk.X, pady=4, ipady=6)

        separator = tk.Frame(left_panel, bg="#262930", height=2)
        separator.pack(fill=tk.X, pady=25)

        tk.Label(left_panel, text="EQUIPO DE DESARROLLO:", font=("Segoe UI", 9, "bold"), bg="#161920", fg="#4f83cc").pack(anchor=tk.W, pady=(0, 5))
        
        autores_texto = (
            "• CALDERON RAMON A. I.\n"
            "• FRANCO ECHEVERRIA J. R.\n"
            "• ORTEGA TAZA W. J.\n"
            "• RAMON VALIENTE M. F.\n"
            "• REYES QUIJIJE R. A.\n"
            "• VALAREZO RUÍZ G. C.\n"
            "• VILLAMAR SUÁREZ J. L."
        )
        tk.Label(left_panel, text=autores_texto, font=("Consolas", 9), bg="#161920", fg="#a6b1c2", justify=tk.LEFT, anchor=tk.W).pack(fill=tk.X)

        center_panel = tk.Frame(body_frame, bg="#161920", bd=1, relief=tk.SOLID, padx=10, pady=10)
        center_panel.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        tk.Label(center_panel, text="ANÁLISIS DE SEÑAL EN TIEMPO REAL (OSCILOSCOPIO)", font=("Segoe UI", 10, "bold"), bg="#161920", fg="#ffffff").pack(anchor=tk.W, pady=(0, 10))

        self.fig, (self.ax_dig, self.ax_ana) = plt.subplots(2, 1, figsize=(5, 4))
        self.fig.patch.set_facecolor('#161920')
        self.fig.subplots_adjust(hspace=0.45, left=0.08, right=0.96, top=0.92, bottom=0.08)
        
        for ax in [self.ax_dig, self.ax_ana]:
            ax.set_facecolor('#0d0e12')
            ax.tick_params(colors='#525f73', labelsize=8)
            ax.grid(True, color="#1f232e", linestyle="-", linewidth=0.7)
            ax.title.set_color('#ffffff')
            ax.title.set_fontsize(9)
            ax.title.set_weight('bold')

        self.canvas = FigureCanvasTkAgg(self.fig, master=center_panel)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        right_panel = tk.Frame(body_frame, bg="#161920", bd=1, relief=tk.SOLID, padx=15, pady=10)
        right_panel.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        
        tk.Label(right_panel, text="TELEMETRÍA Y LOGS DE PROCESAMIENTO", font=("Segoe UI", 10, "bold"), bg="#161920", fg="#ffffff").pack(anchor=tk.W, pady=(0, 10))

        self.consola = tk.Text(right_panel, bg="#0d0e12", fg="#cbd5e1", font=("Consolas", 9), padx=12, pady=12, bd=0, wrap=tk.WORD)
        self.consola.pack(fill=tk.BOTH, expand=True)
        
        self.consola.tag_config("ESCENARIO", fg="#33b1ff", font=("Consolas", 9, "bold"))
        self.consola.tag_config("APLICACIÓN", fg="#e2e8f0")
        self.consola.tag_config("TEORÍA", fg="#ffaa00", font=("Consolas", 9, "italic"))
        self.consola.tag_config("SISTEMA", fg="#00e676", font=("Consolas", 9, "bold"))

        footer_status = tk.Frame(root, bg="#1f232e", height=25, bd=1, relief=tk.SOLID, padx=15)
        footer_status.grid(row=2, column=0, sticky="ew")
        footer_status.pack_propagate(False)
        
        info_txt = "Estado: Listo | Modelo Teórico: Teorema de Nyquist [ C = 2 * B * log2(L) ] | Capa Física Redes UNEMI"
        tk.Label(footer_status, text=info_txt, font=("Segoe UI", 8), bg="#1f232e", fg="#a6b1c2").pack(side=tk.LEFT)
        tk.Label(footer_status, text="PROYECTO INTEGRADOR V1.2", font=("Segoe UI", 8, "bold"), bg="#1f232e", fg="#4f83cc").pack(side=tk.RIGHT)

    def log_avanzado(self, tipo, msg):
        if tipo in ["ESCENARIO", "TEORÍA U3", "SISTEMA"]:
            tag_name = "TEORÍA" if tipo == "TEORÍA U3" else tipo
            self.consola.insert(tk.END, f"[{tipo}] ", tag_name)
            self.consola.insert(tk.END, f"{msg}\n")
        else:
            self.consola.insert(tk.END, f"[INFO] {msg}\n", "APLICACIÓN")
        self.consola.see(tk.END)
        self.root.update()

    def reset(self):
        self.ax_dig.clear()
        self.ax_ana.clear()
        for ax in [self.ax_dig, self.ax_ana]:
            ax.grid(True, color="#1f232e", linestyle="-", linewidth=0.7)
        self.canvas.draw()
        self.consola.delete(1.0, tk.END)
        self.btn_tx.config(state=tk.NORMAL)

    def transmitir(self):
        texto = self.entry_msg.get().strip()
        
        if not texto:
            messagebox.showwarning("Validación de Entrada", "El campo de texto no puede estar vacío. Por favor, ingrese un mensaje.")
            return
            
        if not texto.isalnum() and not " " in texto:
            messagebox.showwarning("Validación de Entrada", "El sistema sólo acepta caracteres alfanuméricos (Letras y Números).")
            return

        texto_procesar = texto.upper()
        self.btn_tx.config(state=tk.DISABLED)
        self.consola.delete(1.0, tk.END)
        
        for i, letra in enumerate(texto_procesar):
            self.ax_dig.clear()
            self.ax_ana.clear()
            
            self.ax_dig.grid(True, color="#1f232e", linestyle="-", linewidth=0.7)
            self.ax_ana.grid(True, color="#1f232e", linestyle="-", linewidth=0.7)
            
            bits = [int(b) for b in format(ord(letra), '08b')]
            self.ax_dig.step(range(len(bits)), bits, where='post', color='#33b1ff', lw=2) # Azul Eléctrico
            self.ax_dig.set_title(f"DOMINIO DIGITAL: Carácter '{letra}' procesado en CPU")
            self.ax_dig.set_ylim(-0.2, 1.2)

            t = np.linspace(0, len(bits), 1000)
            frecuencia = 5 
            senal = np.sin(2 * np.pi * frecuencia * t) * np.repeat(bits, 1000 // len(bits))
            self.ax_ana.plot(t, senal, color='#ffaa00', lw=1.2) # Ámbar/Naranja de instrumentación
            self.ax_ana.set_title(f"MEDIO FÍSICO: Onda Analógica transportando '{letra}'")
            
            self.canvas.draw()
            
            detalle = self.detalles_reales[i % len(self.detalles_reales)]
            self.log_avanzado("ESCENARIO", detalle['ejemplo'])
            self.log_avanzado("APLICACIÓN", detalle['explicacion'])
            self.log_avanzado("TEORÍA U3", detalle['teoria'])
            self.consola.insert(tk.END, "—"*50 + "\n")
            
            time.sleep(2.0)

        self.log_avanzado("SISTEMA", f"Mensaje '{texto_procesar}' recibido de forma íntegra.")
        self.btn_tx.config(state=tk.NORMAL)
        
        messagebox.showinfo("Transmisión Exitosa", f"El proceso ha culminado con éxito.\n\nMensaje enviado: {texto_procesar}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorContextoRealUNEMI(root)
    root.mainloop()