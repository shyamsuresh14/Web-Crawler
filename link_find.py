from html.parser import HTMLParser
from urllib import parse

class link_finder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':                           #a link start tag
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)       #baseurl + relative_url
                    self.links.add(url)
        elif tag == 'script':
            for (attribute,value) in attrs:
                if attribute == 'src':
                    url = parse.urljoin(self.base_url, value) 
                    self.links.add(url)     

    def links_in_page(self):
        return self.links

    def error(self,message):
        pass         

#find = link_finder('ooo','ooo')
#find.feed('<html><head><title>hello</head></title></html>')        
#find.feed('<script type="text/javascript" src="http://moodlecc.vit.ac.in/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js&amp;rollup/1520398157/mcore-min.js"></script>')
#print(find.links_in_page())