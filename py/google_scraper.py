import sys
import  requests, re
from    bs4 import BeautifulSoup 
 
def get_urls(search_string, start):
    temp        = []
    url         = 'http://www.google.com/search'
    payload     = { 'q' : search_string, 'start' : start, 'num':'100' }
    my_headers  = { 'User-agent' : 'Mozilla/11.0' }
    r           = requests.get( url, params = payload, headers = my_headers )
    soup        = BeautifulSoup( r.text, 'html.parser' )
    h3tags      = soup.find_all( 'h3', class_='r' )
    for h3 in h3tags:
        try:
            temp.append( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1) )
        except:
            continue
    return temp
 
def main():
    result    = []
    search    = sys.argv[1]
    pages     = sys.argv[2]
    fs        = sys.argv[3]
    for page in range( 0,  int(pages) ):
        result.extend( get_urls( search, str(page*100) ) )
    result    = list( set( result ) )
    thefile=open(fs,'w')
    for item in result:
        thefile.write("%s\n" % item)
    print( '\nTotal URLs Scraped : %s ' % str( len( result ) ) )
 
if __name__ == '__main__':
    main()
