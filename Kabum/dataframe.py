# Import the libs for use 
import pandas as pd


class DataFrame:
    
    def __init__(self) -> None:
        self.create_dataframe()
        self.remove_repeated_values()
        self.selections_and_frequency()
        self.save_new_excel()
    
    
    def create_dataframe(self):
        self.data = pd.read_excel("C:\\Users\\Alan\\Desktop\\Projetos GIT pessoal\\Project-Kabum\\Kabum\\Produtos.xlsx")
        self.dt = pd.DataFrame(self.data)
        
        
    def remove_repeated_values(self):
        self.dt.drop_duplicates(inplace= True) # Implace serve para salvar as alterações que fizemos no Data Frame.
        
    
    def selections_and_frequency(self):
        # Verificando se há computadores com o valor menor ou igual a 4000
        selection = (self.dt['Valor'] <= 4000)
        # Verificando quantos computadores tem o valor menor ou igual a 4000
        self.value = self.dt[selection]
        # Alterando o index do quadro
        self.value.index = range(self.value.shape[0])
        # Mostrando a média de valores
        self.mean_value = self.dt['Valor'].mean().__round__(1)
        # Estatística Descritiva dos valores de pc gamers
        self.est_descr = self.dt['Valor'].describe().round(2)

        
    def save_new_excel(self):
        # Salvando arquivo filtrado
        self.value.to_excel("Kabum/new_excel.xlsx", index= False)
        

DataFrame()