'''
Tetris game + a billion comments
http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/
6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
assignments/MIT6_189IAP11_final_proj.pdf
'''


from graphics import *
import random

############################################################
# BLOCK CLASS
############################################################

class Block(Rectangle):
    ''' Block class:
        Implement a block for a tetris piece
        Attributes: x - type: int
                    y - type: int
        specify the position on the tetris board
        in terms of the square grid
    '''

    BLOCK_SIZE = 30
    OUTLINE_WIDTH = 2

    def __init__(self, pos, color):
        self.x = pos.x
        self.y = pos.y
        #When I instantiate a Block, I am going to give it a Point and a color.
        #self.x is going to be the Point's x-value
        #self.y is going to be the Point's y-value
        #Whenever I want a block's x and y points, I will call myblock.x
        #and myblock.y
        

        p1 = Point(pos.x*Block.BLOCK_SIZE + Block.OUTLINE_WIDTH,
                   pos.y*Block.BLOCK_SIZE + Block.OUTLINE_WIDTH)
        p2 = Point(p1.x + Block.BLOCK_SIZE, p1.y + Block.BLOCK_SIZE) 
        #Because the Rectangle class needs to be fed two corners
        #to be instantiated (see instantiation below), we need to
        #mark those two corners as p1 and p2, but also multiply them by BLOCK_SIZE
        #to convert from pixels to blocks. 

        Rectangle.__init__(self, p1, p2)
        #A Block is a special tyep of Rectangle
        #use this format to call the parent class Rectangle
        
        self.setWidth(Block.OUTLINE_WIDTH)
        self.setFill(color)
        #these are methods of the parent class but we'll
        #label as "self" since Block inherited Rectangle

    def can_move(self, board, dx, dy): #Block.can_move
        ''' Parameters: dx - type: int
                        dy - type: int

            Return value: type: bool
                        
            checks if the block can move dx squares in the x direction
            and dy squares in the y direction
            Returns True if it can, and False otherwise
            HINT: use the can_move method on the Board object
        '''
        return board.can_move(self.x+dx, self.y+dy)

        #board.can_move checks if its parameters are within BOARD_WIDTH
        #and BOARD_HEIGHT
        
    
    def move(self, dx, dy):
        ''' Parameters: dx - type: int
                        dy - type: int
                        
            moves the block dx squares in the x direction
            and dy squares in the y direction
        '''

        self.x += dx
        self.y += dy
        #in other words, self.x = self.x + dx

        Rectangle.move(self, dx*Block.BLOCK_SIZE, dy*Block.BLOCK_SIZE)

############################################################
# SHAPE CLASS
############################################################

