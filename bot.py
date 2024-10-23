from botcity.web import WebBot, Browser
import time

class Bot(WebBot):
    def action(self, execution=None):
        # Abrir a aplicação GUI
        self.execute("python3", "main.py")
        
        # Esperar a aplicação abrir
        time.sleep(2)

        # Preencher dados do veículo
        veiculos = [
            {"nome": "Fusca", "ano": "1970", "valor_diario": "100", "tipo_combustivel": "Gasolina", "cilindrada": "1300"},
            {"nome": "Civic", "ano": "2020", "valor_diario": "150", "tipo_combustivel": "Álcool", "cilindrada": "1600"}
        ]

        for veiculo in veiculos:
            self.find("input_nome", matching=0.97)
            self.click()
            self.paste(veiculo["nome"])  # Nome do veículo
            
            self.find("input_ano", matching=0.97)
            self.click()
            self.paste(veiculo["ano"])  # Ano do veículo
            
            self.find("input_valor_diario", matching=0.97)
            self.click()
            self.paste(veiculo["valor_diario"])  # Valor diário
            
            self.find("select_combustivel", matching=0.97)
            self.click()
            self.paste(veiculo["tipo_combustivel"])  # Tipo de combustível
            
            self.find("input_cilindrada", matching=0.97)
            self.click()
            self.paste(veiculo["cilindrada"])  # Cilindrada
            
            self.find("btn_adicionar", matching=0.97)
            self.click()  # Clicar no botão Adicionar Veículo

            time.sleep(1)  # Pausar para garantir que o veículo seja adicionado

        # Calcular aluguel
        self.find("btn_calcular", matching=0.97)
        self.click()  # Clicar no botão Calcular Aluguel

    def not_found(self, label):
        print(f"Elemento {label} não encontrado.")
