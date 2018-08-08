from urllib.parse import urlparse

#getting the subdomain from a given url
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

#getting the domain name by removing the third level domain from the sub_domain
def get_domain_name(url):
    try:
        subdomain = get_subdomain_name(url)
        parts = subdomain.split('.')
        domain = ''
        for i in range(len(parts)):
            if parts[i] == 'www':
                for part in parts[i+1:len(parts)-1]:
                    domain = domain + part + '.'
                domain = domain + parts[len(parts) - 1]
        return domain
    except:
        return ''    
