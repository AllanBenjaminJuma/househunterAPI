class UserModel: 
    def __init__(self, phoneno, name): 
        self.phoneno=phoneno
        self.name=name
      
    # getter method phoneno
    def get_phoneno(self): 
        return self.phoneno 
      
    # setter method phoneno
    def set_phoneno(self, x): 
        self.phoneno = x 

        # getter method name
    def get_name(self): 
        return self.name 
      
    # setter method name
    def set_name(self, x): 
        self.name = x 