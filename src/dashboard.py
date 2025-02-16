import PySimpleGUI as sg

# Criando o layout
def criar_janela_inicial():
    sg.theme('DarkBlue4')

    # Layout inicial do Backlog
    back_log = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    # Layout inicial do To-Do
    to_do = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    # Layout inicial do In Progress
    in_progress = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    # Layout inicial do Done
    done = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    # Layout principal com a estrutura de rolagem
    layout = [
        [
            sg.Column([[sg.Frame('BackLog', layout=[[sg.Column(back_log, scrollable=True, vertical_scroll_only=False, size=(300, 200), key='col_backlog')]],  key='container1')],
            [sg.Button('Nova Tarefa', key='back_log'), sg.Button('Mover para To-do')]],element_justification='center', expand_x=True),

            sg.Column([[sg.Frame('To-do', layout=[[sg.Column(to_do, scrollable=True, vertical_scroll_only=False, size=(300, 200), key='col_todo')]], key='container2')],
            [sg.Button('Nova Tarefa', key='to_do'), sg.Button('Mover para In Progress')]], element_justification='center', expand_x=True),

            sg.Column([[sg.Frame('In Progress', layout=[[sg.Column(in_progress, scrollable=True, vertical_scroll_only=False, size=(300, 200), key='col_progress')]], key='container3')],
            [sg.Button('Nova Tarefa', key='in_progress'), sg.Button('Mover para Done')]], element_justification='center', expand_x=True),

            sg.Column([[sg.Frame('Done', layout=[[sg.Column(done, scrollable=True, vertical_scroll_only=False, size=(300, 200), key='col_done')]], key='container4')],
            [sg.Button('Nova Tarefa', key='done')]], element_justification='center', expand_x=True)
        ],

        [sg.Button('Resetar Tudo')]
    ]
    
    return sg.Window('Task Flow', layout=layout, finalize=True)

# Criar a janela
janela = criar_janela_inicial()

# Loop de eventos da janela
while True:
    event, value = janela.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'back_log':
        # Adicionar nova tarefa ao Backlog
        nova_tarefa_backlog = [sg.Checkbox(''), sg.Input('')]
        janela.extend_layout(janela['col_backlog'], [nova_tarefa_backlog])
        
        # Atualizar a coluna para rolagem
        janela['col_backlog'].contents_changed()

    elif event == "to_do":
        # Adicionar nova tarefa ao To-Do
        nova_tarefa_todo = [sg.Checkbox(''), sg.Input('')]
        janela.extend_layout(janela['col_todo'], [nova_tarefa_todo])
        
        # Atualizar a coluna para rolagem
        janela['col_todo'].contents_changed()

    elif event == "in_progress":
        # Adicionar nova tarefa ao In Progress
        nova_tarefa_progress = [sg.Checkbox(''), sg.Input('')]
        janela.extend_layout(janela['col_progress'], [nova_tarefa_progress])
        
        # Atualizar a coluna para rolagem
        janela['col_progress'].contents_changed()

    elif event == "done":
        # Adicionar nova tarefa ao Done
        nova_tarefa_done = [sg.Checkbox(''), sg.Input('')]
        janela.extend_layout(janela['col_done'], [nova_tarefa_done])
        
        # Atualizar a coluna para rolagem
        janela['col_done'].contents_changed()

    elif event == "Resetar Tudo":
        # Fechar e criar uma nova janela para resetar tudo
        janela.close()
        janela = criar_janela_inicial()