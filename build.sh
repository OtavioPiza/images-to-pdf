#!/bin/sh
pyinstaller __main__.py --name images-to-pdf --onefile
mv ./dist/images-to-pdf .
rm -r -f -d dist build
rm images-to-pdf.spec