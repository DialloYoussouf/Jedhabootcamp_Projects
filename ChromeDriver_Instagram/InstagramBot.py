import os
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

class InstagramBot:
    """ 
    
    Class InstagramBot("username", "password")
        
    
    """
    
    def __init__(self, username, password):
        """
        
        Initiallize an instance of class InstagramBot
        Call login method for autentification
        
            Args: 
                str(username): The instagram username or email_adress
                str(password): The instagram password
            
            Attribute:
                selenium.webdriver.driver.Chrome(): The Chromedriver used to automate browser actions on Instgram.com 
            
            
        
        """
        
        self.username = username
        self.password = password
        
        self.Keys = Keys.RETURN
        
        self.driver = webdriver.Chrome()
        
        
        
        self.base_url = "https://www.instagram.com/"
        
        self.login()
        
        
    def login(self):
        """
        login method called while class InstagramBot instance initialization
        
            Attribute:
        
                The Chromedriver will get to Instagram web site:

                    login with the username and passorwd provided and then click on 'Connexion' button

                        Click on 'Plus tard' button for Saving login Information

                        Click on 'Yes' button for Turn On Notification 
                    
        
        """
        
        self.driver.get('{}'.format(self.base_url))
        time.sleep(1/3)
        
            #Enter username
        self.driver.find_element_by_name('username').send_keys(self.username)
        
            #Enter password then push Enter  
        self.driver.find_element_by_name('password').send_keys(self.password, self.Keys)
        time.sleep(2)
        
        try:
                #Saving login Information ==> Click on 'Not Now' button
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
            time.sleep(1)

        except:
            pass

        try:
                #Turn On Notification ==> Yes
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
            time.sleep(1)

        except:
            pass

        
       
    def nav_hashtag(self, hashtag, Follow_hashtag=True):
        """
        nav_hashtag method of class InstagramBot:
            navigate through hashtag's profile
            
            Args: 
                str(hashtag): Instagram hashtag
                bool(Follow_hashtag): Following Instagram hashtag
                
            
            Attribute:
                
                The Chromedriver will get to the instagram page of the hashtag provided:
                    if Follow_hashtag == True:
                        click on Follow button
                    else :
                        pass
                        
                    Scroll down page ten times
            

        call user_photos_ref method of class InstagramBot
            
        
        """
        
        self.hashtag = hashtag
        self.Follow_hashtag = Follow_hashtag
        
        self.driver.get('{}explore/tags/{}'.format(self.base_url, self.hashtag))
        
            #Push Follow button
        if Follow_hashtag == True:
            time.sleep(3)
            try:
                self.driver.find_element_by_css_selector('button.sqdOP.L3NKy._4pI4F.y3zKF').click()

            except:
                pass
        else:
            pass
            
            # Scrolling down page
        for i in range(1,10):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            
        self.user_photos_ref()

        
        
        
       
            
            
    def nav_user(self, user, Follow_user):
        """
        nav_user method of class InstagramBot:
            navigate through user's profile
        
            Args: 
                str(user): Instagram username
                bool(Follow_user): Following Instagram user
            
            Attribute:
                
                The Chromedriver will get to the instagram page of the username provided:
                
                   if Follow_user == True:
                        click on Follow button
                        
                    else :
                        pass 
    
                    Scroll down page ten times
                    
        call user_photos_ref method of class InstagramBot:


        """
        self.user = user
        self.Follow_user = Follow_user
        self.driver.get('{}{}/'.format(self.base_url, self.user))
        
        
        if Follow_user==True:
            time.sleep(3)
            try:
                self.driver.find_element_by_css_selector('button._5f5mN.jIbKX._6VtSN.yZn4P').click()

            except:
                pass
            
        else:
            pass
        

        for i in range(1,10):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            
        self.user_photos_ref()

   
        
    def user_photos_ref(self):
        """
        user_photos_ref method of class InstagramBot:
            gathering hashtag's or user's photos references (links url) in the photos_profile attribute
            
        method called automatically by nav_hashtag and nav_user method of class InstagramBot
        
        """
        
        
        self.photos_profile = []

        photos_tag = self.driver.find_elements_by_tag_name("a")

        photos_hrefs = [photo.get_attribute('href') for photo in photos_tag if ".com/p/" in photo.get_attribute('href')] 

        [self.photos_profile.append(href) for href in photos_hrefs if href not in self.photos_profile]

        

        
    def view_photo_profile(self, Like=False, Save_Photo_comments=False):
        """
        view_photo_profile method of class InstagramBot:
            Args:
                bool(Like) : Like Hashtag's or user Instagram's photos
                bool(Save_Photo_comments): Save All photos comments in the attribute photo_all_comments
                
            Attribute:
                
                The Chromedriver will get to the instagram page of the username or hashtag provided previsiouly:
                    loop through all photos:
                
                        if Like == True:
                            Like all photos

                        else :
                            pass 

                        if Save_Photo_comments == True:
                            Save all Photos comments in the photo_all_comments attribute (list())
                            
                        else:
                            pass  
        
        """
        
        #self.photos_profile_indices = []
        #self.comment_text_indices = []
        self.Like = Like
        self.Save_Photo_comments = Save_Photo_comments
        self.photo_all_comments = []
        self.photo_date = []

        for x, y in enumerate(self.photos_profile):
            self.driver.get(y)
            time.sleep(7)
            
            
            
            if Like==True:
                
                
        
                    #like button
                like = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                like.click()
                time.sleep(3)
                #self.photos_profile_indices.append(x)
            
            else:
                pass

            
            if Save_Photo_comments==True:
                #time.sleep(1)
                photo_comments_span = self.driver.find_elements_by_tag_name('span')
                
                all_photo_comments = [com.text for com in photo_comments_span if com.text != '']
                photo_date = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[2]/a/time').text


                #time.sleep(1)
                self.photo_all_comments.append(all_photo_comments)
                self.photo_date.append(photo_date)
                print(photo_date)
                print(all_photo_comments)
                print()
                #time.sleep(1)
                
            else:
                pass
            

            if x>len(self.photos_profile):
                break


                
                
                
                
                
            
            
    def download_photos(self):
        """
        download_photos method of class InstagramBot:
            Args: None

            Attribute:
                
                The Chromedriver will get to the instagram page of the username or hashtag provided:
                    loop through all photos:
                        download each one of them on a Image folder in local machine
                        copy Image url in the photo_url attribute
        CAUTION:  
            THIS METHOD MUST BE CALLED AFTER INITALISATION OF THE nav_hashtag OR nav_user METHOD 
        """
        
        
        try:
            os.mkdir('Image')
        except FileExistsErrors:
            print("le dossier Image existe déjà, veuillez le supprimer au préalable avant d'appeler cette method!")
            pass
        count = 0
        photos_url = []
        
        for url in self.photos_profile:
            self.driver.get(url)
            time.sleep(6)
            
            
            
            src = self.driver.find_element_by_css_selector('img.FFVAD').get_attribute('src')
            
            
            try:    
                if src != None:
                    src = str(src)
                    photos_url.append(src)
                    print(src)
                    print()
                    count+= 1
                    urllib.request.urlretrieve(src, os.path.join('Image', str(self.hashtag)+'_'+str(count)+'.jpg'))
                    #urllib.request.urlretrieve(src, os.path.join('Image', str(self.user)+'_'+str(count)+'.jpg'))



                else:

                    continue
                    
            except AttributeError:
                
                urllib.request.urlretrieve(src, os.path.join('Image', str(self.user)+'_'+str(count)+'.jpg'))
                

        self.photos_url = photos_url
        
        
    def quit(self):
        """
        To quit the Chromedriver and close window
        """
        
        self.driver.quit()
    
        