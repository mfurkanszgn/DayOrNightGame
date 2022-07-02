from typing import Optional

from games.DayOrNight.action import DayOrNightAction
from games.DayOrNight.result import DayOrNightResult
from games.state import State
from games.DayOrNight.grid import grid
from colorama import Fore, Back, Style

class DayOrNightState(State):
   
    EMPTY_CELL = -1
    
    def __init__(self, num_rows: int = 7, num_cols: int = 7):
        super().__init__()
    
        if num_rows < 4:
            raise Exception("the number of rows must be 4 or over")
        if num_cols < 4:
            raise Exception("the number of cols must be 4 or over")

        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        """
        the grid
        """
        #self.__grid = [[DayOrNightState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]
       
        self.__grid=[[-1,-2,-1,-2,-1,-2,-1,-2,-1,-2,-1],
                     [-2,-1,-2,-1,-2,-1,-2,-1,-2,-1,-2],
                     [-1,-2,-1,-2,-1,-2,-1,-2,-1,-2,-1],
                     [-2,-1,-2,-1,-2,-1,-2,-1,-2,-1,-2],
                     [-1,-2,-1,-2,-1,-2,-1,-2,-1,-2,-1],
                     [-2,-1,-2,-1,-2,-1,-2,-1,-2,-1,-2],
                     [-1,-2,-1,-2,-1,-2,-1,-2,-1,-2,-1],
                     [-2,-1,-2,-1,-2,-1,-2,-1,-2,-1,-2],
                     [-1,-2,-1,-2,-1,-2,-1,-2,-1,-2,-1],
                     [-2,-1,-2,-1,-2,-1,-2,-1,-2,-1,-2],
                     [-1,-2,-1,-2,-1,-2,-1,-2,-1,-2,-1]
                     ]
        
        self.__grid_copy=grid
        
    
        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1
        

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 4):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player and \
                        self.__grid[row][col + 4] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 4):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player and \
                        self.__grid[row + 4][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and  \
                   abs(self.__grid[row][col]-player)==1 and \
                        self.__grid[row - 1][col + 1] == player and \
                        abs( self.__grid[row - 1][col + 1]-player)==1 and \
                        self.__grid[row - 2][col + 2] == player and \
                        abs(  self.__grid[row - 2][col + 2]-player)==1 and \
                        self.__grid[row - 3][col + 3] == player and \
                        abs(  self.__grid[row - 3][col + 3]-player)==1 :
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: DayOrNightAction) -> bool:
            col = action.get_col()
            row= action.get_row()
            
            if row < 0 or row > self.__num_rows:
                
                return False      
            # valid column and row
            if col < 0 or col > self.__num_cols:
                return False
            # full column
           
           
            
            if action.get_moveOrdrop()==2 and self.__grid[row][col]!=-1:
                
                return False
            
            return True


    def update(self, action: DayOrNightAction):
        col = action.get_col()
        row=action.get_row()
        moveORdrop=action.get_moveOrdrop()
        # drop the checker
       
        # if moveORdrop!=2 or moveORdrop!=1:
        #    moveORdrop=2
           
           
        if moveORdrop==2:
            for selectedrow in range(self.__num_rows):
                for selectedcol in range(self.__num_cols):
                    if selectedrow== row and selectedcol==col :
                        if self.__grid[row][col]==-1:  #is it black place(Game rule -1=black ,-2=white)
                            
                            self.__grid[row][col]=self.__acting_player
                            
                            self.__has_winner = self.__check_winner(self.__acting_player)
                            # switch to next player
                            self.__acting_player = 1 if self.__acting_player == 0 else 0
       
                            self.__turns_count += 1
                        else:
                            break
        if moveORdrop==1:
             for selectedrow in range(self.__num_rows):
                for selectedcol in range(self.__num_cols):
                    if selectedrow== row and selectedcol==col :
                        #is square white (Game rule.Move white square always)
                        
                        if self.__grid[row][col]==0 or self.__grid[row][col]==1:
                           
                             #restore square
                             print("Chose new square")
                             new_row=int(input("new row "))
                             new_col=int(input("new col "))
                             self.__grid[row][col]=self.__grid_copy[row][col]
                             if self.__moveControl(row, col, new_row, new_col)==True:
                                 
                                 
                                 self.__grid[new_row][new_col]=self.__acting_player
                                 self.__has_winner = self.__check_winner(self.__acting_player)
                                 self.__acting_player = 1 if self.__acting_player == 0 else 0
                                 # switch to next player
                                 self.__turns_count += 1
                             else:
                                 
                                 self.clone()    
                        else:
                            self.clone()
            
            
            
       
           
        # for row in range(self.__num_rows - 1, -1, -1):
        #     for col in range
        #     if self.__grid[row][col] < 0:
        #         print(self.__grid[row][col])
        #         self.__grid[row][col] = self.__acting_player
        #         break

        # determine if there is a winner

       # print("turns_count 1"+ self.__turns_count)
      
    def __moveControl(self,row,col,new_row,new_col):
        
        if self.__grid[new_row][new_col]==-2: # if square is free
            # if stone on white 
            
            
            if  self.__grid[row][col]== -2  :
                
                if  row - 1 == new_row and col-1 ==new_col:
                    return  True
                elif row - 1 == new_row and col+1 ==new_col:
                    return True
                
                elif row + 1 == new_row and col-1 ==new_col:
                    return True
                elif  row + 1 == new_row and col+1 ==new_col:
                    return True
                else:
                    
                    self.__grid[row][col]=self.__acting_player
                        
                    
            # if stone on black
            if  self.__grid[row][col]==  -1 :
                print("1.adım black")
                if row + 1== new_row and col==new_col:
                    return True
                elif row - 1== new_row and col==new_col:
                    return True
                elif row == new_row and col+1==new_col :
                    return True
                elif row == new_row and col-1==new_col:
                    return True
                else:
                     self.__grid[row][col]=self.__acting_player
                    
                
            else:
                
                return False
                        
                    
                    
                
                
                
            
        else:
            self.__grid[row][col]=self.__acting_player
           
        
                
            
            
            
        
            
            
        
        
    def __display_cell(self, row, col):
        print({
            0:                              Fore.BLUE+'b'+Fore.WHITE,
            1:                              Fore.RED+'w'+Fore.WHITE,
           -1:                              Fore.WHITE+'B'+ Fore.WHITE,
           -2:                              Fore.WHITE+'W'+Fore.WHITE
        }[self.__grid[row][col]], end="")
       

 
    def __display_numbers(self):
       
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("")
        

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
        
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            
            print(row,end="")
            print("")
            self.__display_separator()
        

        self.__display_numbers()
    

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = DayOrNightState(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[DayOrNightResult]:
        if self.__has_winner:
            return DayOrNightResult.LOOSE if pos == self.__acting_player else DayOrNightResult.WIN
        if self.__is_full():
            return DayOrNightResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass


