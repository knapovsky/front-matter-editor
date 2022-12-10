import frontmatter
from os import listdir
from os.path import isfile, join
import datetime

import codecs #this is nasty...

"""
Bulk edit function for tags in Jekyll posts.

The script will attempt to edit and OVERWRITE ALL FILES
in the specified folder:
you should place selected files in a temporary folder.
"""

# -------  INPUT PARAMETERS --------------

# TEMPORARY folder with selected files
# (do not specify the main _posts folder!)
folder = 'input/'

add_tag = 'Notesheet' #tag to be insereted

remove_tag= '' #tag to be removed

# ----------- ENGINE --------------------

for f in listdir(folder):

    file = join (folder, f)

    if not isfile(file): continue

    print (file)

    post = frontmatter.load (file)

    #print (post['title'])
    oldtitle = f
    title = f[:-3].replace("_"," ")
    title = title.replace(" - Chords", "")
    post['title'] = title

    if remove_tag :
        try:  post['tags'].remove(remove_tag)
        except: pass

    if add_tag:
        print('Adding tags')
        try:
            if add_tag not in post['tags'] :
                post['tags'] += [add_tag]
        except:
            # tags do not exist yet
            post.metadata['tags'] = [add_tag]

    if title.find("Chords"):
        if 'Chords' not in post['tags']:
            post['tags'] += ['Chords']

    post['date'] = datetime.datetime(2022, 12, 10, 3, 18, 48, 631729)
    post['dateCreated'] = datetime.datetime(2022, 12, 10, 3, 18, 48, 631729)
    post['description'] = 'Notesheet'
    post['editor'] = 'markdown'
    post['slug'] = oldtitle[:-3].lower()

	# this is the output in text format
    out = frontmatter.dumps(post)

    # https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python/934203#934203
    o = codecs.open(file, 'w', 'utf-8')
    o.write(out)
    o.close()