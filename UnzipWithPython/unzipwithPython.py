import zipfile

zippedFilePath = r"C:\myZipAnimationData\animation.csv.zip"
unzipPath = r"C:\myUnzipAnimationData"


with zipfile.ZipFile(zippedFilePath) as f:
    ro = f.extractall(path = unzipPath)

with open(rf"{unzipPath}\animation.csv", "r") as f:
    print(f.readline())

