#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Defining tile classes

class AccentTile: 
    def __init__(self, name, position): 
        self.name = name 
        self.position = position


    def apply_ability(self, game_board): pass

class HarmonyTile(AccentTile): 
    def apply_ability(self, game_board): 
        # Example ability: Creates harmony with adjacent tiles 
        for adj_tile in game_board.get_adjacent_tiles(self.position): 
            if adj_tile.is_harmonious(self): adj_tile.boost_harmony()
                
class BlockingTile(AccentTile): 
    def apply_ability(self, game_board): 
        # Example ability: Blocks movement of opponent's pieces 
        for adj_tile in game_board.get_adjacent_tiles(self.position): 
            adj_tile.block_movement()


# In[11]:


#Game board set-up

class GameBoard: 
    def __init__(self, size): 
        self.size = size 
        self.board = [[None for _ in range(size)] for _ in range(size)] 
        
        def place_tile(self, tile, position): 
            x, y = position 
            self.board[x][y] = tile 
            
            def get_adjacent_tiles(self, position): 
                x, y = position 
                adjacent_positions = [ (x-1, y), (x+1, y), (x, y-1), (x, y+1) ] 
                
                return [self.board[pos[0]][pos[1]] for pos in adjacent_positions if self.is_valid_position(pos)] 
            
            def is_valid_position(self, position): 
                x, y = position 
                return 0 <= x < self.size and 0 <= y < self.size


# In[12]:


#Implementing & Integrating tile abilities

class Game: 
    def __init__(self): 
        self.game_board = GameBoard(9) 
        
        def place_accent_tile(self, accent_tile, position): 
            self.game_board.place_tile(accent_tile, position)
            accent_tile.apply_ability(self.game_board) 
            
            # Example usage 
            game = Game() 
            harmony_tile = HarmonyTile("Harmony", (4, 4)) 
            game.place_accent_tile(harmony_tile, (4, 4)) 
            blocking_tile = BlockingTile("Blocking", (3, 3)) 
            game.place_accent_tile(blocking_tile, (3, 3))


# In[ ]:




