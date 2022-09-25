"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

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