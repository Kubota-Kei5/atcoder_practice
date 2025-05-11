# %%
# X/10の計算でfloatになった場合、16桁の程度の精度しか持たない。
# そのため、このコードでは10の18乗のような桁数の入力があった場合に誤差が発生する。
import math
X=int(input())

print(math.ceil(X/10))

# %%
# このコードでAC
X = int(input())
print((X + 9) // 10)
