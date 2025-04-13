# Let's unzip the animation movies dataset [Here](https://www.kaggle.com/datasets/rajugc/imdb-movies-dataset-based-on-genre?select=animation.csv) 📽️

## 1️⃣ Import the `zipfile` module, or `pip install zipfile` first if you don't already have it

```python
import zipfile
```

## 2️⃣ Write the path of the file to be zipped in 'zippedFilePath' and the path to be unzipped to in `unzipPath`

```python
zippedFilePath = r"C:\myZipAnimationData\animation.csv.zip"
unzipPath = r"C:\myUnzipAnimationData"
```

## 3️⃣ Use the following context manager to unzip!

```python
with zipfile.ZipFile(zippedFilePath) as f:
    ro = f.extractall(path = unzipPath)
```

**Successfully unzipped!🎉 I checked the unzipPath on my computer and thers is a resulted file called _animation.csv_**

## 4️⃣ Use the following context manager to read the first line from the unzipped file

```python
with open(rf"{unzipPath}\animation.csv", "r") as f:
    print(f.readline())
```






