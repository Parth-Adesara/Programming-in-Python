input()
marks_list = map(int, input().split())
no_dubs_marks_list = list(set(marks_list))
no_dubs_marks_list.sort(reverse=True)

print(no_dubs_marks_list[1])
