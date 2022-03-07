from moviepy.editor import *
import os


def extract_audio():
    ## example: 视频中提取音频
    # video = VideoFileClip('test1.mp4')
    # audio = video.audio
    # audio.write_audiofile('test1.mp3')

    ## 有语音
    path_video = 'F:/项目/项目材料梳理模板-海事局项目/1.项目资料/（4）实验数据/2021-01-24-视频汇总/有语音'
    path_mp3_save = 'F:/desk_others/sound_separation/audio_original/'

    ## 无语音
    # path_video = 'F:/项目/项目材料梳理模板-海事局项目/1.项目资料/（4）实验数据/2021-01-24-视频汇总/无语音'
    # path_mp3_save = 'F:/desk_others/sound_separation/audio_original_non/'

    dirs = os.listdir(path_video)
    for file in dirs:   
        file_ID = file[:-4]
        dirs_save = path_video + '/'+ file 
        # 视频转语音
        video = VideoFileClip(dirs_save)
        audio = video.audio
        file_mp3_name = path_mp3_save + file_ID + '.mp3'
        print(file_mp3_name)
        audio.write_audiofile(file_mp3_name)

        # print
        print(file_ID)
        print(dirs_save)

def spleeter_separate():

    # 有声音
    path_audio = 'F:/desk_others/sound_separation/audio_original'
    save_separate_audio =  'F:/desk_others/sound_separation/audio_spleeter_separate'

    # 无声音
    path_audio = 'F:/desk_others/sound_separation/audio_original_non'
    save_separate_audio =  'F:/desk_others/sound_separation/audio_non_spleeter_separate'

    dirs = os.listdir(path_audio)
    for file in dirs: 
        dirs_save = path_audio + '/'+ file 
        print(dirs_save)
        
       
        ## example:音频中分离人声
        # command = 'spleeter separate -p spleeter:4stems -o output -i test.mp3'
        # os.system(command)
        ##
        command =  'spleeter separate -p spleeter:4stems' +' '+ '-o' + ' '+ save_separate_audio +' ' + '-i'+' '+ dirs_save
        print(command)
        os.system(command)
       


if __name__ == '__main__':
    # 从视频中提取音频
    # extract_audio()

    # 从音频中分离人声
    spleeter_separate()
 
   



   