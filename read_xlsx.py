import pandas as pd
import unicodedata as uni

# def func(x):
#     return f"{x:20}"

def name_format(text, text_len):
    if type(text) == str:
        half_sum_len = sum([(1, 2)[uni.east_asian_width(t) in 'FWA'] for t in text])
    else:
        half_sum_len = sum([(1, 2)[uni.east_asian_width(t) in 'FWA'] for t in str(text)])
    half_text_len = text_len * 2

    space_len = half_text_len - half_sum_len

    return f"{' ' * space_len}{text}"


df = pd.read_excel('sample.xlsx')

df["お店"] = df["お店"].apply(lambda x: name_format(x, 20))
df["商品名"] = df["商品名"].apply(lambda x: name_format(x, 20))
df["価格"] = df["価格"].apply(lambda x: name_format(x, 8))

print(df.to_string(index=0, header=False))

with open('hoge.txt', mode='w', encoding='utf_8') as f:
    f.write(df.to_string(index=0, header=False))