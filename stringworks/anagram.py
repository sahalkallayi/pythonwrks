
source_word="listen"

target_word="silent"

#sorted_source=sorted(source_word)

#sorted_target=sorted(target_word)

#if sorted_source==sorted_target:

    #print(sorted_source==sorted_target)


def is_anagram(word1,word2):

    return sorted(word1)==sorted(word2)

print(is_anagram(source_word,target_word))


