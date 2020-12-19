import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # theme
        sg.theme('DarkAmber')
        # layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(20,0), key='nome')],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(20,0), key='idade')],
            [sg.Text('Que redes sociais você usa?', size=(25,0))],
            [sg.Checkbox('Tik Tok', key='tik tok'), 
            sg.Checkbox('YouTube', key='youtube'),
            sg.Checkbox('WhatsApp', key='whatsapp')],
            [sg.Button('Enviar dados')]
        ]

        #janela
        janela = sg.Window('Dados do Usuário').layout(layout)

        #extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        usa_tik_tok = self.values['tik tok']
        usa_youtube = self.values['youtube']
        usa_whatsapp = self.values['whatsapp']

        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'usa tik tok: {usa_tik_tok}')
        print(f'usa youtube: {usa_youtube}')
        print(f'usa whatsapp: {usa_whatsapp}')

tela = TelaPython()
tela.Iniciar()