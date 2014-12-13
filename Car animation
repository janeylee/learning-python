from graphics import *
 
class Wheel(object):
 
    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, wheel_radius)
 
    def draw(self, win): 
        self.tire_circle.draw(win) 
        self.wheel_circle.draw(win) 
 
    def move(self, dx, dy): 
        self.tire_circle.move(dx, dy) 
        self.wheel_circle.move(dx, dy)
 
    def set_color(self, wheel_color, tire_color):
        self.tire_circle.setFill(tire_color) 
        self.wheel_circle.setFill(wheel_color)
 
    def undraw(self): 
        self.tire_circle .undraw() 
        self.wheel_circle .undraw() 
 
    def get_size(self):
        return self.tire_circle.getRadius()
 
    def get_center(self):
        return self.tire_circle.getCenter()
 
    def animate(self,win,dx,dy,n):
        if n > 0:
            self.move(dx,dy)
            win.after(100, self.animate, win, dx, dy, n-1)
 
 
# Define a main function; if you want to display graphics, run main()
# after you load code into your interpreter
def main():
    # create a window with width = 700 and height = 500
    new_win = GraphWin('Wheel', 700, 500) 
 
    # What we'll need for the wheel...
    wheel_center = Point(200, 200) # The wheel center is a Point at (200, 200)
    tire_radius = 50  # The radius of the outer tire is 100
 
    # Make a wheel object
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)
 
    # Set its color
    new_wheel.set_color('LavenderBlush1', 'PaleTurquoise4')
 
    # And finally, draw it 
    new_wheel.draw(new_win)
 
    new_wheel.animate(new_win,30,20,100)
 
 
    # Run the window loop (must be the *last* line in your code)
new_win.mainloop()
 
----------------
 
 
from graphics import *
from wheel import *
 
# new_win = GraphWin("A Car", 700, 300)
# rect = Rectangle( Point( 10,10), Point(200, 100 ) )
# rect.setOutline("MistyRose1")
# rect.setWidth(10)
# rect.setFill( "LightCyan2" )
# rect.draw( new_win )
 
class Car(object):
	def __init__(self, width, height):
		rad = height/2
		self.rect = Rectangle(Point(rad, 300 - rad - height), Point(rad + width, 300 - rad))
		#rectangle defined by upper left corner and bottom right
		self.wheel1 = Wheel(Point(rad, 300 - rad), rad * 0.8, rad)
		self.wheel2 = Wheel(Point(rad + width, 300 - rad), rad * 0.8, rad)
 
	def draw(self, win):
		self.rect.draw(win)
		self.wheel1.draw(win)
		self.wheel2.draw(win)
 
	def color(self, body_color,tirescolor, wheelscolor):
		self.rect.setFill(body_color)
		self.wheel1.tire_circle.setFill(tirescolor)
		self.wheel1.wheel_circle.setFill(wheelscolor)
		self.wheel2.tire_circle.setFill(tirescolor)
		self.wheel2.wheel_circle.setFill(wheelscolor)
 
	def move(self, dx, dy):
		self.rect.move(dx,dy)
		self.wheel1.move(dx,dy)
		self.wheel2.move(dx,dy)
 
	def animate(self,win,dx,dy,n):
		if n > 0:
			self.move(dx,dy)
			win.after(20,self.animate,win,dx,dy,n-1)
 
#The first parameter
#is the time in milliseconds after which the GraphWin object will call the animate method again. The second
#parameter is the function object the GraphWin object needs to call; in our case it is the animate method
#of the Wheel object.
 
 
window = GraphWin('Car', 700, 300) 
car1 = Car(70, 40)
car1.color('LightCyan2','black','grey')
car1.draw(window)
car1.animate(window,1,0,400)
 
 
new_win.mainloop()
