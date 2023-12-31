# Meme Generator

Meme Generator web app / CLI that creates memes with user-uploaded images and custom captions...

## Prerequisites

- pip
- python 3

## How to setup

```
$ pip install -r requirements.txt
```

Notes: the `requirement.txt` was generated from

```
$ pipreqs --force
```

for minimal dependencies list

## How to run

- Create meme with command line.

```
$ python meme.py
```

Meme will be stored inside tmp folder.

- Create meme with web app browser (http://127.0.0.1:5000)

```
$ python app.py
```

Meme will be stored inside static folder.
