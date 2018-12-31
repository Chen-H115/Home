from pydocx import PyDocX
import sys, os, time, shutil

file = "article"
before = dict ([(f, None) for f in os.listdir (file)])

while True:
    time.sleep(1)
    after = dict([(f, None) for f in os.listdir(file)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]

    if added:
        print("Added:", ", ".join(added))
        html = PyDocX.to_html("article/" + " ".join(added))
        f = open("article/" + " ".join(added) + ".html", 'w', encoding="utf-8")
        f.write(html)
        f.close()
        shutil.copy("blog-example.html","article/bolg." + " ".join(added) + ".html")
        temp = open("article/bolg." + " ".join(added) + ".html", "r+")
        str = '<div class="content"><object class="text" data="test.html"></object></div></body></html>'
        temp.seek(0, 2)
        temp.write(str)
        temp.close()
        after = dict([(f, None) for f in os.listdir(file)])
        os.system('git add .')
        os.system("git commit -m'backup'")
        os.system('git push')
    if removed:
        print("Removed:", ", ".join(removed))

    before = after
