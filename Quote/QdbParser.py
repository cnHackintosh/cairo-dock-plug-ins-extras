# This is a part of the external Quote applet for Cairo-Dock
#
# Author: Eduardo Mucelli Rezende Oliveira
# E-mail: edumucelli@gmail.com or eduardom@dcc.ufmg.br

from sgmllib import SGMLParser

class QdbParser(SGMLParser):

    def reset(self):                              
        SGMLParser.reset(self)
        self.name = "Qdb.us"
        self.url = "http://www.qdb.us/random"
        self.quote = []
        self.inside_span_element = False                                            # indica se o parser esta dentro de <span></span> tag
        self.inside_nickname = False                                                # <p>"<nickname>phrase"</p>
        self.current_quote = ""

    def start_span(self, attrs):
        for name, value in attrs:
            if name == "class" and value == "qt":                                   # <span class="qt">...</span>
                self.inside_span_element = True
    
    def end_span(self):
        self.inside_span_element = False
        self.quote.append(self.current_quote)                                       # adiciona o conteudo completo da tag
        self.current_quote = ""                                                     # reinicia o armazenador do conteudo

    def handle_data(self, text):
        if self.inside_span_element:                                                # estamos dentro de <span>...</span>
            self.current_quote += text
#            if not self.inside_nickname:                                            # <nickname> quote
#                if text == '<':                                                     # entered the "nickname area"
#                    self.inside_nickname = True
#                    self.current_quote += '\n<'                                     # linebreak
#                else:
#                    self.current_quote += text                                      # concatena tudo que tiver dentro da tag
#            else:                                                                   
#                self.current_quote += text                                          # concatenate all the nickname
#                if text == '>':                                                     # nickname is over
#                    self.inside_nickname = False                                    # set it

    def parse(self, page):
        self.feed(str(page))                                                             # feed the parser with the page's html
        self.close()
