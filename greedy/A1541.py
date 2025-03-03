input_txt = input()
split_list = input_txt.split('-')

answer = sum(map(int, split_list[0].split('+')))
for chunk in split_list[1:]:
    answer -= sum(map(int, chunk.split('+')))
print(answer)


"""
aditional test cases

#1 괄호 2개인 케이스
1-100+10-10+30
-149

"""