class Shape():
    ''' Shape class:
        Base class for all the tetris shapes
        Attributes: blocks - type: list - the list of blocks making up the shape
                    rotation_dir - type: int - the current rotation direction of the shape
                    shift_rotation_dir - type: Boolean - whether or not the shape rotates
    '''

    def __init__(self, coords, color):
        self.blocks = []
        #list of blocks (will be used to compose shapes)
        self.rotation_dir = 1
        ### A boolean to indicate if a shape shifts rotation direction or not.
        ### Defaults to false since only 3 shapes shift rotation directions (I, S and Z)
        self.shift_rotation_dir = False
        
        
        for pos in coords:
            self.blocks.append(Block(pos, color))
        #for coordinate in the list of coordinates provided
        #by the individual shape classes, create a block at that coordinate


    def get_blocks(self):
        '''returns the list of blocks
        '''
        return self.blocks
    
        

    def draw(self, win):
        ''' Parameter: win - type: CanvasFrame

            Draws the shape:
            i.e. draws each block
        ''' 
        for block in self.blocks:
            block.draw(win)

    def move(self, dx, dy):
        ''' Parameters: dx - type: int
                        dy - type: int

            moves the shape dx squares in the x direction
            and dy squares in the y direction, i.e.
            moves each of the blocks
        '''
        for block in self.blocks:
            block.move(dx, dy)

    def can_move(self, board, dx, dy): # Shape.can_move
        ''' Parameters: dx - type: int
                        dy - type: int

            Return value: type: bool
                        
            checks if the shape can move dx squares in the x direction
            and dy squares in the y direction, i.e.
            check if each of the blocks can move
            Returns True if all of them can, and False otherwise
           
        '''
        
        for block in self.blocks: # check if all blocks in shape can move
            if block.can_move(board, dx, dy) == False:
                return False
        return True
        #####**********### INDENT: dear janey plz stop making this mistake

        
    def get_rotation_dir(self):
        ''' Return value: type: int
        
            returns the current rotation direction
        '''
        return self.rotation_dir

    def can_rotate(self, board):
        ''' Parameters: board - type: Board object
            Return value: type : bool
            
            Checks if the shape can be rotated.
            
            1. Get the rotation direction using the get_rotation_dir method
            2. Compute the position of each block after rotation and check if
            the new position is valid
            3. If any of the blocks cannot be moved to their new position,
            return False
                        
            otherwise all is good, return True
        '''
        
        rot_dir = self.get_rotation_dir()
        #self.get_rotation_dir() is set as 1
        
        center = self.center_block
        #self.center_block comes from the individual shape classes
        #that inherit from Shape

        for block in self.blocks:

            x = center.x - rot_dir*center.y + rot_dir*block.y

            y = center.y + rot_dir*center.x - rot_dir*block.x
            #formula for new coordinates if block is rotated
            #90 deg around another blocks
            
            if board.can_move(x, y) == False:
                return False
        return True

        



    def rotate(self, board):
        ''' Parameters: board - type: Board object

            rotates the shape:
            1. Get the rotation direction using the get_rotation_dir method
            2. Compute the position of each block after rotation
            3. Move the block to the new position
            
        '''    
        rot_dir = self.get_rotation_dir()
        center = self.center_block
        if self.can_rotate(board) == True:
            for block in self.blocks:
                    block.move(center.x - rot_dir*center.y + rot_dir*block.y - block.x, center.y + rot_dir*center.x - rot_dir*block.x - block.y)



        ### This should be at the END of your rotate code. 
        ### DO NOT touch it. Default behavior is that a piece will only shift
        ### rotation direciton after a successful rotation. This ensures that 
        ### pieces which switch rotations definitely remain within their 
        ### accepted rotation positions.
        if self.shift_rotation_dir:
            self.rotation_dir *= -1

        

############################################################
# ALL SHAPE CLASSES
############################################################

 
class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, 'blue')
        self.shift_rotation_dir = True
        self.center_block = self.blocks[2]

class J_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, 'orange')        
        self.center_block = self.blocks[1]

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'cyan')        
        self.center_block = self.blocks[1]


class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x    , center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x   , center.y + 1),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'red')
        self.center_block = self.blocks[0]

    def rotate(self, board):
        # Override Shape's rotate method since O_Shape does not rotate
        return 

class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'green')
        self.center_block = self.blocks[0]
        self.shift_rotation_dir = True
        self.rotation_dir = -1


class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x    , center.y + 1)]
        Shape.__init__(self, coords, 'yellow')
        self.center_block = self.blocks[1]


class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y), 
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, 'magenta')
        self.center_block = self.blocks[1]
        self.shift_rotation_dir = True
        self.rotation_dir = -1      



############################################################
# BOARD CLASS
############################################################

