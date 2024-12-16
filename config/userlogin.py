from seleniumbase import BaseCase
import os
import urllib.request
import speech_recognition as sr
import pydub
import time

class user(BaseCase):
  def loginapp(self, username, password):
    self.open ("https://frontend.elhkpn.devel.torche-indonesia.com")
    self.maximize_window()
    popup = "#cls-popup-lanppg"
    self.wait_for_element_present(popup)
    self.click(popup)

    self.input("#username", username)
    self.input("#password", password)

    input("selesaikanlah capctha itu!!!!!!!!")
    # self.sleep(5)
    # self.switch_to_frame("iframe[src*='recaptcha']")
    # self.sleep(5)
    # self.click('.recaptcha-checkbox-border')
    # self.sleep(5)
    # self.switch_to_default_content()
    # try:
    #   self.switch_to_frame(2)
    #   self.sleep(5)
    #   self.click('#recaptcha-audio-button')
    #   self.sleep(5)
    #   self.click('.rc-button-default.goog-inline-block')
    #   self.sleep(5)

    #   # directory = os.path.dirname(__file__)
    #   directory = os.getcwd()
    #   # os.makedirs(directory,exist_ok=True)
    #   # fullP = os.path.join(directory, "sample.mp3")

    #   src = self.get_attribute('#audio-source', 'src')
    #   print("[INFO] Audio src: %"%src)

    #   urllib.request.urlretrieve(src, directory+"\sample.mp3")
    #   # print(f"Full path: {fullP}")
    #   # print(f"Type of full path: {type(fullP)}")
    #   print(f"Current working directory: {os.getcwd()}")

    #   sound = pydub.AudioSegment.from_mp3(directory+"\sample.mp3")
    #   sound.export(directory+"\sample.wav", format="wav")

    #   sample_audio = sr.AudioFile(os.path.join(directory,"\sample.wav"))
    #   r = sr.Recognizer()

    #   with sample_audio as source:
    #     audio = r.record(source)

    #   key = r.recognize_google_cloud(audio)
    #   print("[INFO] Recaptcha Passcode : %s" %key)

    #   self.input('#audio-response',key.lower())
    #   self.click('#recaptcha-verify-button')
    # except:
    #   pass
    # self.switch_to_default_content()

    self.sleep(2)
    self.click("#sign-in")
    self.sleep(3)

    popup = "#cls-popup-lanppg"
    self.wait_for_element_present(popup)
    self.click(popup)
  
  def custom_wait_for_element(self, selector, timeout=10):
    start_time = time.time()
    while time.time() < start_time + timeout:
        if self.is_element_present(selector):
            return True
        time.sleep(1)
    raise Exception(f"Element {selector} not found within {timeout} seconds.")
    

