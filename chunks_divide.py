from pydub import AudioSegment as As
import os
import video_sub_caps as vsc
def audio_info(file_path):
    # Load the audio file
    audio = As.from_file(file_path,format="mp4")
    # File size in MB
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    
    # Sampling rate
    sampling_rate = audio.frame_rate  # in Hz
    
    # Number of channels
    num_channels = audio.channels

    # Duration in seconds (optional)
    # duration_seconds = len(audio) / 1000
    
    # Duration in milliseconds
    duration_ms = len(audio)

    sample_width = audio.sample_width  # Bytes per sample (e.g., 2 for 16-bit audio)
    
    # Bit depth
    bit_depth = sample_width * 8 

    return file_size_mb, sampling_rate, num_channels, duration_ms,bit_depth


def segdivide(file_path,chunk_size_in_mb=24):
    
    names=[]
    audio = As.from_file(file_path,format="mp4")
    file_size_mb,sampling_rate,num_channels,duration_ms,bit_depth=audio_info(file_path)
    if file_size_mb<=24:
        audio.export("chunk_0",format="mp3")
        names.append("chunk_0")
        return names

    # Size per second (bytes)=Sample rate×Bit depth (bytes)×Channels
    # time_for_chunk_size_in_mb= chunk_size_in_mb / size_per_second
    # size_per_sec=(sampling_rate*bit_depth*num_channels)//(1024*1024)
    # time_for_each_chunk=(chunk_size_in_mb*1000//size_per_sec) 
    # *1000 to convert it into milli seconds
    # getting wrong using this

    # size_per_second(mb)=file_size_mb/duration_in_sec
    # time_for_each_chunk=(chunk_size_in_mb)/size_per_sec
    size_per_sec=((file_size_mb)/duration_ms)*1000
    time_for_each_chunk=((chunk_size_in_mb) // size_per_sec)*1000

    segments=[]
    # print(len(audio))
    # time_for_each_chunk=10000 #in ms
    for i in range(0,len(audio),time_for_each_chunk):
        if (i+time_for_each_chunk)>len(audio):
            segments.append(audio[i:len(audio)])
        else:
            segments.append(audio[i:i+time_for_each_chunk])
        print(len(segments[len(segments)-1]))
    
    for idx, segment in enumerate(segments):
        segment.export(f"chunk_{idx + 1}.mp3", format="mp3")
        names.append(f"chunk_{idx + 1}.mp3")
    return duration_ms,names

def convert_chunk(names):
    final_sub=[]
    i=0
    for nm in names:
        new_list,result=vsc.transcribe_aud(nm,i)
        final_sub.extend(new_list)
        # aud=As.from_file(nm,format="mp3")

        # i=i+len(aud)
        # print(result["text"])
        os.remove(nm)
    return final_sub

def time_to_SRT(name,final_sub,path):
    # name="subtitles.srt"
    # name=input("enter name of su")
    audio=As.audio = As.from_file(path,format="mp4")
    total_time=len(audio)
    file=open(name,'w')
    for i in range(1,len(final_sub)+1,1):
        segment=final_sub[i-1]
        st=segment['start']
        ed=segment['end']
        if st-0.5>=0:
            st=st-0.5
        if ed+0.5<=total_time:
            ed=ed+0.5
        fst=sec_process(st)
        fed=sec_process(ed)
        if i!=1:
            file.write("\n")
        file.write(f"{i}\n")
        file.write(f"{fst} --> {fed}\n")
        file.write(f"{segment['word']}\n")


def sec_process(st):
    hr=int(st//(60*60))
    min=int((st%3600)//60)
    sec=int(st%60)
    stmill=round((st - int(st)) * (10**3))
    return f"{hr}:{min}:{sec},{stmill}"

def final_time(path):
    names=segdivide(path)
    final_sub=convert_chunk(names)
    return final_sub


if __name__ == "__main__":
    path="test.mp4"
    # names=segdivide(path)
    # new_list,result=vsc.transcribe_aud(path)
    # print(result["text"])
    final_sub=final_time(path)
    print(final_sub)
    # time_to_SRT(final_sub)
    # print("----------------------------------------------------------------------------------------------")
    # final_sub=convert_chunk(names)
    # print("----------------------------------------------------------------------------------------------")
    # print(final_sub)
