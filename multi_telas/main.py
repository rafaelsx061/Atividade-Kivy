import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

# Tela de Login
class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        label = Label(text="Bem-vindo! Clique para começar", size_hint=(1, 0.2))
        layout.add_widget(label)

        botao = Button(text="Clique aqui", size_hint=(1, 0.2))
        botao.bind(on_press=self.ir_para_filmes)
        layout.add_widget(botao)

        self.add_widget(layout)

    def ir_para_filmes(self, instance):
        self.manager.current = 'movie'

# Tela de Sugestão de Filmes
class MovieScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filmes_favoritos = []  # Lista de favoritos

        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.nome_input = TextInput(
            hint_text="Digite seu nome:",
            multiline=False,
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.nome_input)

        self.genero_spinner = Spinner(
            values=("Ação", "Comedia", "Animação"),
            text="Escolha o gênero",
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.genero_spinner)

        botao_sugerir = Button(
            text="Sugerir filme",
            size_hint=(1, 0.2)
        )
        botao_sugerir.bind(on_press=self.sugerir)
        layout.add_widget(botao_sugerir)

        botao_favoritos = Button(
            text="Ver favoritos",
            size_hint=(1, 0.2)
        )
        botao_favoritos.bind(on_press=self.ir_para_favoritos)
        layout.add_widget(botao_favoritos)

        botao_limpar = Button(
            text="Limpe suas escolhas",
            size_hint=(1, 0.2)
        )
        botao_limpar.bind(on_press=self.limpar)
        layout.add_widget(botao_limpar)

        self.mensagem_label = Label(
            text="Digite seu nome e escolha um gênero",
            size_hint=(1, 0.2)
        )
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
            self.mensagem_label.text = "Por favor, digite seu nome."
        elif genero == "Escolha o gênero":
            self.mensagem_label.text = "Por favor, selecione um gênero"
        else:
            filme_escolhido = random.choice(self.filmes[genero])
            self.mensagem_label.text = f"{nome}! Sua sugestão de filme de {genero} é: {filme_escolhido}."
            # Adiciona à lista de favoritos
            if filme_escolhido not in self.filmes_favoritos:
                self.filmes_favoritos.append(filme_escolhido)

    def ir_para_favoritos(self, instance):
        fav_screen = self.manager.get_screen('favorites')
        fav_screen.atualizar_lista(self.filmes_favoritos)
        self.manager.current = 'favorites'

    def limpar(self, instance):
        self.nome_input.text = ""
        self.genero_spinner.text = "Escolha o gênero"
        self.mensagem_label.text = "Digite seu nome e escolha um gênero"

class FavoriteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.grid = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)

        botao_voltar = Button(text="Voltar", size_hint=(1, 0.1))
        botao_voltar.bind(on_press=self.voltar)
        layout.add_widget(botao_voltar)

        botao_reiniciar = Button(text="Reiniciar App", size_hint=(1, 0.1))
        botao_reiniciar.bind(on_press=self.reiniciar)
        layout.add_widget(botao_reiniciar)

        self.add_widget(layout)

    def atualizar_lista(self, filmes_favoritos):
        self.grid.clear_widgets()
        if filmes_favoritos:
            for filme in filmes_favoritos:
                self.grid.add_widget(Label(text=filme, size_hint_y=None, height=40))
        else:
            self.grid.add_widget(Label(text="Nenhum filme favoritado ainda.", size_hint_y=None, height=40))

    def voltar(self, instance):
        self.manager.current = 'movie'

    def reiniciar(self, instance):
        self.manager.get_screen('movie').filmes_favoritos = []
        self.manager.get_screen('movie').limpar(instance)
        self.manager.current = 'login'

class GeneroFilmeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(MovieScreen(name='movie'))
        sm.add_widget(FavoriteScreen(name='favorites'))
        return sm

if __name__ == "__main__":
    GeneroFilmeApp().run()
