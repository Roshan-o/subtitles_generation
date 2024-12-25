
# import openai as  
# api_key="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"

import whisper as w

# can set "small" "medium" "large"
path="test.mp4"


model=w.load_model("base")
def transcribe_aud(path):
    result=model.transcribe(path,word_timestamps=True)
    
    # return
        # -text=pure text
        # -words: each word along with their timestamps
    j=0
    new_list=[]
    seg_l=len(result["segments"])
    while j<seg_l:
        words_with_t=result["segments"][j]["words"]
        i=0
        n=len(words_with_t)
        while i<n:
            word_info=words_with_t[i]
            start_t=word_info["start"]
            end_t=word_info["end"]
            str=word_info["word"]
            while len(str)<=20 and(end_t-start_t)<=3:
                i=i+1
                if i>=n:
                    break
                word_info=words_with_t[i]
                start_t=word_info["start"]
                end_t=word_info["end"]
                str2=word_info["word"]
                str=str+str2
            new_list.append({'word':str,'start':start_t,'end':end_t})
            i=i+1
        j=j+1
    return new_list,result

if __name__ == "__main__":
    new_list,result=transcribe_aud(path)
    print(result["text"])
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print(new_list)
    

# two criteria
# 1)20 words in a sentense
# or
# 2)crosses 3 sec

# other way
# 1)search for the '.'-nothing but the end of the sentence
# 2)not geater that 20 charcters
# 3)doesn't crosses 3 sec's 


