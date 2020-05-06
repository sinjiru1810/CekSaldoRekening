from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

info_login = {
    'username': '<user ID klik bca anda>',
    'password': '<pin klik bca anda>'
}


#xpath html yang sudah di inspek
xpath = {
    'info_saldo': '//table[1]/tbody/tr[1]/td[2]/table[1]/tbody/tr[4]/td[1]/table[1]/tbody/tr[1]/td[2]/font/a', #xpath menu bar kiri
    'rekening'  : '/html/body/table[3]/tbody/tr[2]/td[1]/div/font',
    'jenis'     : '/html/body/table[3]/tbody/tr[2]/td[2]/div/font',
    'matauang'  : '/html/body/table[3]/tbody/tr[2]/td[3]/div/font',
    'saldo'     : '/html/body/table[3]/tbody/tr[2]/td[4]/div/font', #xpath value saldo
}

#membuka browser
br = webdriver.Chrome('/home/sinjirusetyawan/Downloads/chromedriver')

#buka web, tunggu 1 detik agar semua selesai load, lanjut
br.get('https://ibank.klikbca.com/authentication.do?value(actions)=logout')
time.sleep(0.5)

#agar bisa kontrol pindah tab
br.window_handles

#mencari elemen form login
username_input = br.find_element_by_id('user_id')
password_input = br.find_element_by_id('pswd')
login_button = br.find_element_by_name('value(Submit)')

#mengisi form login
username_input.send_keys(info_login['username'])
password_input.send_keys(info_login['password'])
login_button.click()

br.get('https://ibank.klikbca.com/nav_bar_indo/account_information_menu.htm') #membuka navbar kiri bca

#cari dan klik info saldo utk buka halaman info saldo
saldo = br.find_element_by_xpath(xpath['info_saldo']) 
saldo.click()

#otomatis buka ke tab baru, suruh webdriver pindah tab
br.find_element_by_tag_name('body').send_keys(Keys.CONTROL + "2")
br.switch_to.window(br.window_handles[-1])

#cari eelemen berisi nilai saldo dan dicetak
norek = br.find_element_by_xpath(xpath['rekening'])
jenis = br.find_element_by_xpath(xpath['jenis'])
matauang = br.find_element_by_xpath(xpath['matauang'])
saldo = br.find_element_by_xpath(xpath['saldo'])
print("NO REK     : ",norek.text)
print("JENIS REK  : ",jenis.text)
print("MATA UANG  : ",matauang.text)
print("SALDO ANDA :  Rp. ",saldo.text)

#tutup browser
#ActionChains(br).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('w').key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()
br.quit()
