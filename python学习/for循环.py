# text=input("请输入你要加密的文字：")
# secret=""
# for n in text:
#     result=ord(n)
#     secret+=chr(result+1)
# print(f"你加密的文字为：{secret}")

secret=input("请输入你要解密的文字：")
text=""
for n in secret:
    result=ord(n)
    text+=chr(result-1)
print(f"你解密的文字为：{text}")