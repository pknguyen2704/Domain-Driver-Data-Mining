from utils import *
stopwords_file_path = "../vietnamese-stopwords/vietnamese-stopwords.txt"

stopwords = []
with open(stopwords_file_path, "r", encoding="utf-8") as file:
    stopwords = [line.strip() for line in file if line.strip()]

# print(stopwords)
text="Đây là một đoạn văn mẫu với nhiều từ không cần thiết như là, hoặc, và."
rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir='../VnCoreNLP')
output = rdrsegmenter.word_segment(text)
print(output)
# Tách từ và loại bỏ stopword sử dụng underthesea
def remove_stopwords_underthesea(text, stopwords):
    tokens = word_tokenize(text, format="text").split()
    filtered_tokens = [token for token in tokens if token.lower() not in stopwords]
    return " ".join(filtered_tokens)

result_1 = remove_stopwords_underthesea(text, stopwords)
print(result_1)
#tách từ sử dụng VncoreNLP
# def remove_stopwords(text, stopwords):
#     # Tách từ
#     segmented_text = rdrsegmenter.word_segment(text)
#     words = segmented_text
#     # Loại bỏ stopword
#     filtered_words = [word for word in words if word.lower() not in stopwords]
#     return " ".join(filtered_words)

# result = remove_stopwords(text, stopwords)
# print(result)