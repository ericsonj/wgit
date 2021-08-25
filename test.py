# Python3 code to demonstrate working of
# Check if string matches regex list
# Using join regex + loop + re.match()
# import re

# def getIndex(test, lst: list):
#     if test in lst:
#         return lst.index(test)
#     else:
#         for l in lst:
#             if re.match(l, test):
#                 return lst.index(l)
#     return None

# # initializing list 
# test_list = ["gitlab.*", "gitlab_surix", "gitlab_ericson|joseph"]
# test_list = sorted(test_list, key=len, reverse=True)

# print(test_list)

# test = "gitlab_ericson"

# print(getIndex(test, test_list))

from pathlib import Path
import json
import re

HOME = str(Path.home())
WGIT_CONFIG_FOLDER = f"{HOME}/.config/wgit/accounts.json"

def _getKeyMatched(test, lst: list):
    if test in lst:
        return test
    else:
        for l in lst:
            if re.match(l, test):
                return l
    return None

def get_config_profile(profile):
    accounts_dict = {}
    with open(WGIT_CONFIG_FOLDER, 'r') as file:
        accounts = json.load(file)
        if not isinstance(accounts, list):
            return None
        for account in accounts:
            if 'host_owners' in account and isinstance(account['host_owners'], list):
                for host_owner in account['host_owners']:
                    accounts_dict[host_owner] = account
    key = _getKeyMatched(profile, list(accounts_dict.keys()))
    return accounts_dict[key]

print(get_config_profile("gitlab_ericson"))