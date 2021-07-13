#!/bin/sh
pyinstaller __main__.py --name images-to-pdf.out --onefile -w
rm -r -f -d build
rm *.spec