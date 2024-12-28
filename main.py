import translate_t as translate
import chunks_divide as process


if __name__ == "__main__":
    path="test.mp4"
    final_sub=process.final_time(path) # final processed subtitles with correct timestamps
    # print(final_sub)
    # translate_sub=translate.translate_full(final_sub)
    # print(translate_sub)
    process.time_to_SRT("before_trans.srt",final_sub,path)
    # process.time_to_SRT("after_trans.srt",translate_sub,path)
