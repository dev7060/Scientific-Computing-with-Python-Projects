class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def set_width(self, width):
    self.width=width
  def set_height(self, height):
    self.height = height
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    mystr = ""
    for i in range (0, self.height):
      for j in range (0, self.width):
        mystr = mystr + "*"
      mystr = mystr + "\n"
    return mystr
  def __str__(self): 
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
  def get_amount_inside(self, obj):
    return int((self.height*self.width)/(obj.height*obj.width))
   
class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  def set_side(self, side):
    self.height = side
    self.width = side
  def __str__(self):
    return "Square(side=" + str(self.height) +")"
  def set_width(self, width):
    self.height = width
    self.width = width
  def set_height(self, height):
    self.height = height 
    self.width = height
