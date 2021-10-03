def song_sum_time(song_count):
    song_time = 0
    for i in range(song_count):
        song_name = input("Название {0} песни: ".format(i+1))
        if song_name in violator_songs:
            song_time += violator_songs[song_name]
    return round(song_time, 2)


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

song_count = int(input('Сколько песен выбрать? '))
print('Общее время звучания песен: {0} минут'.format(song_sum_time(song_count)))

