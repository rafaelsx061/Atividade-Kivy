from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

KV = """
<MainWidget>:
    orientation: "vertical"
    padding: 30
    spacing: 20

    canvas.before:
        Color:
            rgba: 0.9, 0.9, 0.9, 1  # fundo cinza claro
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "📂 Verificador de Arquivo"
        font_size: 28
        bold: True
        color: 0.5, 0, 0.5, 1   # Roxo
        size_hint_y: None
        height: 50

    TextInput:
        id: nome_input
        hint_text: "Digite seu nome"
        font_size: 18
        multiline: False
        size_hint_y: None
        height: 50

    TextInput:
        id: idade_input
        hint_text: "Digite sua idade"
        font_size: 18
        multiline: False
        input_filter: "int"
        size_hint_y: None
        height: 50

    Button:
        text: "Enviar"
        font_size: 20
        size_hint_y: None
        height: 55
        background_normal: ""
        background_color: 0.2, 0.6, 1, 1  # azul claro
        color: 1, 1, 1, 1
        on_release: root.verificar_idade()

    Label:
        id: resultado
        text: ""
        font_size: 20
        halign: "center"
        valign: "middle"
        text_size: self.size
        color: 0, 0, 0, 1
"""

class MainWidget(BoxLayout):
    def verificar_idade(self):
        nome = self.ids.nome_input.text.strip()
        idade_texto = self.ids.idade_input.text.strip()

        if not nome or not idade_texto:
            self.mostrar_mensagem("⚠️ Preencha todos os campos.", "aviso")
            return

        try:
            idade = int(idade_texto)
        except ValueError:
            self.mostrar_mensagem("❌ A idade deve ser um número.", "erro")
            self.ids.idade_input.text = ""
            self.ids.idade_input.focus = True
            return

        if idade < 0 or idade > 120:
            self.mostrar_mensagem("❌ Idade inválida. Digite entre 0 e 120.", "erro")
            self.ids.idade_input.text = ""
            self.ids.idade_input.focus = True
            return

        if idade < 18:
            self.mostrar_mensagem(f"👋 Olá, {nome}! Você é menor de idade.", "info")
        elif idade >= 60:
            self.mostrar_mensagem(f"🌟 Olá, {nome}! Você é idoso e merece muito respeito ❤️.", "sucesso")
        else:
            self.mostrar_mensagem(f"✅ Olá, {nome}! Você é maior de idade.", "sucesso")

    def mostrar_mensagem(self, texto, tipo):
        self.ids.resultado.text = texto
        cores = {
            "erro": (1, 0, 0, 1),
            "aviso": (1, 0.6, 0, 1),
            "sucesso": (0, 0.6, 0, 1),
            "info": (0, 0.5, 1, 1)
        }
        self.ids.resultado.color = cores.get(tipo, (0, 0, 0, 1))


class MeuApp(App):
    def build(self):
        Builder.load_string(KV)
        return MainWidget()


if __name__ == "__main__":
    MeuApp().run()