class Board():
    ''' Board class: it represents the Tetris board

        Attributes: width - type:int - width of the board in squares
                    height - type:int - height of the board in squares
                    canvas - type:CanvasFrame - where the pieces will be drawn
                    grid - type:Dictionary - keeps track of the current state of
                    the board; stores the blocks for a given position
    '''
    
    def __init__(self, win, width, height):
        self.width = width
        self.height = height

        # create a canvas to draw the tetris shapes on
        self.canvas = CanvasFrame(win, self.width * Block.BLOCK_SIZE,
                                        self.height * Block.BLOCK_SIZE)
        self.canvas.setBackground('light gray')

        # create an empty dictionary
        # currently we have no shapes on the board
        self.grid = {}

    def draw_shape(self, shape):
        ''' Parameters: shape - type: Shape
            Return value: type: bool

            draws the shape on the board if there is space for it
            and returns True, otherwise it returns False
        '''
        if shape.can_move(self, 0, 0):
            shape.draw(self.canvas)
            return True
        return False

    def can_move(self, x, y): #Board.can_move
        ''' Parameters: x - type:int
                        y - type:int
            Return value: type: bool

            1. check if it is ok to move to square x,y
            if the position is outside of the board boundaries, can't move there
            return False


            2. if there is already a block at that postion, can't move there
            return False

            3. otherwise return True
            
        '''

        if x in range(Tetris.BOARD_WIDTH) and y in range(Tetris.BOARD_HEIGHT) and (x,y) not in self.grid.keys():
            return True
        else:
            return False


      
    def add_shape(self, shape):
        ''' Parameter: shape - type:Shape
            
            add a shape to the grid, i.e.
            add each block to the grid using its
            (x, y) coordinates as a dictionary key

            Hint: use the get_blocks method on Shape to
            get the list of blocks
            
        '''
        for block in shape.get_blocks(): # returns list of blocks in the shape
            self.grid[block.x,block.y] = block


    def delete_row(self, y):
        ''' Parameters: y - type:int

            remove all the blocks in row y
            to remove a block you must remove it from the grid
            and erase it from the screen.
            If you dont remember how to erase a graphics object
            from the screen, take a look at the Graphics Library
            handout
            
        '''
        for x in range(self.width):
            block = self.grid[x,y]
            #assigning 'block' to be the block oN THE BOARD
            #whose dictionary entry i'm bout to delete
            
            del self.grid[x,y]
            #delete that block IN THE DICTIONARY 
            #(but it still exists so now we can undraw it below)
            
            block.undraw()
            #if you write self.grid[x,y].undraw()
            #you'll get a KeyError because you just deleted
            #that key
            ###THAT'S WHY WE ASSIGNED NEW variable 'block'
            
            

    
    def is_row_complete(self, y):        
        ''' Parameter: y - type: int
            Return value: type: bool

            for each block in row y
            check if there is a block in the grid (use the in operator) 
            if there is one square that is not occupied, return False
            otherwise return True
            
        '''
        
        for x in range(self.width):
            if (x,y) not in self.grid:
                return False
        return True #this must be outside if statement. if it is in the 
        #if statement, it returns True *for each block*. we only need ONE 
        #True for the entire function that says if the row is complete

    def move_down_rows(self, y_start):
        ''' Parameters: y_start - type:int                        

            for each row from y_start to the top
                for each column
                    check if there is a block in the grid
                    if there is, remove it from the grid
                    and move the block object down on the screen
                    and then place it back in the grid in the new position

        '''
        
        for y in reversed(range(y_start + 1)):
            for x in range(self.width):
                if (x,y) in self.grid:
                    block = self.grid[x,y]
                    #'block'is a NEW BLOCK at position x,y
                    
                    del self.grid[x,y]
                    #here we delete the block IN THE GRID
                    
                    block.move(0,1)
                    #here we move the block ON THE BOARD
                    
                    self.grid[x,y+1] = block
                    #here we place the block that was previously ONLY
                    #ON THE BOARD in the GRID


    def remove_complete_rows(self):
        ''' removes all the complete rows
            1. for each row, y, 
            2. check if the row is complete
                if it is,
                    delete the row
                    move all rows down starting at row y - 1

        '''
        
        for y in range(self.height):
            if self.is_row_complete(y):
                self.delete_row(y)
                self.move_down_rows(y-1)

    def game_over(self):
        ''' display "Game Over !!!" message in the center of the board
            HINT: use the Text class from the graphics library
        '''
        
        new_win = GraphWin("Game Over", 300, 100) 
        msg1 = Text(Point(150,50), "Gurl yo game is ovah") 
        msg1.setSize(20)
        msg1.setTextColor("red")
        msg1.draw(new_win)
        new_win.mainloop()  


