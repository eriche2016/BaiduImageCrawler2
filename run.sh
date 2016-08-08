#!/usr/bin/env bash

# run this file: ./run.sh
# may also need to run this command if necessary: 
#               chmod +x run.sh
# may specicy a list of key words to download 
declare -a key_words_list=('dog' 'woman') # download each key word images num_images 
if [ 1 -eq 1 ]; then
    for i in "${key_words_list[@]}"
    do
        new_path="./$i"
        python crawler.py -key_word '$i' \
                        -store_dir "$new_path" \
                        -num_images 10 \
                        -num_threads 5 
    done
fi
