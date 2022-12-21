# Import the libs for use 
import pandas as pd


class DataFrame:
    
    def __init__(self) -> None:
        self.create_dataframe()
        self.remove_repeated_values()
        self.selections_and_frequency()
    
    
    def create_dataframe(self):
        self.data = pd.read_excel("C:\\Users\\Alan\\Desktop\\Projetos GIT pessoal\\Project-Kabum\\Kabum\\Produtos.xlsx")
        self.dt = pd.DataFrame(self.data)
        
        
    def remove_repeated_values(self):
        self.dt.drop_duplicates(inplace= True) # Implace serve para salvar as alterações que fizemos no Data Frame.
        
    
    def selections_and_frequency(self):
        # Verificando se há computadores com o valor menor ou igual a 4000
        selection = (self.dt['Valor'] <= 4000)
        # Verificando quantos computadores tem o valor menor ou igual a 4000
        self.value = selection.shape[0]
        

    

DataFrame()