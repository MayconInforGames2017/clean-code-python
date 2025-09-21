import os

class PlaylistCreatorView:
    def playlis_creator_success(self, controller_response) -> None:
        self.__clear()
        print("Playlist Criada com sucesso! \n\n")

        for music in controller_response["playlist"]:
            message = """
                Titulo da musica: {}
                Artista: {}
                Ano de publicação: {}
            
            """.format(
                music.title,
                music.artist,
                music.year
            )
            print(message)

    def playlist_creator_fail(self, controller_response) -> None:
        self.__clear()

        message = """
                Erro na criação da playlist
                
                * Erro: {}
            
            """.format(
                controller_response["erro"]
            )
        print(message)

    def __clear(self):
        os.system("cls||clear")