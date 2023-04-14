cols = '   1  2  3'
row1 = list('A   |   |   \n' \
        '  ---------')
row2 = list('B   |   |   \n' \
        '  ---------')
row3 = list('C   |   |   ')


print("Let's play Tic-Tac-Toe!\n"
      "X goes first.")

ison = True
i = 0
while ison:
        print(''.join(cols), ''.join(row1), ''.join(row2), ''.join(row3), sep='\n')
        if i % 2 ==0:
                player = 'X'
        else:
                player = 'O'
        selection = input(f"{player}, choose a row and column (For example, type 'A1' to choose the position in row A column 1):")
        selection = selection.upper()
        if selection[0] == 'A':
                if selection[1] == '1' and row1[2] == ' ':
                        row1[2] = player
                        i+=1
                elif selection[1] == '2' and row1[6] == ' ':
                        row1[6] = player
                        i += 1
                elif selection[1] == '3' and row1[10] == ' ':
                        row1[10] = player
                        i += 1
                else:
                        print('Column number is out of bounds. Try again!')
        elif selection[0] == 'B':
                if selection[1] == '1' and row2[2] == ' ':
                        row2[2] = player
                        i += 1
                elif selection[1] == '2' and row2[6] == ' ':
                        row2[6] = player
                        i += 1
                elif selection[1] == '3' and row2[10] == ' ':
                        row2[10] = player
                        i += 1
                else:
                        print('Column number is out of bounds. Try again!')
        elif selection[0] == 'C':
                if selection[1] == '1' and row3[2] == ' ':
                        row3[2] = player
                        i += 1
                elif selection[1] == '2' and row3[6] == ' ':
                        row3[6] = player
                        i += 1
                elif selection[1] == '3' and row3[10] == ' ':
                        row3[10] = player
                        i += 1
                else:
                        print('Column number is out of bounds. Try again!')
        else:
                print('Row letter is out of bounds. Try again!')

        if row1[2] == row1[6] == row1[10] == player or row2[2] == row2[6] == row2[10] == player or row3[2] == row3[6] == row3[10] == player:
                ison = False
        elif row1[2] == row2[2] == row3[2] == player or row1[6] == row2[6] == row3[6] == player or row1[10] == row2[10] == row3[10] == player:
                ison = False
        elif row1[2] == row2[6] == row3[10] == player or row1[10] == row2[6] == row3[2] == player:
                ison = False

else:
        print(''.join(cols), ''.join(row1), ''.join(row2), ''.join(row3), sep='\n')
        print(f'Game Over! {player} wins!')