############################################################
# TETRIS CLASS
############################################################

class Tetris():
    ''' Tetris class: Controls the game play
        Attributes:
            SHAPES - type: list (list of Shape classes)
            DIRECTION - type: dictionary - converts string direction to (dx, dy)
            BOARD_WIDTH - type:int - the width of the board
            BOARD_HEIGHT - type:int - the height of the board
            board - type:Board - the tetris board
            win - type:Window - the window for the tetris game
            delay - type:int - the speed in milliseconds for moving the shapes
            current_shapes - type: Shape - the current moving shape on the board
    '''
    
    SHAPES = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
    DIRECTION = {'Left':(-1, 0), 'Right':(1, 0), 'Down':(0, 1)}
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20
    
    def __init__(self, win):
        self.board = Board(win, self.BOARD_WIDTH, self.BOARD_HEIGHT)
        self.win = win
        self.delay = 100 #ms

        # sets up the keyboard events
        # when a key is called the method key_pressed will be called
        self.win.bind_all('<Key>', self.key_pressed)

        # set the current shape to a random new shape
        self.current_shape = self.create_new_shape()

        # Draw the current_shape on the board (take a look at the
        # draw_shape method in the Board class) 
        self.board.draw_shape(self.current_shape)

        # For Step 9:  animate the shape!
        self.win.after(self.delay, self.animate_shape())


    def create_new_shape(self):
        random_shape = self.SHAPES[random.randint(0,6)] #any of the above shapes
        #check how those shapes are implemented
        #ie. I_shape(CENTER)
        return random_shape(Point((int(self.BOARD_WIDTH/2)), 0))



        ''' Return value: type: Shape
            
            Create a random new shape that is centered
             at y = 0 and x = int(self.BOARD_WIDTH/2)
            return the shape
        '''
    
    def animate_shape(self):
        ''' animate the shape - move down at equal intervals
            specified by the delay attribute
        '''
        
        self.do_move('Down')
        self.win.after(self.delay, self.animate_shape)
    
    def do_move(self, direction):
        ''' Parameters: direction - type: string
            Return value: type: bool

            Move the current shape in the direction specified by the parameter:
            First check if the shape can move. If it can, move it and return True

            Otherwise if the direction we tried to move was 'Down',
            1. add the current shape to the board
            2. remove the completed rows if any 
            3. create a new random shape and set current_shape attribute
            4. If the shape cannot be drawn on the board, display a
               game over message

            return False

        '''
        (dx,dy) = Tetris.DIRECTION[direction]
        if self.current_shape.can_move(self.board, dx, dy) == True:
            self.current_shape.move(dx, dy)
            return True
        elif self.current_shape.can_move(self.board,dx,dy) == False:
            if direction == 'Down':
                self.board.add_shape(self.current_shape)
                self.board.remove_complete_rows()
                self.current_shape = self.create_new_shape()
                if self.board.draw_shape(self.current_shape) == False:
                    self.board.game_over()
            return False

        

    def do_rotate(self):
        ''' Checks if the current_shape can be rotated and
            rotates if it can
        '''
        
        if self.current_shape.can_rotate(self.board): 
            self.current_shape.rotate(self.board)
    
    def key_pressed(self, event):
        ''' this function is called when a key is pressed on the keyboard
            it currenly just prints the value of the key

            Modify the function so that if the user presses the arrow keys
            'Left', 'Right' or 'Down', the current_shape will move in
            the appropriate direction

            if the user presses the space bar 'space', the shape will move
            down until it can no longer move and is added to the board

            if the user presses the 'Up' arrow key ,
                the shape should rotate.

        '''
        key = event.keysym
        if key in Tetris.DIRECTION:
            self.do_move(key)

        if key == "space":
            for block in self.current_shape.get_blocks():
                while self.current_shape.can_move(self.board,0,1):
                    self.current_shape.move(0,1)
            self.do_move("Down")


        if key == "Up":
            self.do_rotate()



       
################################################################
# Start the game
################################################################

win = Window("Tetris")
game = Tetris(win)
win.mainloop()

