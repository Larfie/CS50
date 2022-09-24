filename = input("Enter your filename: ").strip().lower()

if "." in filename:
    suffix = filename.rsplit(".", 1)[1]
else:
    suffix = ""

if suffix == "gif":
    print("image/gif")
elif suffix == "jpg" or suffix == "jpeg":
    print("image/jpeg")
elif suffix == "png":
    print("image/png")
elif suffix == "pdf":
    print("application/pdf")
elif suffix == "txt":
    print("text/plain")
elif suffix == "zip":
    print("application/zip")
else:
    print("application/octet-stream")