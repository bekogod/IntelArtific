# Importar classes nodo e grafo
from grafo import Graph
from mapa import *
from resolver import Resolver
from matplotlib import pyplot as plt
from matplotlib import colors
from vector import Vector
from jogo import Jogo
from interface import *


def main():

    running = True

    jogo = Jogo()
    resolver = Resolver()
    grafo = Graph()

    map_selected = 0
    mapa = Mapa("tracks/track.txt")

    jogador1 = Player()
    jogador2 = Player()

    jogo.addPlayer(jogador1)
    jogo.addPlayer(jogador2)

    jogo.resetPlayers(mapa)
    jogo.n_players = 1

    grafo.createGraphCartesian(mapa)

    alg_selected = 0

    players_selected = 0

    game_menu = "main_menu"

    while running:

        # CHECK MENU

        if game_menu == 'main_menu':

            # Background colour
            screen.fill((50, 50, 50))

            jogo.run = True

            screen.blit(icon_dimmed, (0, 0))

            start = createButton("Start", 0, COLOR_BLACK)
            maps = createButton("Choose Map", 1, COLOR_BLACK)
            algoritmos = createButton("Choose Algorithm(s)", 2, COLOR_BLACK)
            players = createButton("Choose Number of players", 3, COLOR_BLACK)
            calcPath = createButton("Calculate Best Path", 4, COLOR_BLACK)
            quit_game = createButton("Quit", 6, COLOR_BLACK)

        if game_menu == 'pista':

            time.sleep(1)
            if jogo.run:
                for jogador in jogo.getPlayers():

                    alg_selected = jogador.alg_selected

                    jog = resolver.getJog(
                        alg_selected, jogador, mapa.finish, grafo)

                    possivelPosicao = jogador.estado + jogador.velocidade + jog

                    novaPosicao, stopType = grafo.checkPath(
                        jogador.estado, possivelPosicao)

                    jogador.jogada(jog)

                    if stopType == WALL:
                        jogador.estado = novaPosicao
                        jogador.velocidade = Vector(0, 0)
                    elif stopType == FINISH:
                        jogador.estado = novaPosicao
                        jogador.velocidade = Vector(0, 0)
                        break

            drawMap(screen, mapa, jogo.getPlayers())

            if stopType == FINISH:
                screen.blit(winImg, (0, 0))
                jogo.run = False

        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if game_menu == "maps":
                # event mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    option = buttonIndex([map1, map2, map3, map4], mousePos)

                    if option == 0:
                        mapa = Mapa("tracks/track.txt")
                        map_selected = 0

                    elif option == 1:
                        mapa = Mapa("tracks/trackCircle.txt")
                        map_selected = 1
                    elif option == 2:
                        mapa = Mapa("tracks/trackSimple.txt")
                        map_selected = 2
                    elif option == 3:
                        mapa = Mapa("tracks/bigtrack.txt")
                        map_selected = 3

                    elif leave.collidepoint(mousePos):
                        game_menu = 'main_menu'
                    else:
                        pass

                    map1, map2, map3, map4, leave = drawMapsMenu(
                        map_selected)

                    grafo = Graph()
                    grafo.createGraphCartesian(mapa)

            elif game_menu == "algoritmos":
                # event mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    option = buttonIndex([a_estrela, greedybf, greedy, bfs, dfs, a_estrela2,
                                          greedybf2, greedy2, bfs2, dfs2, leave_alg], mousePos)

                    if option > 0 and option < 5:

                        jogo.players[0].alg_selected = option

                    elif option > 4 and option < 10:

                        jogo.players[1].alg_selected = option-5

                    elif leave_alg.collidepoint(mousePos):
                        game_menu = 'main_menu'
                    else:
                        pass
                a_estrela, greedybf, greedy, bfs, dfs, a_estrela2, greedybf2, greedy2, bfs2, dfs2, leave_alg = drawAlgoritmosMenu(
                    alg_selected, jogo.players)

            elif game_menu == "calcPath":
                # event mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    option = buttonIndex(
                        [a_estrela, greedybf, greedy, bfs, dfs, leave], mousePos)

                    inicio = mapa.start
                    fim = mapa.finish

                    if option == 0:
                        (path, custoT) = resolver.a_estrela_search(
                            inicio, fim, grafo)
                        p = [(vector.x, vector.y)for vector in path]

                        mapa.show()
                        showPath(p)
                        plt.show()
                    elif option == 1:
                        (path, custoT) = resolver.greedy_bf_search(
                            inicio, fim, grafo)
                        p = [(vector.x, vector.y)for vector in path]

                        mapa.show()
                        showPath(p)
                        plt.show()
                    elif option == 2:

                        (path, custoT) = resolver.greedy_search(
                            inicio, fim, grafo, 0, path=[])
                        p = [(vector.x, vector.y)for vector in path]

                        mapa.show()
                        showPath(p)
                        plt.show()

                    elif option == 3:

                        (path, custo) = resolver.bfs(inicio, fim, grafo)
                        p = [(vector.x, vector.y)for vector in path]

                        mapa.show()
                        showPath(p)
                        plt.show()

                    elif option == 4:

                        (path, custoT) = resolver.dfs(
                            inicio, fim, grafo, path=[], visited=set())
                        p = [(vector.x, vector.y)for vector in path]

                        mapa.show()
                        showPath(p)
                        plt.show()

                    elif leave.collidepoint(mousePos):
                        game_menu = 'main_menu'
                    else:
                        pass

                a_estrela, greedybf, greedy, bfs, dfs, leave = drawPathMenu()

            elif game_menu == "players":

                # event mouse
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if one.collidepoint(mousePos):

                        jogo.resetPlayers(mapa)

                        jogo.n_players = 1
                        players_selected = 0

                        one, two, leave = drawJogMenu(
                            players_selected)
                    elif two.collidepoint(mousePos):

                        jogo.resetPlayers(mapa)

                        jogo.n_players = 2
                        players_selected = 1

                        one, two, leave = drawJogMenu(
                            players_selected)
                    elif leave.collidepoint(mousePos):
                        game_menu = 'main_menu'
                    else:
                        pass

            elif game_menu == "pista":

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_menu = 'main_menu'

            elif game_menu == "main_menu":
                jogo.resetPlayers(mapa)
                # event mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill((50, 50, 50))

                    if start.collidepoint(mousePos):
                        game_menu = "pista"
                        drawMap(screen, mapa, jogo.getPlayers())

                    if maps.collidepoint(mousePos):
                        game_menu = "maps"

                        map1, map2, map3, map4, leave = drawMapsMenu(
                            map_selected)

                    if algoritmos.collidepoint(mousePos):
                        game_menu = "algoritmos"

                        a_estrela, greedybf, greedy, bfs, dfs, a_estrela2, greedybf2, greedy2, bfs2, dfs2, leave_alg = drawAlgoritmosMenu(
                            alg_selected, jogo.players)

                    if players.collidepoint(mousePos):
                        game_menu = "players"

                        one, two, leave = drawJogMenu(
                            players_selected)

                    if calcPath.collidepoint(mousePos):
                        game_menu = "calcPath"

                        a_estrela_path, greedybf_path, greedy_path, bfs_path, dfs_path, leave = drawPathMenu()

                    if quit_game.collidepoint(mousePos):
                        running = False

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
