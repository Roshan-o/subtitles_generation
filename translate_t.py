
# import openai as trans
# trans.api_key="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"

# def translate_sent(text,target):
#     prompt = f"Translate the following text to {target}:\n\n{text}"
#     response=trans.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{
#             'role':'user',
#             'content':prompt,
#         }],
#     )
    
#     translation = response
#     return translation.strip() # .stripe() to remove leading and trailing white spaces

# def translate_full(final_sub):
#     target_language=input("enter LANGUAGE to which you want to translate:")
#     new_trans=final_sub
#     for seg in new_trans:
#         new_trans['word']=translate_sent(seg['word'],target_language)

#     return new_trans




# if __name__ == "__main__":
