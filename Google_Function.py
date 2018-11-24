import googlesearch # pip install google

'''
DOWNLOAD

Download object, pdf or image
Takes a set of urls and tries to download them to path
If path is None, won't save on drive

Return reference list to images
'''

def download(urls, path= None):
    pass


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

def get_hits(query, tld='com', lang='en', tbs='0', safe='off', domains=None, extra_params={}, tpe='', user_agent=None):
    return googlesearch.hits(query, tld, lang, tbs, safe, domains, extra_params, tpe, user_agent)

'''
SEARCH

This is a simplified search function implementation.
I added some parameters to make it more generic towards google import.

'''

def search(query, tld='com',
    lang='en',
    tbs='0',
    safe='off',
    num=10,
    start=0,
    stop=5,
    domains=None,
    pause=2.0,
    only_standard=False,
    extra_params={},
    tpe='',
    user_agent=None,
    type = 'none'):

    '''
    google search
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
    '''

    if (type == 'text' or type == 'none' or type is None): # normal search
        return googlesearch.search(query,
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
             user_agent)
        '''
            Return type:

            generator of str
            Returns:
            Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''

    elif (type == 'image') : # image search

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

    elif (type == 'video' or  type == 'film' or type == 'movie') : # video search
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
        return googlesearch.search_news(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)

        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    elif (type == 'lucky') : # i am luchy search
        return googlesearch.lucky(query, tld, lang, tbs, safe, only_standard, extra_params, tpe)

        '''
        Return type:

        str
        Returns:

        URL found by Google.
        '''
    elif (type == 'shop') : #
        return googlesearch.search_shop(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)

        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    elif (type == 'app' or type == 'apps') : # search apps
        return googlesearch.search_apps(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)
        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    elif (type == 'books' or type == 'book') : # book search
        return googlesearch.search_books(query, tld, lang, tbs, safe, num, start, stop, domains, pause, only_standard, extra_params)
        '''
        Return type:

        generator of str
        Returns:

        Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
        '''
    else :
        raise Exception("Unsupported type as parameter to search function!")
