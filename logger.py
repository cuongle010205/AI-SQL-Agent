from datetime import datetime

def log(question,sql):

    with open(
        "log.txt",
        "a",
        encoding="utf8"
    ) as f:

        f.write("="*50+"\n")

        f.write(str(datetime.now())+"\n")

        f.write(question+"\n")

        f.write(sql+"\n\n")