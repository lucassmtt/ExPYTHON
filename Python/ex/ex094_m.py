def confirma_int():
    while True:
        resp = input('Digite algo')
        if resp.isnumeric():
            int(resp)
            break
    return resp

num = confirma_int()