from jamo import h2j, j2hcj
from jamo_extension import *

text = '안녕하세요 얂녱화쒜욝'
text = j2hcj(h2j(text))

print(f'Before Processing: {text}')

text = double_moum_decomp(text)
print(f'After Double-Moum-Decomp: {text}')

text = double_moum_merge(text)
print(f'Reconstruction: {text}')