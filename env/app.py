#-*- coding: utf-8 -*-


from time import sleep
from pytube import YouTube
from pytube import Playlist
from pytube import Channel

class Youtube_Download:
    def SingleVideoDownload(link):
        try:
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            print('Baixando Video...')
            stream.download()
            print('------ Download Concluido ------')
            Youtube_Download.opcoes()
        except KeyboardInterrupt:
            print('Download cancelado pelo usuario!')
            print('\n\n')
            Youtube_Download.opcoes()
        finally:
            print('Erro ao efetuar o download\n')
            print('\n\n')
            Youtube_Download.opcoes()

    def PlaylistDownload(link):
        try:
            p = Playlist(link)
            print(f'baixando playlist {p.title}')
            for video in p.videos:
                stream = video.streams.get_highest_resolution()
                print(f"video: {video.title}")
                print('Download em andamento...')
                stream.download(f'{p.title}/') 
                print('------ Download Concluido ------')
            print('Download efetuado com sucesso!')
            print('\n\n')
            Youtube_Download.opcoes()

        except KeyboardInterrupt:
            print('Download cancelado pelo usuario!')
            print('\n\n')
            Youtube_Download.opcoes()
        finally:
            print("Erro ao efetuar download!\n")

    def ChannelDownload(link):
        try:
            c = Channel(link)
            print(f'Baixando Canal: {c.channel_name}')
            for video in c.videos:
                stream = video.streams.get_highest_resolution()
                print(f"Baixando video: {video.title}")
                print('Download em andamento...')
                stream.download(f'{c.channel_name}/')
                print('------ Download Concluido ------')
            print('Download efetuado com sucesso!')
            print('\n\n')
            Youtube_Download.opcoes()
            
        except KeyboardInterrupt:
            print('Download cancelado pelo usuario!')
            print('\n\n')
            Youtube_Download.opcoes()
        finally:
            print("Erro ao efetuar download!\n")

    def opcoes():

        print('[1] para baixar um único video\n[2] para baixar uma Lista de Reprodução\n[3] para baixar o canal inteiro')
        print()
        print('*** Pressione Ctrl - C para cancelar o download ***')
        print()

        op = input("Digite a opção: ")

        if int(op) == 1:
            link = input("Digite o link do video: ")
            Youtube_Download.SingleVideoDownload(link)

        elif int(op) == 2:
            link = input('Digite o link da lista de reprodução: ')
            Youtube_Download.PlaylistDownload(link)

        elif int(op) == 3:
            link = input("Digite o link do canal: ")
            Youtube_Download.ChannelDownload(link)

if __name__ == "__main__":
    Youtube_Download.opcoes()