# TranslationMachineMultiLingoual
for English to German and French we used t5-small model and this needs to be run with tensorflows==4.17
for Persian and Hindi you can use the latest update of transformers 
# Huggingface AIPI
you need to install these libraries :
transformers
gradio
torch
sentencepiece(required for Hindi and Persian)

# demo 
https://huggingface.co/spaces/barghavani/translation_machin_en_to_multi_languages
 Model :
 1- persiannlp/mt5-base-parsinlu-opus-translation_fa_en
 2- t5-small


 datasets:
 "opus_books", "en-fr"
 bbaaaa/iwslt14-de-en
 persiannlp/parsinlu_translation_en_fa
 cfilt/iitb-english-hindi
