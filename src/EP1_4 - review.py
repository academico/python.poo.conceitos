# ler uma image no formato PBM
def leiaImagemPBM(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Verifica se o arquivo é uma imagem PBM válida (P1 na 1ra linha)
    formato =  lines[0].strip()
    if formato != 'P1':
        raise ValueError('O arquivo não é uma imagem PBM válida.')

    # Obtém as dimensões da imagem
    vet = lines[1].split()
    width, height = [int(vet[i]) for i in range(len(vet))]
    #print(width, height)

    # Inicializa a matriz de pixels
    pixels = [[0]*width for _ in range(height)]

    # Percorre as linhas da imagem e preenche a matriz de pixels
    for i in range(2,height+1):
        row = lines[i].strip()
        for j in range(len(row)):
            pixels[i-2][j] = int(row[j])
    return formato, width, height, pixels # retorna tupla (string, int, int, matriz)



def dilata(pixels):
    height,width = len(pixels),len(pixels[0])
    dil = [[0]*width for _ in range(height)]

    for i in range(height):
        for j in range(width):
            max = pixels[i][j]
            for x in range(-1,2):
              for y in range(-1,2):
                viz_i = i + x
                viz_j = j + y
                if 0<=viz_i and viz_i < height and 0<=viz_j and viz_j < width:
                  if pixels[viz_i][viz_j] > max:
                    max = pixels[viz_i][viz_j]
            dil[i][j] = max
    return dil



def PrintMatrix(matrix):
    for linha in matrix:
      print(''.join(map(str, linha)))
    print()



def ReadFilePbm():
    filename = input()
    formato, width, height, pixels = leiaImagemPBM(filename) # recebe tupla (string formato, int width, int height , matriz pixel)
    # Imprimir a matriz
    print(filename)
    print(formato)
    print(width, height)
    PrintMatrix(pixels)
    return pixels



def ImageDilation(pixels):
  dilatada = dilata(pixels)
  print('Matriz Resultante')
  PrintMatrix(dilatada)



def main():
    try:      #Captura exceção lançada pela leiaImagemPBM'raise ValueError'
      pixels = ReadFilePbm()
      ImageDilation(pixels)
    except ValueError as e:
      print(f"{e}")  # printa mensagem da exceção ValueError


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()