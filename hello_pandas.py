import pandas as pd


hoge = "Ohio"
header1 = "state"

data = {f'{header1:30}': [f'{hoge:20}', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print(f"【支出】\n{frame.to_string(index=False)}")
