# Copyright 2022, Jônatas Trabuco Belotti [jonatas.t.belotti@hotmail.com]

import sys
import os
import fitz # PyMuPDF
import io
from PIL import Image

if __name__ == "__main__":
    assert len(sys.argv) >= 2, "É obrigatório informar o PDF para extrair as imagens"
    assert len(sys.argv) >= 3, "É obrigatório informar a pasta de destino das imagens"
    arq_entrada = sys.argv[1]
    pasta_final = str(sys.argv[2])
    pasta_final += "/" if not pasta_final.endswith("/") else ""

    # Garantindo que a pasta existe
    os.makedirs(pasta_final, exist_ok=True)

    # open the file
    pdf_file = fitz.open(arq_entrada)

    # iterate over PDF pages
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.getImageList()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.getImageList(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open("%spg %02d - imagem %02d.%s" % (pasta_final, page_index+1, image_index, image_ext), "wb"))
