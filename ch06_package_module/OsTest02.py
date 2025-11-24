import os

targetFolder = 'd:\\'
parentPath = os.path.join(targetFolder, 'exercise')
print(parentPath)
try :
    os.mkdir(parentPath)
    FolderList = ['alpha', 'bravo', 'delta', 'nova', 'terra', 'pixel', 'orbit', 'matrix', 'spark', 'fusion']

    # 반복문을 사용하여 하위 폴더 10개를 만들어 봅니다.
    for forder in FolderList:
        # zfill : 0을 () 숫자만큼의 자리수로 만들어 채워라
        newFolder = os.path.join(parentPath,forder)
        # print(newFolder)
        os.mkdir(newFolder)

except FileExistsError :
    print('해당 디랙토리가 이미 존재합니다.')
# end try