ret["comment"] = "\n".join(
                            [
                                (
                                    'Attempt {0}: Returned a result of "{1}", '
                                    'with the following comment: "{2}"'.format(
                                        retries, orig_ret["result"], orig_ret["comment"]
                                    )
                                )]
)
ret["comment"] = "  ".join(
                    [
                        "" if not ret["comment"] else ret["comment"],
                        (
                            "The state would be retried every {1} seconds "
                            "(with a splay of up to {3} seconds) "
                            "a maximum of {0} times or until a result of {2} "
                            "is returned"
                        ).format(
                            low["retry"]["attempts"],
                            low["retry"]["interval"],
                            low["retry"]["until"],
                            low["retry"]["splay"],
                        ),
                    ]
                )