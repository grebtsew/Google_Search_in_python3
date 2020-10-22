import googlesearch # pip install google
from google_images_download import google_images_download   #importing the library
import requests
import bs4
import os

'''
DOWNLOAD

Download url as html file

Returns path
'''
def Download(url_list, path, out_format):

    list = []

    for url in url_list:
        try:
            r = requests.get(url)

            html = bs4.BeautifulSoup(r.text, features="lxml")

            if not os.path.exists(path +"/"):
                os.makedirs(path +"/")


            file_path = path +"/" + html.title.text.replace(" ", "_").replace("|","")+ '.' + out_format

            list.add(file_path)
            f = open(file_path, 'wb')
            f.write(r.text.encode('utf-8'))
            f.close
        except Exception as e:
            print(str(e))

    return list

'''
DISTANCE

Get google distance between words

Returns float
'''
def Distance(term1,term2):
    return googlesearch.ngd(term1, term2)

'''
GET RANDOM USER AGENT

Get a random user agent string.

Return string
'''
def get_user_agent():
 return googlesearch.get_random_user_agent()[source]

'''
GET HITS

This function return the amount of hits on search query

Return int
'''
def get_hits(query, tld='com', lang='sv', tbs='0', safe='off', domains=None, extra_params={}, tpe='', user_agent=None):
    return googlesearch.hits(query, tld, lang, tbs, safe, domains, extra_params, tpe, user_agent)

'''
SEARCH

This is a simplified search function implementation.
I added some parameters to make it more generic towards google and google_search_image import.
I have not experimented with all different parameters.
Code assume from examples on the imported libraries github repos.

ARGUMENTS:

    query (str) – Query string. Must NOT be url-encoded.
    tld (str) – Top level domain.
    lang (str) – Language.
    tbs (str) – Time limits (i.e “qdr:h” => last hour, “qdr:d” => last 24 hours, “qdr:m” => last month).
    safe (str) – Safe search.
    num (int) – Number of results per page.
    start (int) – First result to retrieve. or None
    stop (int) – Last result to retrieve. Use None to keep searching forever.
    of str or None domains (list) – A list of web domains to constrain the search.
    pause (float) – Lapse to wait between HTTP requests. A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP. Your mileage may vary!
    only_standard (bool) – If True, only returns the standard results from each page. If False, it returns every possible link from each page, except for those that point back to Google itself. Defaults to False for backwards compatibility with older versions of this module.
    of str to str extra_params (dict) – A dictionary of extra HTTP GET parameters, which must be URL encoded. For example if you don’t want Google to filter similar results you can set the extra_params to {‘filter’: ‘0’} which will append ‘&filter=0’ to every query.
    tpe (str) – Search type (images, videos, news, shopping, books, apps) Use the following values {videos: ‘vid’, images: ‘isch’, news: ‘nws’, shopping: ‘shop’, books: ‘bks’, applications: ‘app’}
    or None user_agent (str) – User agent for the HTTP requests. Use None for the default.
    type - Changes which function to use.

    ----- For images only -----
    path -  if download is active, path will discribe output directory
    rights - (str) - Values labeled-for-reuse-with-modifications,labeled-for-reuse, labeled-for-noncommercial-reuse-with-modification,labeled-for-nocommercial-reuse
    download - Download html, pdf or image,    Takes a set of urls and tries to download them to path, If path is None, won't save on drive, Return reference list to images, Path file to save to

    # Read more here: https://python-googlesearch.readthedocs.io/en/latest/
'''
def search(query,
    tld='com',
    lang='en',
    tbs='0',
    safe='off',
    num=10,
    start=0,
    stop=1,
    domains=None,
    pause=2.0,
    only_standard=False,
    extra_params={},
    tpe='',
    user_agent=None,
    type = 'none',
    rights = '',
    download = False,
    path = None,
    out_format = "html"):



    if (type == 'text' or type == 'none' or type is None): # normal search
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download(googlesearch.search(query,
                tld,
                lang,
                 tbs,
                 safe,
                 num,
                 start,
                 stop,
                 domains,
                 pause,
                 only_standard,
                 extra_params,
                 tpe,
                 user_agent), p, out_format)

        else:
            return googlesearch.search(query,
                tld,
                lang,
                 tbs,
                 safe,
                 num,
                 start,
                 stop,
                 pause,
                 domains, # country
                 
                 #only_standard,
                 extra_params, 
                 #tpe,
                 user_agent
                 #ssl
                 )
            '''
            Return type:

            generator of str
            Returns:
            Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''

    elif (type == 'image_home') : # image search
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download(googlesearch.search_images(query,
             tld,
             lang,
             tbs,
             safe,
             num,
             start,
             stop,
             pause,
             domains,
             only_standard,
             extra_params), p, out_format)
        else:
            return googlesearch.search_images(query,
             tld,
             lang,
             tbs,
             safe,
             num,
             start,
             stop,
             pause,
             domains,
             only_standard,
             extra_params)
        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    elif(type == 'image' or type == 'images'):

        response = google_images_download.googleimagesdownload()   #class instantiation

        if lang == "sv":
            language = "Swedish"
        else:
            language = "English"

        arguments = {
        "keywords":query,
        "limit":num,
        "print_urls":"false",
        "language":language
          }

          # add rights
        if rights in ["labeled-for-reuse-with-modifications",
         "labeled-for-reuse",
         "labeled-for-noncommercial-reuse-with-modification",
         "labeled-for-nocommercial-reuse" ]:
            arguments["usage_rights"] =  rights

        # add safe
        if safe == "true":
            arguments["safe_search"] = safe

        if download:
            if path is not None:
                arguments["output_directory"] = path

        else:
            arguments["no_download"] = "true"
            arguments["no_directory"] = "true"

        '''
        This one is a little special,
        Here we instead use google_images_download library
        Used to download images directly!
        '''

        return   response.download(arguments) #passing the arguments to the function


    elif (type == 'video' or  type == 'film' or type == 'movie') : # video search
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download(googlesearch.search_videos(query,
             tld,
             lang,
             tbs,
             safe,
             num,
             start,
             stop,
             pause,
             domains,
             only_standard,
             extra_params), p, out_format)
        else:

            return googlesearch.search_videos(query,
             tld,
             lang,
             tbs,
             safe,
             num,
             start,
             stop,
             domains,
             pause,
             only_standard,
             extra_params)

        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''

    elif (type == 'news') : # search news
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download(googlesearch.search_news(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params), p, out_format)
        else:
            return googlesearch.search_news(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)

        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    elif (type == 'lucky') : # i am luchy search
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download( googlesearch.lucky(query, tld, lang, tbs, safe, only_standard, extra_params, tpe), p, out_format)
        else:
            return googlesearch.lucky(query, tld, lang, tbs, safe, only_standard, extra_params, tpe)

        '''
        Return type:

        str
        Returns:

        URL found by Google.
        '''
    elif (type == 'shop') : #
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download( googlesearch.search_shop(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params), p, out_format)
        else:

            return googlesearch.search_shop(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)

        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    elif (type == 'app' or type == 'apps') : # search apps
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download( googlesearch.search_apps(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params), p, out_format)
        else:

            return googlesearch.search_apps(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)
        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    elif (type == 'books' or type == 'book') : # book search
        if download:
            p = "downloads"
            if path is not None:
                p = path
            return Download( googlesearch.search_books(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params), p, out_format)
        else:
            return googlesearch.search_books(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)
        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    else :
        raise Exception("Unsupported type as parameter to search function!")
