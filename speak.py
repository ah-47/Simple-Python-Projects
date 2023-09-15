import os
if __name__ == '__main__':
    print('Welcome to Robo Speaker')
    while True:
        x = input('What do u want me to speak: ')
        if x == 'q':
            os.system("say 'byeee'")
            break
        command = f'say {x}'
        os.system(command)