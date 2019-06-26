## python-ipstack
python-ipstack provides an object wrapper for IPStack (ipstack.com) https requests and responses. You will need an api access key from ipstack.com to use this library.

#### Example:

    >>> from ipstack import IPStack
    >>> ip = IPStack('134.201.250.155', YOUR_ACCESS_KEY)
    >>>
    >>> print(ip.city)
    >>> Toronto
    
There are also two helper methods:

`IPStack.get_ip_address_from_headers(headers: dict)`

`IPStack.lookup_ip_info(ip_address: str, ip_stack_api_key: str)`


#### Run Tests:

`python -m unittest test_ipstack`



    
