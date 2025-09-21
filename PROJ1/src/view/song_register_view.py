import os

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        self.__clear()

        print("Implementar Nova Musica \n\n")

        title = input("Digite o nome da Música: ")
        artist = input("Digite o nome do artista: ")
        year = input("Digite o ano de publicação: ")

        new_song_informations = {
            "title": title, "artist": artist, "year": year
        }

        return new_song_informations

    def registry_song_success(self, controller_response: dict) -> None:
        self.__clear()

        message = """
            Musica Cadastrada com sucesso!

            * Titulo: {}
            * Quantidade: {}
        """.format(
            controller_response["attributes"]["title"], 
            controller_response["count"]
        )
        print(message)

    def registry_song_fail(self, controller_response: dict) -> None:
        self.__clear()

        message = """
            Erro ao Cadastrada musica

            * Erro: {}
            
        """.format(
            controller_response["error"],
        )
        print(message)

    def __clear(self):
        os.system("cls||clear")