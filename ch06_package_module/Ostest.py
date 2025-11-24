import os
#
# save_path = input('생성할 폴더 이름 입력 : ')
#
#
# if not os.path.isdir(save_path): # 폴더가 존재하지 않는 경우
#     os.mkdir(save_path)
# else:
#     print(f'{save_path} 폴더는 존재합니다.')
# # end if

# 특정 디렉토리에 하위 디렉토리 여러 개 생성하기
targetFolder = 'd:\\' # \는 특수문자라서 \\라고 표시해야합니다.
parentPath = os.path.join(targetFolder, 'sample')
print(parentPath)

try :
    os.mkdir(parentPath)

    # 반복문을 사용하여 하위 폴더 10개를 만들어 봅니다.
    for idx in range(1,11):
        # zfill : 0을 () 숫자만큼의 자리수로 만들어 채워라
        newFolder = os.path.join(parentPath,'folder'+str(idx).zfill(2))
        # print(newFolder)
        os.mkdir(newFolder)

except FileExistsError :
    print('해당 디랙토리가 이미 존재합니다.')
# end try