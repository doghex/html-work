import re
file_object = open('C:/Users/root/source/text.txt','r',encoding='UTF-8')
file_context = file_object.read()
pattern = re.compile(r'\d{1,2}[ ]<.*|\d{1,2}[ ][A-Za-z0-9"].*>')
m = pattern.findall(file_context)
file_new = open('C:/Users/root/source/texxt.html','w',encoding='utf-8')
for b in m:
    del_head = re.sub(r'\d{1,2}[ ]<div class=".*"></div>', ' ', b)
    del_head=re.sub(r'</html>|</body>','',del_head)
    del_head = re.sub(r'</head>', '<link rel="stylesheet" type="text/css" href="css/css.css" /></head>', del_head)
    del_head = re.sub(r'<!--footer end-->', '</html></body>', del_head)
    num=re.sub(r'\d{1,2}[ ]',' ',del_head)
    print("num"+num)
    file_new.write(num)
    file_new.write('\n')#显示写入换行
#heml END<link rel="stylesheet" type="text/css" href="theme.css" />
#css STAR
css_new = open('C:/Users/root/source/css/css.css','w',encoding='utf-8')
css_pattern=re.compile(r'\d{1,2}[ ]\..*|\d{1,2}[ ].*:.*;|\d{1,2}[ ]\}')
c = css_pattern.findall(file_context)
#print(' css\n')
for a in c:
    csss=re.sub(r'^\d{1,2}[ ]','\n',a)
    csss=re.sub(r'.header{', '*{margin:0;padding:0;border:0;list-style: none;}\nbody{font-family: "微软雅黑";font-size: 16px;color:#404042;}\n a{text-decoration: none;color:#fff;} \n .header{',csss)
    csss = re.sub(r'.head{',
                  '*{margin:0;padding:0;border:0;list-style: none;}\nbody{font-family: "微软雅黑";font-size: 16px;color:#404042;}\n a{text-decoration: none;color:#fff;} \n .head{',
                  csss)
    print(csss)
    css_new.write(csss)
    css_new.write('\n')#显示写入换行
#css END
file_new.close()
file_object.close()
