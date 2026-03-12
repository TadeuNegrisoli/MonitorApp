import customtkinter as ctk
from database_module.database import adicionar_site_db, carregar_sites
from logs_module.logs import get_logs, gerar_novo_log
from core.worker import start_worker

class MonitorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MonitorApp"); self.geometry("800x600")
        self.grid_columnconfigure(1, weight=1); self.grid_rowconfigure(0, weight=1)
        self.aba_atual= "dash"
        self.site_labels= {}
        self.sidebar= ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(self.sidebar, text="Monitor", font=("Arial", 20, "bold")).pack(pady=20)
        ctk.CTkButton(self.sidebar, text="Dashboard", command=self.show_dash).pack(pady=10, padx=20)
        ctk.CTkButton(self.sidebar, text="Adicionar", command=self.show_add).pack(pady=10, padx=20)
        ctk.CTkButton(self.sidebar, text="Logs", command=self.show_logs).pack(pady=10, padx=20)
        self.main_frame= ctk.CTkFrame(self, corner_radius=10, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        start_worker(); self.show_dash(); self.loop_refresh()

    def limpar(self):
        self.site_labels.clear()
        [w.destroy() for w in self.main_frame.winfo_children()]

    def loop_refresh(self):
        if self.aba_atual == "dash":
            for s in carregar_sites():
                if s["url"] in self.site_labels:
                    cor= "green" if s["status"] == "Online" else "yellow" if s["status"] == "Conectando" else "red"
                    self.site_labels[s["url"]].configure(text=s["status"], text_color=cor)
        self.after(1000, self.loop_refresh)

    def show_dash(self):
        self.aba_atual= "dash"; self.limpar()
        from database_module.database import remover_site_db
        for s in carregar_sites():
            cor= "green" if s["status"] == "Online" else "yellow" if s["status"] == "Conectando" else "red"
            f= ctk.CTkFrame(self.main_frame); f.pack(fill="x", padx=10, pady=5)
            ctk.CTkLabel(f, text=s['url']).pack(side="left", padx=10)
            ctk.CTkButton(f, text="X", width=30, fg_color="red", command=lambda u=s["url"]: [remover_site_db(u), self.show_dash()]).pack(side="right", padx=5)
            ctk.CTkButton(f, text="Copiar", width=60, command=lambda u=s["url"]: [self.clipboard_clear(), self.clipboard_append(u)]).pack(side="right", padx=5)           
            lbl= ctk.CTkLabel(f, text=s["status"], text_color=cor); lbl.pack(side="right", padx=10)
            self.site_labels[s["url"]]= lbl
        
        self.loader= ctk.CTkProgressBar(self.main_frame, width=200, mode="indeterminate")
        self.loader.pack(side="bottom", pady=20); self.loader.start()

    def show_add(self):
        self.aba_atual= "add"; self.limpar()
        url_e= ctk.CTkEntry(self.main_frame, placeholder_text="URL", width=300); url_e.pack(pady=5)
        time_e= ctk.CTkEntry(self.main_frame, placeholder_text="Segundos", width=300); time_e.pack(pady=5)
        ctk.CTkButton(self.main_frame, text="Salvar", command=lambda: [adicionar_site_db(url_e.get(), time_e.get()), self.show_dash()]).pack(pady=20)

    def show_logs(self):
        self.aba_atual= "logs"; self.limpar()
        txt= ctk.CTkTextbox(self.main_frame, width=500, height=350); txt.pack(pady=10)
        txt.insert("0.0", get_logs())
        ctk.CTkButton(self.main_frame, text="Gerar Novo Log", command=lambda: [gerar_novo_log(), self.show_logs()]).pack(pady=10)

if __name__ == "__main__": MonitorApp().mainloop()