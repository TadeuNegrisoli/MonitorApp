# 🌐 MonitorApp

O **MonitorApp** é um aplicativo para desktop simples e direto, criado em Python. A ideia principal é monitorar o status de vários sites ao mesmo tempo e avisar você imediatamente se algum deles cair ou deixar de responder.

## Funcionalidades

* **Dashboard:** Uma interface visual e moderna, construída com CustomTkinter, onde você pode ver rapidamente o status de todos os sites que adicionou.
* **Avisos:** O programa se comunica diretamente com as notificações do Windows (através do `winotify`). Se um site cair, você verá um pop-up e ouvirá um alerta sonoro na hora.
* **Motor:** Graças ao uso de *threading*, o programa faz as verificações em segundo plano. Isso significa que cada site é testado no seu próprio tempo, sem travar ou deixar a interface lenta.
* **Logs:** Tudo o que dá errado fica registrado. Você pode consultar o histórico de falhas e criar arquivos de backup de forma muito simples, com apenas um clique.

## Linguagem e Bibliotecas

* **Python 3.x**
* **CustomTkinter:** Responsável por dar ao aplicativo um visual limpo e atual.
* **Requests:** O motor que vai até a internet confirmar se os seus sites estão realmente no ar.
* **Winotify:** A ponte que permite ao programa enviar os avisos diretamente para a sua tela do Windows.

## Como Instalar e Executar

A ideia é que você não perca tempo com configurações complicadas.

1. **Baixe o projeto:**
   ```bash
   git clone [https://github.com/TadeuNegrisoli/MonitorApp.git](https://github.com/TadeuNegrisoli/MonitorApp.git)
   ```

2. **Instale o que é necessário:**
   Abra a pasta onde salvou o projeto e dê um duplo clique no arquivo `install_dependencies.bat`. Ele é encarregado de instalar todas as bibliotecas para você, de forma automática.

3. **Inicie o aplicativo:**
   Para abrir o programa, você só precisa dar um duplo clique no arquivo `MonitorApp.pyw` (caso o seu Python já esteja configurado para abrir esse tipo de arquivo) ou abrir o terminal e digitar:
   ```bash
   pythonw MonitorApp.pyw
   ```
   *(Nota: Usar arquivos `.pyw` é excelente porque o aplicativo roda de forma silenciosa, sem deixar aquela janela preta do terminal aberta atrapalhando).*

## Estrutura do Projeto

Organizei o código em diferentes módulos para que seja fácil de ler, manter e atualizar no futuro. A pasta raiz está limpa e dividida da seguinte forma:

* `/core`: O cérebro do agendamento, que controla quando cada verificação deve acontecer em segundo plano.
* `/database_module`: Onde é feita a leitura e gravação das suas informações no arquivo JSON.
* `/logs_module`: Tudo o que envolve criar e salvar o histórico de erros.
* `/monitor_module`: A parte responsável por testar os sites e disparar o alerta no Windows.
* `MonitorApp.pyw`: A janela e a interface gráfica com a qual você interage.

---
Desenvolvido por [Tadeu Negrisoli](https://github.com/TadeuNegrisoli)
