virtualenv LegoEnv
LegoEnv\Scripts\activate
conda.bat deactivate

cd ProblemStatement



pip install -r requirements.txt
This is for me : pip list -> full_reqs.txt

# https://openbase.com/python/legofy/documentation
Usage: legofy [OPTIONS] IMAGE [OUTPUT]

InputImg.jpeg

$ legofy --palette solid InputImg.jpeg
$ legofy --palette transparent InputImg.jpeg
$ legofy --palette effects InputImg.jpeg
$ legofy --palette all InputImg.jpeg
legofy --palette mono InputImg.jpeg InputImg_monolego.jpeg

  Legofy an image!

Options:
  --size INTEGER                  Number of bricks the longest side of the legofied image should have.
  --dither / --no-dither          Use dither algorithm to spread the color approximation error.
  --palette [all|effects|mono|solid|transparent]
                                  Palette to use based on real Lego colors.
  --help                          Show this message and exit.


legofy --palette all InputImg.jpeg --dither OutputImgdit1.jpeg
legofy --palette all InputImg.jpeg --no-dither OutputImgdit2.jpeg

legofy --palette all InputImg.jpeg  --size 90 OutputImgsiz02.jpeg

legofy --palette mono InputImg.jpeg  --size 90 --no-dither OutputImgsiz01.jpeg

legofy --palette mono InputImg.jpeg  --size 450 --no-dither OutputImgsiz03.jpeg

legofy --palette all InputImg.jpeg  --size 450 OutputImgsiz450.jpeg