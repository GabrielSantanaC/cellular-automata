import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    # Cria uma cópia da grade para atualizar
    newGrid = grid.copy()
    # Percorre cada célula da grade
    for i in range(N):
        for j in range(N):
            # Calcula o total de vizinhos vivos (usando vizinhança com wrap-around, ou seja, bordas conectadas)
            total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                     grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                     grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                     grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            
            # Aplica as regras do Game of Life:
            # 1. Qualquer célula viva com menos de 2 ou mais de 3 vizinhos vivos morre.
            # 2. Qualquer célula morta com exatamente 3 vizinhos vivos se torna viva.
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    # Atualiza a imagem com a nova grade
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    # Define o tamanho da grade
    N = 50
    # Inicializa a grade de forma aleatória (20% células vivas, 80% mortas)
    grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)
    
    # Configura a figura para a animação
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='binary')
    
    # Cria a animação que chama a função update a cada 300ms
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                                  frames=10, interval=300, save_count=50)
    plt.title("Conway's Game of Life")
    plt.show()

if __name__ == '__main__':
    main()
