import json
inpit = input('Stock Ticker:')
inpit = {'ticker':inpit}
inpit = json.dumps(inpit)
with open('BigBoyProj\Stocks\localdata.txt', 'w') as op:
    op.write(inpit)
    op.close()


import api