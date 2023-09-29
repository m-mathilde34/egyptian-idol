import os
import requests

from fastapi import FastAPI, File, UploadFile, Path

app = FastAPI()
urlList = ["https://collections.louvre.fr/media/cache/large/0000000021/0000000007/0000582334_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000038/0000077510_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000035/0000605804_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000096/0001057904_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000041/0000835058_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000048/0000579653_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000042/0000966184_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000203/0000835008_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000032/0000989864_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000040/0000157059_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000081/0000167228_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000023/0000966182_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000015/0000850367_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000017/0001183526_OG.JPG",
"https://collections.louvre.fr/media/cache/original/0000000021/0000000030/0000149503_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000228/0000835060_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000016/0000108128_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000012/0000847022_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000011/0000847020_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000013/0000847023_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000229/0000835063_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000708/0000583597_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000705/0000148160_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000701/0000907558_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000704/0000148166_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000703/0000148162_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000689/0000584838_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000687/0000584835_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000685/0000584867_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000683/0000584968_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000707/0000583596_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000706/0000907747_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000679/0000584935_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000688/0000584752_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000680/0000584936_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000681/0000584937_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000666/0000157256_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000676/0000584830_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000677/0000584831_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000678/0000584832_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000743/0000157788_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000722/0000584771_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000723/0000584772_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000724/0000584774_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000748/0000580741_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000709/0000583607_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000721/0000584770_OG.JPG",
"https://collections.louvre.fr/media/cache/original/0000000021/0000000741/0000154135_OG.JPG",
"https://collections.louvre.fr/media/cache/original/0000000021/0000000742/0000154134_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000718/0000584766_OG.JPG",
"https://collections.louvre.fr/media/cache/large/0000000021/0000000720/0000584768_OG.JPG"]

job_counter = 0
uploadFolder = "/upload/"
os.makedirs(uploadFolder, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/get_job")
async def get_job():
    global job_counter
    url = urlList[job_counter]
    job_counter += 1
    return {"job_url": url}

@app.get("/job_count")
async def job_count():
    return {"job_counter": job_counter}

@app.post("/img_upload")
async def img_upload(file: UploadFile):
    with open(os.path.join(uploadFolder, file.filename), "wb") as img:
        img.write(file.file.read())
    return {"status": "successful"}

@app.get("/img_download/")
async def img_download(url: str):
    response = requests.get(url)

    url_breakdown = url.split("/")
    filename = url_breakdown[-1]

    if response.status_code == 200:
        content = response.content
        with open(os.path.join(uploadFolder, filename), "wb") as img:
            img.write(content)
        return {"status": "successful"}
    else:
        return {"status": "failed"}

@app.get("/uploaded_content/")
async def uploaded_content():
    listUrls = os.listdir(uploadFolder)
    return {"uploaded_content": listUrls}