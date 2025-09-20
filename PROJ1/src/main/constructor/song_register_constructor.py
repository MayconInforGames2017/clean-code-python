from src.view.song_register_view import SongRegisterView

# SongRegisterView -> Pascal Case (classes)
# song_register_process -> Snake Case (Funções, métodos, variaveis)

def song_register_process():
    song_register_view = SongRegisterView()

    new_song_informations = song_register_view.registry_song_initial()
    # Enviar new_song_informations para controller