# playlist_transfer
site to transfer playlists
get_all_playlists строка 150 self.missing_playlist: #КОСТЫЛЬ: количество плейлистов стоящих подряд которые были удалены (при создании плелиста в данные пользователя передатся значение kind начинающийся с 1000 и каждый новый плелист будет равен текущему kind+1, при этом kind будет обновлен, как следствие, если пользователь удалил свой плейлист где-то в середине, kind у остальных не поменяется на kind-1, поэтому появится пустой запрос, для этого и нужна эта переменная, чтобы отслеживать сколько пустых плейлистов должно стоять подряд, чтобы завершить цикл. с помощью этой перменной можно сделать утечку плелистов наименьшей...) 