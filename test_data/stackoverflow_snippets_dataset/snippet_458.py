# Extracted from https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
async def get_local_ip():
    loop = asyncio.get_event_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        asyncio.DatagramProtocol,
        remote_addr=('8.8.8.8', 80))
    result = transport.get_extra_info('sockname')[0]
    transport.close()
    return result

