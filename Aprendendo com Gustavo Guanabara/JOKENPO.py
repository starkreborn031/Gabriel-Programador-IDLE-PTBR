import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class JokenpoGame(BoxLayout):
    def __init__(self, **kwargs):
        super(JokenpoGame, self).__init__(**kwargs)
        self.opcoes = ['Pedra', 'Papel', 'Tesoura']

        self.label = Label(text='Escolha sua jogada:', font_size=20)
        self.add_widget(self.label)

        for opcao in self.opcoes:
            btn = Button(text=opcao, font_size=20)
            btn.bind(on_press=self.jogar)
            self.add_widget(btn)

        self.resultado_label = Label(font_size=20)
        self.add_widget(self.resultado_label)

    def jogar(self, instance):
        escolha_usuario = instance.text.lower()
        escolha_computador = random.choice(self.opcoes).lower()

        self.resultado_label.text = f"Você escolheu: {escolha_usuario}\nComputador escolheu: {escolha_computador}\n"

        if escolha_usuario == escolha_computador:
            self.resultado_label.text += "Empate!"
        elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
             (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
             (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
            self.resultado_label.text += "Você venceu!"
        else:
            self.resultado_label.text += "Você perdeu!"

class JokenpoApp(App):
    def build(self):
        return JokenpoGame()

if __name__ == '__main__':
    JokenpoApp().run()
