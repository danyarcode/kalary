import requests,random,time,os



url_insta='https://www.instagram.com/accounts/login/ajax/'
head_insta={
            'authority': 'www.instagram.com',
            'method': 'POST',
            'path': '/accounts/login/ajax/',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7',
            'content-length': '277',
            'content-type': 'application/x-www-form-urlencoded',
           'cookie': 'ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'origin': 'https://www.instagram.com',
           'referer': 'https://www.instagram.com/accounts/login/',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
           'x-csrftoken': 'u27l2skXxXS3smNyYh7bYQ7GZeC39zq5',
           'x-ig-app-id': '936619743392459',
           'x-ig-www-claim': '0',
           'x-instagram-ajax': '7a3a3e64fa87',
           'x-requested-with': 'XMLHttpRequest'
        }
        
        
def cheker():
        global head_insta
        global url_insta
        moha = 0
        filer=input("list email :")
        
        filer=open(filer,"r").readlines()
        for x in filer:
        	u = x.strip()
        	data={
        'username': u,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
        	}
        	re = requests.post(url=url_insta,headers=head_insta,data=data).text
        	
        	if '"message":"There was an error with your request. Please try again."' in re:
        		print("EMAIL :{}".format(u))
        		
 
def email():
	a=input("name : ")
	filer=open("user.txt","w")
	for x in range(200):
		x="10394857102840194"
		x1=random.choice(x)
		x2=random.choice(x)
		x3=random.choice(x)
		x5=a+x1+x2+x3+"@yahoo.com"
		filer.write(x5+"\n")
#email()
cheker()
exit()
        
        