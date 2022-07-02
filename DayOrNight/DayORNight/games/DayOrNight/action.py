class DayOrNightAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __col: int
    __row: int
    __moveOrdrop:int
 
    def __init__(self, row: int,col:int,moveOrdrop:int=2):
        self.__col = col
        self.__row = row
        self.__moveOrdrop=moveOrdrop
    def set_moveOrdrop(self,option):
        self.moveOrdrop=option
        
        
    def get_col(self):
        return self.__col
    
    def get_row(self):
        return self.__row
    
    def get_moveOrdrop(self):
        return self.__moveOrdrop