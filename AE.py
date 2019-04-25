#-------------------------------------------------------------------------------------------
# File        : AE.py
# Description : Analytics Engine is a collection of API's supporting Turing Process in
#customer screens at mobile end, Billing and Pricing Details etc. 
# Author      : Phani Kumar Dytha
# Copyright   : Copyright © BP International Ltd. 2018. All rights reserved.
#               No unauthorised copy, use or distribution of this code is permitted.
# Version     : V9.0
#-------------------------------------------------------------------------------------------

'''
Analytics Engine is currently hosting the following API's

1)Community Usage API: https://analytics.strala.energy

parameters required: ?cid &start_date &end_date

2)Customer historical Information: https://analytics.strala.energy

parameters required: ?cid &start_date &end_date

3)EnergyEquivalence: https://analytics.strala.energy

parameters required: ?inp

4)Home Energy Saving: https://analytics.strala.energy

parameters required ?cid &dt

5)Pricing Engine: https://analytics.strala.energy

parameters required: none

BillingDetails and EnergySaving are now moved to lambdas
Current Billing Details is currently scrapped

'''


import boto3


def Testaccount():
    return("This is just for testing if the scans can identify BP confidential information")