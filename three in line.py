
import PySimpleGUI as sg

button_size=(7,3)
player_one=("X")
player_two=("O")
game_board=[""]*9

current_player=player_one

layout= [[sg.Button("",key="-0", size=(button_size)), 
          sg.Button("",key="-1" ,size=(button_size)), 
          sg.Button("",key="-2" ,size=(button_size))],
         [
             sg.Button("", key="-3" ,size=(button_size)), 
          sg.Button("",key="-4" , size=(button_size)), 
          sg.Button("",key="-5" ,size=(button_size))],
         [sg.Button("", key="-6" ,size=(button_size)), 
          sg.Button("", key="-7" ,size=(button_size)), 
          sg.Button("",key="-8" ,size=(button_size))],
         [sg.Button('He terminado', key="-OK-")]]

window=sg.Window("Demo", layout)


def check_winner():
    #check rows
    for i in range(0,9,3):
        if game_board[i]==game_board[i+1]==game_board[i+2]!="":
            return True
        
    #check columns 
    for i in range(3):
        if game_board[i]==game_board[i+3]==game_board[i+6]!="":
            return True
    
    #check diagonals
    if game_board[0]== game_board[4]==game_board[8]!="":
        return True

    if game_board[2]==game_board[4]==game_board[6]!="":
        return True
    
    return False

while True:
    event, values=window.read()

    if event==sg.WIN_CLOSED or event == "-OK-":
        break
    
    if event!="-OK-":
        button_key=event
        # print(button_key)
        # print("Clicked button key", button_key)
        button_text=window[button_key].ButtonText
        # print("Button Text: ", button_text)

    if button_text=="":
        window[button_key].update(text=current_player)
        game_board[int(button_key[1:])]=current_player
        
        # print(game_board)

        if check_winner():
            if current_player=="X":
                current_player="Player One"
            if current_player=="O":
                current_player="Player Two"
            
            sg.popup("The Winner is {}".format(current_player))
            break


        if current_player==player_one:
            current_player=player_two
        elif current_player==player_two:
            current_player=player_one

window.close()