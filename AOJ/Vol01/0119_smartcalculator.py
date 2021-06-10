# 0109 Smart calculator
# https://gist.github.com/draftcode/1357281

class S:
    target=""
    cursor=0
    debug=False
    
    def __init__(self,S):
        self.target=S
        self.cursor=0
        self.debug=False
        
    def set_debug(self,b):
        self.debug=b
        
    def cursor_back(self):
        self.cursor-=1
        
    def get_char(self):
        if self.cursor>=len(self.target):
            return ""
        ans=self.target[self.cursor]
        return ans
    def next(self):
        self.cursor+=1
    def print_content(self):
        return self.target[self.cursor:]


    def number(self):
        ret=0
        while True:
            t=self.get_char()
            if t=="":break
            if not(t.isdigit()):
                break
            ret*=10
            ret+=int(t)
            self.next()
        return ret


    def term(self):
        if self.debug:print("term:",self.print_content())
        ret = self.factor();
        while True:
            t=self.get_char()
            if t=='*':
                self.next()
                ret *= self.factor()
            elif t=='/':
                self.next()
                #print(S.get_char())
                #ret //=self.factor()
                ret = int(ret/self.factor())
            else:
                break
        if self.debug: print("term-e:",ret)
        return ret

    def expression(self):
        if self.debug: print("expression:",self.print_content())

        ret = self.term();
        while True:
            t=self.get_char()
            if t=='+':
                self.next()
                ret += self.term()
            elif t=='-':
                self.next()
                ret -= self.term()
            else:
                break
        if self.debug: print("expression-e:",ret)
        return ret

    def factor(self):
        if self.debug:print("factor:",self.print_content())
        t=self.get_char()
        if t == '(':
            self.next()
            ret = self.expression()
            self.next()
            if self.debug: print("factor-e:",ret)

            return ret
        else:
            ret=self.number()
            if self.debug: print("factor-e:",ret)
            return ret

N=int(input())


for _ in range(N):
    _S=S(input()[:-1])
    #_S.set_debug(True)
    print(_S.expression()) 