import argostranslate.package
from argostranslate import translate

# By default, the Whisper API only supports files that are less than 25 MB

# argostranslate.package.install_from_path('translate-en_es.argosmodel')
def trans(from_lang,to_lang):
    # from_lang="en"
    # to_lang="ur"

    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_lang and x.to_code == to_lang, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

    translated_text = translate.translate("Hello, world!", from_lang, to_lang)
    print(translated_text)

if __name__=='__main__':
    file_size_mb=50
    duration_ms=100000 #100sec
    chunk_size_in_mb=25
    size_per_sec=((file_size_mb)/duration_ms)*1000
    time_for_each_chunk=((chunk_size_in_mb) // size_per_sec)*1000
    print(size_per_sec)
    print(time_for_each_chunk)

