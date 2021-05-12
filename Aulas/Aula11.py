
# ! Cores no terminal

# ANDI - escape sequence
# \033[0;33;44 m
#      estilo, texto, background


# ESTILO                        TEXTO               Background
# 0 = sem estilo                30 = Branco         40 = Branco   
# 1 = Bold (Negrito)            31 = Vermelho       41 = Vermelho
# 4 = Underlin (Sublinhado)     32 = Verde          42 = Verde
# 7 = Negative                  33 = Amarelo        43 = Amarelo
#                               34 = Azul           44 = Azul
#                               35 = Magenta        45 = Magenta
#                               36 = Ciano          46 = Ciano
#                               37 = Cinza          47 = Cinza
#
# Fundo preto - \033[m    -> invertido \033[m7;30

print('\033[4;30;45mOla Mundo!\033[m')
print('\033[7;30mOla Mundo!\033[m')