import os


#edit this part
hosts = [
        'wish-dating-sudden-welfare.trycloudflare.com',
        'albuquerque-hu-ability-disturbed.trycloudflare.com'
        ]

walletID = '0xC4fD61000DFFf9B16B3621916473A124503762ED'
email = 'cominlooks@gmail.com'
password = 's'




hosts = ' '.join(hosts)

os.system("chmod u+x ./bs2/bs2")
os.system("./bs2/bs2 -ho " + str(hosts) + " -w " + str(walletID) + " -e " + str(email) + " -p " + str(password))