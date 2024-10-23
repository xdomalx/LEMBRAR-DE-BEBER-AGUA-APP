lembrete_agua.py.


import time
from plyer import notification

def lembrete_beber_agua():
    # Definir o número de lembretes ao longo do dia (5 vezes)
    numero_lembretes = 5

    # Intervalo em segundos entre os lembretes (ex: 2 horas = 7200 segundos)
    intervalo = 7200  # 2 horas

    for lembrete in range(numero_lembretes):
        # Exibir a notificação
        notification.notify(
            title="Lembrete de Hidratação",
            message="É hora de beber água! 🌊",
            timeout=10  # A notificação fica visível por 10 segundos
        )
        
        # Aguardar até o próximo lembrete
        time.sleep(intervalo)

if __name__ == "__main__":
    lembrete_beber_agua()
