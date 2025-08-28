import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner


class GeneroFilme(App):
    def build(self):
            
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
    
        self.nome_input = TextInput(
            hint_text="Digite seu nome:",
            multiline= False,
            size_hint= (1, 0.2)
    )
    
        self.genero_spinner = Spinner(
            values = ("Ação", "Comedia", "Animação"),
            text = "Escolha o gênero",
            size_hint = (1, 0.2)
    )
        
        botao = Button(
        text="Sugerir filme",
        size_hint=(1, 0.2)
        )
        botao.bind(on_press=self.sugerir)
        
        botao_limpar = Button(
            text = "Limpe suas escolhas",
            size_hint= (1, 0.2)
        )
        botao_limpar.bind(on_press=self.limpar)
        
        self.mensagem_label = Label(
            text = "Digite seu nome e escolha um gênero"
        )
        
        layout.add_widget(self.nome_input)
        layout.add_widget(self.genero_spinner)
        layout.add_widget(botao)    
        layout.add_widget(botao_limpar)
        layout.add_widget(self.mensagem_label)
        
        return layout 
    
    filmes = {
    "Ação": ["Os Vingadores - 2012", "Velozes e Furiosos 5 - 2011", "John Wick - 2014"],
    "Comedia": ["Gente Grande - 2010", "Se beber, Não case! - 2009", "As Branquelas - 2004"],
    "Animação": ["Procurando Nemo - 2003", "Altas Aventuras - 2009", "Rio - 2011"]
}

    def sugerir(self, instance):
        
        nome = self.nome_input.text.strip()
        genero = self.genero_spinner.text

        if not nome:
            self.mensagem_label.text = "Por Favor, digite seu nome."
        elif genero == "Selecione o gênero":
            self.mensagem_label.text = "Por Favor, selecione um gênero"
        else:
            filme_escolhido = random.choice(self.filmes[genero])
            self.mensagem_label.text = f"{nome}! Sua sugestão de filme de {genero} é: {filme_escolhido}."
            
    def limpar(self, instance):
            self.nome_input.text = ""
            self.genero_spinner.text = "Escolha o gênero"
            self.mensagem_label.text = "Digite seu nome e escolha um gênero"
            
if __name__ == "__main__":
    GeneroFilme().run()
