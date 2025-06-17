def avalia_tabuleiro(tabuleiro):
    
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]

    return "Empate"

tabuleiros = [
    [
        ['X', 'O', 'X'],
        [' ', 'X', 'O'],
        ['O', ' ', 'X']
    ],
    [
        ['X', 'O', 'O'],
        ['X', 'X', 'O'],
        ['X', 'O', 'X']
    ],
    [
        [' ', ' ', ' '],
        ['X', ' ', 'O'],
        ['O', 'X', 'X']
    ],
    [
        ['O', 'O', 'O'],
        ['X', ' ', 'X'],
        ['O', 'X', 'X']
    ],
    [
        ['X', 'X', 'O'],
        ['X', ' ', 'O'],
        ['O', 'O', 'X']
    ]
]

for i, tabuleiro in enumerate(tabuleiros, 1):
    print(f"Tabuleiro {i}: {avalia_tabuleiro(tabuleiro)}")
