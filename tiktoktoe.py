import PySimpleGUI as sg

# Konfigurasi tema antarmuka pengguna
sg.theme('LightGrey1')

# Membuat layout antarmuka pengguna
layout = [[sg.Button('', size=(10, 5), key=(i, j), font=('Arial', 20)) for j in range(3)] for i in range(3)]
layout.append([sg.Button('New Game', font=('Arial', 16)), sg.Button('Exit', font=('Arial', 16))])

# Membuat window antarmuka pengguna
window = sg.Window('Tic Tac Toe', layout)

# Inisialisasi variabel permainan
player = 'X'
game_over = False
board = [[None for j in range(3)] for i in range(3)]

# Fungsi untuk mengecek apakah ada pemenang
def check_winner():
    global game_over
    winner = None
    # Cek baris
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            winner = board[i][0]
            break
    # Cek kolom
    if not winner:
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
                winner = board[0][j]
                break
    # Cek diagonal
    if not winner:
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            winner = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            winner = board[0][2]
    # Jika ada pemenang, tampilkan pesan di layar
    if winner:
        game_over = True
        sg.popup(f'Player {winner} wins!')

# Looping untuk memproses event di antarmuka pengguna
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
        
    if event == 'New Game':
        player = 'X'
        game_over = False
        board = [[None for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                window[(i, j)].update('')
        
    elif not game_over and event != 'New Game':
        i, j = event
        if board[i][j] is None:
            board[i][j] = player
            window[event].update(player)
            check_winner()
            player = 'O' if player == 'X' else 'X'

# Close the window
window.close()
