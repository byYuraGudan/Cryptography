from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config

import cezarCrypto

HEIGHT = 480
WIDTH = 640

Config.set('graphics','resizable',1)
Config.set('graphics','width', WIDTH)
Config.set('graphics','height',HEIGHT)

from kivy.uix.boxlayout import BoxLayout


class MyApp(App):


    def initButton(self):
        self.encodeButton = Button(text='Encrypt',
                                   on_press = self.encodeEventButton)
        self.decodeButton = Button(text='Decrypt',
                                   on_press = self.decodeEventButton)

    def initTextInput(self):
        self.phraseTextInput = TextInput(hint_text = "The prhase encrypt or decrypt")
        self.numberTextInput = TextInput(hint_text = "Enter key only number")
        self.resultTextInput = TextInput()

    def initLabel(self):
        self.statusLabel = Label(text ='',
                                 size_hint = [1,.05],
                                 color = [1,0,0,1])
    def build(self):
        self.initButton()
        self.initTextInput()
        self.initLabel()

        pageLayout = PageLayout(page = 2)


        mainLayout = BoxLayout(orientation='vertical',
                               padding = 30)
        textInputLayout = BoxLayout(orientation='vertical',
                                    size_hint = [1,.7],
                                    padding = 5,
                                    spacing = 5)
        textInputLayout.add_widget(Label(text = 'Enter the phrase you want to encrypt or decrypt'))
        textInputLayout.add_widget(self.phraseTextInput)
        textInputLayout.add_widget(Label(text = 'Enter key'))
        textInputLayout.add_widget(self.numberTextInput)

        buttonLayout = BoxLayout(orientation = 'horizontal',
                                 size_hint = [1,.2],
                                 padding = 5,
                                 spacing = 5)
        buttonLayout.add_widget(self.encodeButton)
        buttonLayout.add_widget(self.decodeButton)

        resultLayout = BoxLayout(orientation = 'vertical',
                                 padding = 10)
        resultLayout.add_widget(Label(text = 'Result',
                                      size_hint = [1,.2]))
        resultLayout.add_widget(self.resultTextInput)
    
        mainLayout.add_widget(textInputLayout)
        mainLayout.add_widget(buttonLayout)
        mainLayout.add_widget(resultLayout)
        mainLayout.add_widget(self.statusLabel)

        # mainLayout.add_widget(pageLayout)
        return mainLayout

    def encodeEventButton(self,instance):
        try:
            key = int(self.numberTextInput.text)
            string = str(self.phraseTextInput.text)
            self.resultTextInput.text = cezarCrypto.cEncode(string, key)
            self.clearTextInput()
        except ValueError:
            self.exceptNotNumber()

    def decodeEventButton(self,instance):
            try:
                key = int(self.numberTextInput.text)
                string = str(self.phraseTextInput.text)
                self.resultTextInput.text = cezarCrypto.cDecode(string, key)
                self.clearTextInput()
            except ValueError:
                self.exceptNotNumber()

    def exceptNotNumber(self):
        print('Please enter key only number!')
        self.statusLabel.text = "Please enter key only number!"
        self.numberTextInput.text = ""

    def     clearTextInput(self):
        self.numberTextInput.text = ""
        self.phraseTextInput.text = ""
        self.statusLabel.text = ""

if __name__ == "__main__":
    MyApp().run()