"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import sys
import os.path
from PIL import Image, ImageOps

def main():
    # Chama a função que verifica os argumentos passados
    check_arguments(2, [".jpeg", ".jpg", ".png"])

    # Verifica se o input e output tem a mesma extensão
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Extensions are different")

    # Abre a imagem da tshirt
    shirt = Image.open("shirt.png")

    # Tamanho da imagem da tshirt
    size = shirt.size

    # Abre o ficheiro e caso este não exista fecha o programa
    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")

    # Corta a imagem no tamanho certo(o da imagem da tshirt)
    muppet = ImageOps.fit(muppet, size = size)

    # Cola a image da tshirt sobre o muppet e depois grava com o nome que foi dado nos argumentos
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


def check_arguments(num_arguments, file_types):
    # Função para verificar se foram passados o numero correto de argumenos e se o tipo de ficheiro é o correto
    if len(sys.argv) < num_arguments + 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > num_arguments + 1:
        sys.exit("Too many command-line arguments")

    for num in range(1, num_arguments + 1):
        if not any(type in sys.argv[num].lower() for type in file_types):
            sys.exit("Not a valid file")


if __name__ == "__main__":
    main()
