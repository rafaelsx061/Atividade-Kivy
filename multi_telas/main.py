import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner

# Tela de Login
class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.label = Label(text="Bem-vindo! Clique para começar", size_hint=(1, 0.2))
        layout.add_widget(self.label)

        botao = Button(text="Clique aqui", size_hint=(1, 0.2))
        botao.bind(on_press=self.ir_para_filmes)
        layout.add_widget(botao)

        self.add_widget(layout)

    def ir_para_filmes(self, instance):
        self.manager.current = 'movie'  # Vai para a tela de filmes


class MovieScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.nome_input = TextInput(
            hint_text="Digite seu nome:",
            multiline=False,
            size_hint=(1, 0.2)
        )

        self.genero_spinner = Spinner(
            values=("Ação", "Comedia", "Animação"),
            text="Escolha o gênero",
            size_hint=(1, 0.2)
        )

        botao_sugerir = Button(
            text="Sugerir filme",
            size_hint=(1, 0.2)
        )
        botao_sugerir.bind(on_press=self.sugerir)

        botao_limpar = Button(
            text="Limpe suas escolhas",
            size_hint=(1, 0.2)
        )
        botao_limpar.bind(on_press=self.limpar)

        self.mensagem_label = Label(
            text="Digite seu nome e escolha um gênero",
            size_hint=(1, 0.2)
        )

        layout.add_widget(self.nome_input)
        layout.add_widget(self.genero_spinner)
        layout.add_widget(botao_sugerir)
        layout.add_widget(botao_limpar)
        layout.add_widget(self.mensagem_label)

        self.add_widget(layout)

        self.filmes = {
            "Ação": ["Os Vingadores - 2012", "Velozes e Furiosos 5 - 2011", "John Wick - 2014"],
            "Comedia": ["Gente Grande - 2010", "Se beber, Não case! - 2009", "As Branquelas - 2004"],
            "Animação": ["Procurando Nemo - 2003", "Altas Aventuras - 2009", "Rio - 2011"]
        }

    def sugerir(self, instance):
        nome = self.nome_input.text.strip()
        genero = self.genero_spinner.text

        if not nome:
            self.mensagem_label.text = "Por Favor, digite seu nome."
        elif genero == "Escolha o gênero":
            self.mensagem_label.text = "Por Favor, selecione um gênero"
        else:
            filme_escolhido = random.choice(self.filmes[genero])
            self.mensagem_label.text = f"{nome}! Sua sugestão de filme de {genero} é: {filme_escolhido}."

    def limpar(self, instance):
        self.nome_input.text = ""
        self.genero_spinner.text = "Escolha o gênero"
        self.mensagem_label.text = "Digite seu nome e escolha um gênero"


# ScreenManager
class GeneroFilmeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))  # Tela inicial
        sm.add_widget(MovieScreen(name='movie'))  # Sua tela de filmes
        return sm

if __name__ == "__main__":
    GeneroFilmeApp().run()
