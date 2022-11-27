class Usuario:
    def __init__(self, username=None, password=None, email= None):
        self.username = username
        self._password = self._generate_password(password)
        self._email = email
    
    def _generate_password(self, password):
        
        return password.upper()
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = self._generate_password(password)
        
    

eduardo = Usuario('eduardo', 'eduardo123', 'edu@gmail.com')

print(eduardo.password)

eduardo.password = "Pepe"

print(eduardo.password)
