import tkinter as tk

def main():
    bomb = 100
    score = [0, 0]
    press_return = True

    root = tk.Tk()
    root.title("Game")
    root.geometry("600x600+600+250")
    root.iconbitmap("1.png")

    label = tk.Label(root, text='Press [enter] to start the game', font=('Comic Sans MS', 12))
    label.pack()

    fuse_label = tk.Label(root, text=f'Fuse:{str(bomb)}', font=('Comic Sans MS', 14))
    fuse_label.pack()

    score_label_1 = tk.Label(root, text=f'Player 1 Score:{str(score[0])}', font=('Comic Sans MS', 14))
    score_label_1.pack()

    score_label_2 = tk.Label(root, text=f'Player 2 Score:{str(score[1])}', font=('Comic Sans MS', 14))
    score_label_2.pack()

    img1 = tk.PhotoImage(file = "bomb_1.gif")
    img3 = tk.PhotoImage(file = "bomb_3.gif")
    img4 = tk.PhotoImage(file = "bomb_4.gif")

    bomb_label = tk.Label(image = img1)
    bomb_label.pack()

    def update_display():
        nonlocal bomb
        nonlocal score
        if bomb >= 80:
            bomb_label.config(image=img1)
        elif 50 <= bomb < 80:
            bomb_label.config(image=img3)
        elif 0 < bomb < 50:
            bomb_label.config(image=img3)
        else:
            bomb_label.config(image=img4)
        fuse_label.config(text='Fuse: ' + str(bomb))
        score_label_1.config(text='Player 1 Score: ' + str(score[0]))
        score_label_2.config(text='Player 2 Score: ' + str(score[1]))
        fuse_label.after(100, update_display)

    def is_alive():
        nonlocal bomb
        nonlocal press_return
        if bomb <= 0:
            bomb = 0
            label.config(text='Bang! Bang! Bang!')
            press_return = True
            return False
        else:
            return True

    def update_bomb():
        nonlocal bomb
        if is_alive():
            bomb -= 5
            fuse_label.after(400, update_bomb)

    def update_score(player):
        nonlocal score
        if is_alive():
            score[player] += 1
        if player == 0:
            score_label_1.after(3000, update_score, player)
        elif player == 1:
            score_label_2.after(3000, update_score, player)

    def start(event):
        nonlocal press_return
        if not press_return:
            pass
        else:
            update_bomb()
            update_score(0)
            update_score(1)
            update_display()
            label.config(text='')
            press_return = False

    def click_player_1(event):
        nonlocal bomb
        if is_alive():
            bomb += 1

    def click_player_2(event):
        nonlocal bomb
        if is_alive():
            bomb += 1

    click_button_1 = tk.Button(root, text='Player 1 Click', bg='black', fg='white', width=15, font=('Comic Sans MS', 14))
    click_button_1.pack(side=tk.LEFT)

    click_button_1.bind('<Button-1>', click_player_1)

    click_button_2 = tk.Button(root, text='Player 2 Click', bg='black', fg='white', width=15, font=('Comic Sans MS', 14))
    click_button_2.pack(side=tk.RIGHT)

    click_button_2.bind('<KeyPress-s>', click_player_2)

    root.bind('<Return>', start)
    root.mainloop()

main()