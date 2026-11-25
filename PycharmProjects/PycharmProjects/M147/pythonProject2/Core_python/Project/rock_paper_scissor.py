'''
Rock,paper,scissor

Rock   scissor --> Rock
Rock   paper   --> paper
paper  scissor --> scissor

Rock -- Rock
'''
import random

l = ['Rock','Paper','Scissor']

while True:
    r = random.randint(0,2)
    for i in range(len(l)):
        print(i+1,'--',l[i])
    ch = int(input('enter the choice:'))
    print('you:',l[ch-1])
    print('computer:',l[r])

    if l[ch-1] == l[r]:
        print('It\'s a Draw')
    elif l[ch-1]=='Scissor' and l[r]=='Paper':
        print('Wow nice you won ..!!')
    elif l[ch-1] =='Rock' and l[r]=='Scissor':
        print('Wow nice you won ..!!')
    elif l[ch-1] == 'Paper' and l[r] == 'Rock':
        print('Wow nice you won ..!!')
    else:
        print('Computer WINS...You lost....')

    a = input('Do you wamt to play again ?? (y/n):')
    if a.lower() == 'y':
        continue
    else:
        print('Thank you for playing.....')
        break







