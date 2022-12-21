# Import the libs for use 
import pandas as pd


class DataFrame:
    
    def __init__(self) -> None:
        self.create_dataframe()
        self.remove_repeated_values()
    
    
    def create_dataframe(self):
        self.data = pd.read_excel("C:\\Users\\Alan\\Desktop\\Projetos GIT pessoal\\Project-Kabum\\Kabum\\Produtos.xlsx")
        self.dt = pd.DataFrame(self.data)
        
        
    def remove_repeated_values(self):
        self.dt.drop_duplicates(inplace= True) # Implace serve para salvar as alterações que fizemos no Data Frame.
        
        
DataFrame()