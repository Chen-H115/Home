from pydocx import PyDocX
import sys, os, time, shutil, docx

def git_push():
    os.system('git add .')
    os.system("git commit -m'backup'")
    os.system('git push')

def rename(str):
    new_str = ''
    index = 0
    for i in str:
        if str[index] == '.' and str[index + 1] == 'd' and str[index + 2] == 'o' and str[index + 3] == 'c' and str[index + 4] == 'x':
            break
        new_str  = new_str + i
        index += 1
    return new_str

def main():
    file = "../../../../Desktop/blog"
    before = dict ([(f, None) for f in os.listdir (file)])
    while True:
        time.sleep(1)
        after = dict([(f, None) for f in os.listdir(file)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]

        if added:
            print("Added:", ", ".join(added))

            #get(Date)
            date = time.strftime("%m-%d-%Y %H:%M", time.localtime())
            print(date)

            #get(Header Lead Label)
            doc = docx.Document(file + "/" + " ".join(added))
            fullText = []
            header = doc.paragraphs[0].text
            label = doc.paragraphs[2].text
            lead = doc.paragraphs[4].text
            print(header)
            print(label)
            print(lead)
            type(lead)

            name = rename(" ".join(added))

            #make contents
            html = PyDocX.to_html(file + "/" + " ".join(added))
            f = open("article/" + name + ".html", 'w', encoding="utf-8")
            f.write(html)
            f.close()

            #make pages
            shutil.copy("blog-example.html","article/bolg-" + name + ".html")
            temp = open("article/bolg-" + name + ".html", "r+")
            str = '<div class="content"><object class="text" data="' + name + '.html"></object></div></body></html>'
            temp.seek(0, 2)
            temp.write(str)
            temp.close()

            #get(URL)
            url = "article/bolg-" + name + ".html"
            print(url)

            #write all elements(Date URL Header Label Lead)
            blogIndex = open("blog-index.txt",'a+')
            DUHLL = date + "⊠" + url + "⊠" + header + "⊠" + label + "⊠" + lead + "⊠" + "\n"
            blogIndex.write(DUHLL)
            blogIndex.close()

            after = dict([(f, None) for f in os.listdir(file)])

            print('test...................')


            indexHtml = '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no"><title>Blog</title><link rel="stylesheet" href="../css/reset.css"><link rel="stylesheet" href="../css/sub-pages.css"><link rel="stylesheet" href="../font-awesome/css/font-awesome.min.css"></head><body><head><nav><ul><li class="logo"><a href="../index.html">Hao</a></li><li id="sidebar_trigger"><a href="#">MENU<a></li></ul></nav></head><div class="content"><div class="function"><p>test..........</p></div>'

            for line in open("blog-index.txt", "r"):
                tempDate = ''
                tempURL = ''
                tempHeader = ''
                tempLabel = ''
                tempLead = ''
                for i in line[0:[i for i, x in enumerate(line) if x == '⊠'][0]]:
                    tempDate = tempDate + i
                print(tempDate)
                for i in line[[i for i, x in enumerate(line) if x == '⊠'][0] + 1:[i for i, x in enumerate(line) if x == '⊠'][1]]:
                    tempURL = tempURL + i
                print(tempURL)
                for i in line[[i for i, x in enumerate(line) if x == '⊠'][1] + 1:[i for i, x in enumerate(line) if x == '⊠'][2]]:
                    tempHeader = tempHeader + i
                print(tempHeader)
                for i in line[[i for i, x in enumerate(line) if x == '⊠'][2] + 1:[i for i, x in enumerate(line) if x == '⊠'][3]]:
                    tempLabel = tempLabel + i
                print(tempLabel)
                for i in line[[i for i, x in enumerate(line) if x == '⊠'][3] + 1:[i for i, x in enumerate(line) if x == '⊠'][4]]:
                    tempLead = tempLead + i
                print(tempLead)
                tempStr = '<article class="post"><header><h1><a class="header" href="' + tempURL + '">' + tempHeader + '</a></h1><p><time datetime="' + tempDate + '">' + tempDate + '</time></p></header><div class="lead"><p>' + tempLead + '</p></div><a class="read-more" href="' + tempURL + '">read more</a></article>'
                print(tempStr)
                indexHtml = indexHtml + tempStr
            indexHtml = indexHtml + '</div></div><footer><ul class="share"><li><a href="https://github.com/Chen-H115?tab=repositories" style="color: #ffffff"><i class="fa fa-2x fa-github"></i></a></li><li><a href="https://www.youtube.com/channel/UC-K_8rTxmXDwa1g9oXszp3Q?view_as=subscriber" style="color: #ffffff"><i class="fa fa-2x fa-youtube-square"></i></a></li><li><a href="" style="color: #ffffff"><i class="fa fa-2x fa-instagram"></i></a></li></ul><div class="copy-right">&copy Hao -- 2019</div></footer><div class="mask"></div><div id="sidebar"><ul><li><a href="../project/project-index.html">Project</a></li><li><a href="https://www.youtube.com/channel/UC-K_8rTxmXDwa1g9oXszp3Q?view_as=subscriber">Video</a></li><li><a href="blog-index.html">Blog</a></li></ul></div><script type="text/javascript" src="../js/jquery-3.3.1.min.js"></script><script type="text/javascript" src="../js/main.js"></script></body></html>'
            temp = open("blog-index.html", "w")
            temp.write(indexHtml)
            temp.close()

            git_push()
        if removed:
            print("Removed:", ", ".join(removed))

        before = after


if __name__ == "__main__":
    main()
