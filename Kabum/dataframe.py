# Import the libs for use 
import pandas as pd


class DataFrame:
    
    def __init__(self) -> None:
        self.create_dataframe()
    
    
    def create_dataframe(self):
        self.data = pd.read_excel("C:\\Users\\Alan\\Desktop\\Projetos GIT pessoal\\Project-Kabum\\Kabum\\Produtos.xlsx")
        dt = pd.DataFrame(self.data)
        print(dt.head(10))
        
        

DataFrame()