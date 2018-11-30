
import jieba.posseg as pseg

file = open("../data/jiebaTest.txt","r",encoding="utf-8")
file = file.read()
words = pseg.cut(file)
file_list = []
for word, flag in words:
    word_flag_str = word + "/" + flag
    file_list.append(word_flag_str)
writer_str = " ".join(file_list)
# print(writer_str)
# print(" ".join(file_list))
writer_file = open("../data/result.txt","w",encoding="utf-8")
writer_file.write(writer_str)
writer_file.close()