INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF ='INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EOF'


class Token(object):
    def __init__(self, type, value): 
        self.type = type
        self.value = value
        
    def __str__(self):
        return "Token({type}, {value})".format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("The Lexer was unable to get the next token.")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) -1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def remove_white_space(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit(): 
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:         
            
            if self.current_char.isspace():
                self.remove_white_space()
                continue
            
            if self.current_char.isdigit():
                return Token('INTEGER', self.integer())
            
            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')
            
            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')
            
            if self.current_char == '*':
                self.advance()
                return Token('MULTIPLY', '*')

            if self.current_char == '/':
                self.advance()
                return Token('DIVIDE', '/')

            self.error()
        return Token('EOF', None)

class Interpreter(object): 

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception('The parser failed parsing the input: Invalid Syntax from eat method')
    
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token_value = self.current_token.value
        self.eat(INTEGER)
        return token_value

    def term(self):
        result = self.factor()
        while self.current_token.type in (DIVIDE, MULTIPLY):
           
            if self.current_token.type == DIVIDE:
                self.eat(DIVIDE)
                result = result / self.factor()
                
            elif self.current_token.type == MULTIPLY:
                self.eat(MULTIPLY)
                result = result * self.factor()

        return result


    def expr(self):
        
        result = self.term()
        
        while self.current_token.type in (PLUS, MINUS):
        
            if self.current_token.type == PLUS: 
                self.eat(PLUS)
                result = result + self.term()
            
            elif self.current_token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
            
        print(result)                
