# heic-converter

A simple GUI tool for converting many HEIC images into JPEGs quickly.

![heic-converter GUI](heic-converter.png)

## Backstory

I had a friend who frequently needed to convert large amounts of `.heic` (and `.heif`) images into JPEGs, so I made this tool to do it very quickly, and for very large amounts of files at once.

For this intended purpose, it will indeed get the job done. You can drop lots of files, or even better, an entire directory full of `.heic` files and JPEG copies will be made into the `~/h2j-converts` folder.

I thought about polishing this up to deploy it as a web app for people to use, but then I realized that Kivy (the Python library I used to make the UI) kind of sucks. So instead, I am simply releasing it here for anyone interested. 
