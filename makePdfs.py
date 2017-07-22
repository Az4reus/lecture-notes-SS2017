#!/usr/bin/env python3

from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import sh

def make_pdf(filename):
    parent = str(list(filename.parents)[0])
    file_parent = ''
    if parent.endswith('algebra'): 
        file_parent = 'LA-'
    elif parent.endswith('datastructures'):
        file_parent = 'GAD-'

    sh.pandoc(f'{filename}', '-f', 'markdown', '-t', 'latex',
              '-o', f'/Users/az/Uni/pdf/{file_parent}{filename.stem}.pdf', 
              '-S', '--latex-engine=xelatex')

def markdown_files():
    cwd = Path('/Users/az/Uni/')
    return cwd.glob('**/*.md')

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(make_pdf, f) for f in markdown_files()}
        _ = [id(f) for f in futures]
