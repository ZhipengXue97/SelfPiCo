# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
contracts = self.extract_contracts(method)
if contracts:
    request_cls = Request
    for contract in contracts:
        if contract.request_cls is not None:
            request_cls = contract.request_cls

    # calculate request args
    args, kwargs = get_spec(request_cls.__init__)

    # Don't filter requests to allow
    # testing different callbacks on the same URL.
    kwargs["dont_filter"] = True
    kwargs["callback"] = method

    for contract in contracts:
        kwargs = contract.adjust_request_args(kwargs)

    args.remove("self")

    # check if all positional arguments are defined in kwargs
    if set(args).issubset(set(kwargs)):
        request = request_cls(**kwargs)

        # execute pre and post hooks in order
        for contract in reversed(contracts):
            request = contract.add_pre_hook(request, results)
        for contract in contracts:
            request = contract.add_post_hook(request, results)

        self._clean_req(request, method, results)
        exit(request)
