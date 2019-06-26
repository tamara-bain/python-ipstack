# python-ipstack
python-ipstack provides an object wrapper for IPStack (ipstack.com) https requests and responses. 

#### Example:

    >>> from ipstack import IP
    >>> ip = IP('134.201.250.155', YOUR_ACCESS_KEY)
    >>>
    >>> print(ip.city)
    >>> Toronto
    
There are also two helper methods:

`IP.get_ip_address_from_headers(headers: dict)`

`IP.lookup_ip_info(ip_address: str, ip_stack_api_key: str)`


    
