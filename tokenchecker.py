import requests
import sys
from colorama import Fore, init
import pathlib
init()


def main():
    print(f'''
    ####################################
    #                                  #
    #   Discord Token Checker - {Fore.LIGHTRED_EX}Vito{Fore.RESET}   #
    #                                  #
    ####################################
    ''')
    if len(sys.argv) == 3:
        importedtokens = sys.argv[1]
        exportedtokens = sys.argv[2]

        filechecker = pathlib.Path(importedtokens)
        if filechecker.exists():
            print(f'[{Fore.CYAN}-{Fore.RESET}] Loaded {importedtokens}')
            with open(importedtokens) as f:
                tokens = f.readlines()
                for i in tokens:
                    token = i.rstrip()
                    req = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': token})
                    if req.status_code == 200:
                        print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Working token! Token: {token} saved in {exportedtokens}')
                        with open(exportedtokens, 'a') as writer:
                            writer.write(f'{token}\n')
                    else:
                        pass

        else:
            print(f'Couldnt locate {importedtokens}')
    else:
        print(f'{Fore.WHITE}Usage: py {sys.argv[0]} [tokens.txt] [validtokens.txt]')

main()