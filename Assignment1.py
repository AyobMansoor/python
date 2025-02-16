import re

class Validator:
    def __init__(self, data_dic: dict[str, str]):
        self.data_dic = data_dic
        self.error_dic = {key: [] for key in self.data_dic.keys()}
    
    def validate(self, key):
        self.value = self.data_dic[key]
        self.key = key
        return self
    
    def required(self):
        if not self.value.strip():
            self.error_dic[self.key].append("This field is required.")
        return self
    
    def has_letter(self):
        if not re.search(r"[a-zA-Z]", self.value):
            self.error_dic[self.key].append("This field must contain at least one letter.")
        return self
    
    def has_digit(self):
        if not re.search(r"\d", self.value):
            self.error_dic[self.key].append("This field must contain at least one digit.")
        return self
    
    def has_upper_case(self):
        if not re.search(r"[A-Z]", self.value):
            self.error_dic[self.key].append("This field must contain at least one uppercase letter.")
        return self
    
    def has_lower_case(self):
        if not re.search(r"[a-z]", self.value):
            self.error_dic[self.key].append("This field must contain at least one lowercase letter.")
        return self
    
    def has_symbol(self):
        if not re.search(r"[^a-zA-Z0-9]", self.value):
            self.error_dic[self.key].append("This field must contain at least one special character.")
        return self
    
    def min_length(self, min):
        if len(self.value) < min:
            self.error_dic[self.key].append(f"This field must be at least {min} characters long.")
        return self
    
    def max_length(self, max):
        if len(self.value) > max:
            self.error_dic[self.key].append(f"This field must be at most {max} characters long.")
        return self
    
    def min(self, min):
        try:
            if float(self.value) < min:
                self.error_dic[self.key].append(f"This field must be at least {min}.")
        except ValueError:
            self.error_dic[self.key].append("This field must be a numeric value.")
        return self
    
    def max(self, max):
        try:
            if float(self.value) > max:
                self.error_dic[self.key].append(f"This field must be at most {max}.")
        except ValueError:
            self.error_dic[self.key].append("This field must be a numeric value.")
        return self
    
    def email(self):
        if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", self.value):
            self.error_dic[self.key].append("Invalid email format.")
        return self
    
    def mobile(self):
        if not re.match(r"^\+?\d{10,15}$", self.value):
            self.error_dic[self.key].append("Invalid mobile number format.")
        return self
    
    def ip(self):
        if not re.match(r"^(\d{1,3}\.){3}\d{1,3}$", self.value):
            self.error_dic[self.key].append("Invalid IP address format.")
        return self
    
    def date(self):
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", self.value):
            self.error_dic[self.key].append("Invalid date format. Use YYYY-MM-DD.")
        return self
    
    def url(self):
        if not re.match(r"^(https?|ftp)://[\w.-]+(\.[\w.-]+)+.*$", self.value):
            self.error_dic[self.key].append("Invalid URL format.")
        return self
    
    def get_errors(self):
        return self.error_dic

# Full test case
data = {
    'email': 'ayob@email.com',
    'password': 'pass123#',
    'username': 'Ayob1',
    'phone': '+967774480038',
    'ip': '129.168.11.11',
    'birthdate': '2003-11-11',
    'website': 'http://ayob.com',
    'age': '20'
}

# Create Validator instance
v = Validator(data)

# Validate fields
v.validate('email').email().required()
v.validate('password').has_letter().has_digit().has_symbol().min_length(6).max_length(20)
v.validate('username').required().min_length(5)
v.validate('phone').mobile()
v.validate('ip').ip()
v.validate('birthdate').date()
v.validate('website').url()
v.validate('age').min(18).max(99)

# Get validation errors
print(v.get_errors())
