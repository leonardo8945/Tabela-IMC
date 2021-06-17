print('\033[1;4;36mPROGRAMA IMC\033[m')
from datetime import datetime
nome = str(input('\033[36mDigite o seu nome: '))
data = int(input('Digite o ano do seu nascimento: '))
idade = datetime.now().year - data
massa = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): \033[m'))
imc = massa / altura ** 2
print(f'\033[36mOlá\033[m \033[1;32m{nome}\033[m, \033[36mvocê tem\033[m \033[1;32m{idade} anos.\033[m '
      f'\n\033[36mEstá com\033[m \033[1;32m{massa} (Kg)\033[m, '
      f'\n\033[36mE a sua altura é\033[m \033[1;32m{altura} (M)\033[m')
print(f'\033[36mO seu IMC é:\033[m \033[1;32m{imc:.1f}\033[m')
if imc <= 17:
    print('\033[36mVocê está\033[m \033[1;4;33mMUITO ABAIXO DO PESO!\033[m')
elif imc <= 18.5:
    print('\033[36mVocê está\33[m \033[1;4;32mABAIXO DO PESO!\033[m')
elif imc <= 25:
    print('\033[36mVocê está\033[m \033[1;4;34mCOM O PESO IDEAL!\033[m')
elif imc <= 30:
    print('\033[36mVocê está\033[m \033[1;4;36mCOM SOBPESO!\033[m')
elif imc <= 35:
    print('\033[36mVocê está\033[m \033[1;4;35mCOM OBESIDADE!\033[m')
elif imc <= 40:
    print('\033[36mVocê está\033[m \033[1;4;31mCOM OBESIDADE SEVERA!\033[m')
else:
    print('\033[1;4;31mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA!\033[m')
    


