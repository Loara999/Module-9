def all_variants(text:str):
    flag = True
    step = 1
    while flag:
        for i in range(len(text)):
            if  i + step <= len(text):
                yield text[i:i+step]
            else:
                yield text
                flag = False
                break
        step += 1

Gen = all_variants('abc')
print(Gen)
for elem in Gen:
    print(elem)