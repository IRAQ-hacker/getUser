import requests
import secrets
import sys as n
import os , sys
import time as mm
from time import sleep
os.system("clear")

rreku= '\033[1;32m'
freku = '\033[1;33m'
qreku = '\033[1;36m'
reku_h = '\033[1;31m'
rekugr='\033[0;32m'
rekupr='\033[0;35m'
rekucy='\033[0;36m'
rekuyel='\033[0;33m'

print(qreku+'•'*50)

reku_ban=f"""
{rreku}
|¯ | | |¯ |/    /¯\ |  |  {freku}
|¯ |_| |_ |¯\   |¯| |_ |_    {qreku} Fuck all cuppy paste !
                  
"""

print(reku_ban)
print(qreku+'•'*50)
print ("""
1- Get The hashtag (: 
2- join for youtube channel (:
3- join for  telegram channel (: 

""")
x = input('Choose a department : ')

if x=='1':
	os.system("clear")


	print(qreku+'•'*50)
	print(reku_ban)
	print(qreku+'='*50)
	head = {
	'HOST': "www.instagram.com",
	'KeepAlive' : 'True',
	'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
	'Cookie': 'cookie',
	'Accept' : "*/*",
	'ContentType' : "application/x-www-form-urlencoded",
	"X-Requested-With" : "XMLHttpRequest",
	"X-IG-App-ID": "936619743392459",
	"X-Instagram-AJAX" : "missing",
	"X-CSRFToken" : "missing",
	"Accept-Language" : "en-US,en;q=0.9"
	}
	
	reku = requests.Session()
	rekushe = '''
	
	Hey hackers , please Enter Your One HashTag : fot clone .
	
	
	'''
	
	print(rekushe)
	# Fo Ent Hash Clone Accoun
	
	
	rc1 = input('The first hashtag : '+reku_h)
	rc2 = input('The second hashtag : '+qreku)
	rc3 = input('The third hashtag :'+rekugr)
	rc4 = input('The fourth hashtag : '+rekupr)
	rc5 = input('The fifth hashtag : '+rekucy)
	rc6 = input('The sixth hashtag : '+rekuyel)
	fileuser = open('User.txt', 'a')
	
	print('~'*50)  #for print ~ 50 ;
	def reku1():
		try:
			url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{rc1}'
			mn = 0
			req_id = reku.get(url_id,headers=head).json()		
			while True:
				mn+=1			
				y = str(req_id['users'][mn]['user']['username'])
				fileuser.write(y + '\n')
				
				print(f'{y}')
		except Exception as e:
	           
	            print('~'*50)
	     
	reku1()
	
	#claf Rek1
	def reku2():
		try:
			url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{rc2}'
			mn = 0
			req_id = reku.get(url_id,headers=head).json()		
			while True:
				mn+=1			
				y = str(req_id['users'][mn]['user']['username'])
				fileuser.write(y + '\n')
				print(f'{y}')
		except Exception as e:
	            
	            print('~'*50)
	     
	reku2()	
	#Tgf
	def reku3():
		try:
			url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{rc3}'
			mn = 0
			req_id = reku.get(url_id,headers=head).json()		
			while True:
				mn+=1			
				y = str(req_id['users'][mn]['user']['username'])
				fileuser.write(y + '\n')
				print(f'{y}')
		except Exception as e:
	            
	            print('~'*50)
	     
	reku3()
	#Smail
	def reku4():
		try:
			url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{rc4}'
			reku = 0
			req_id = reku.get(url_id,headers=head).json()		
			while True:
				mn+=1			
				y = str(req_id['users'][mn]['user']['username'])
				fileuser.write(y + '\n')
				print(f'{y}')
		except Exception as e:
	           
	            print('~'*50)
	     
	reku4()
	#Ex Rc
	def reku5():
		try:
			url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{rc5}'                                                                                                      #ريكو
			mn = 0
			req_id = reku.get(url_id,headers=head).json()		
			while True:
				mn+=1			
				y = str(req_id['users'][mn]['user']['username'])
				fileuser.write(y + '\n')
				print(f'{y}')
		except Exception as e:
	           
	            print('~'*50)
	     
	reku5()			
	#facke
	def reku6():
		try:
			url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{rc6}'
			mn = 0
			req_id = reku.get(url_id,headers=head).json()		
			while True:
				mn+=1			
				y = str(req_id['users'][mn]['user']['username'])
				fileuser.write(y + '\n')
				print(f'{y}')
		except Exception as e:
		        print('~'*50)
		        print(u'The examination is over')
		        print(u' Saved in User.txt ')
		        print('~'*50)
	          
	reku6()			
if x=='2':
	os.system('xdg-open https://youtube.com/راشدكريم')
if x=='3':
	os.system('xdg-open https://t.me/Professional_school')

#صمم مو تخمط شغل غيرك اداة صايره قديمه الي خامطهه ليش ابن طلي ؟
#المهم طور براحتگ بس كول فلان تعب بيها خل اذكر بس اسمه ع اقل
