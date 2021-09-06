import random
import smtplib
import unittest
import csv, operator
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_user(self):
        driver = self.driver
        driver.get('http://mydocfam.com:4200/registro')
        driver.implicitly_wait(10) 
        
        lista = []
        with open('prueba.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
            if(x==0):
                x=x+1        
            else:
                #Variables
                correo = linea [0]
                contrasena = linea[1]
                nombre = linea [2]
                apellido_p = linea[3]
                apellido_m = linea [4]
                fecha= linea[5]
                sexo = linea[6]  
                telefono = linea [7]

                email = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[1]/input')
                password = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[2]/input')
                confirm_password = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[3]/input')
                name=driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[4]/input')
                first_name = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[5]/input')        
                last_name = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[6]/input')
                date = driver.find_element_by_id('date')
                number=driver.find_element_by_name('telefono')

                self.assertTrue(email.is_enabled()
                and password.is_enabled()
                and confirm_password.is_enabled()
                and confirm_password.is_enabled()
                and name.is_enabled()
                and first_name.is_enabled()
                and last_name.is_enabled())
        #select gender        
        
                select_sex = Select(driver.find_element_by_id('sexo')) 
        
                #generate new password
                # rando = random.randrange(10, 100)
                # passwordd = nombre[0:2] + correo [0:3] + fecha [0:2] + telefono [0:2]
                # print(password)

                email.send_keys(correo)
                password.send_keys(contrasena)
                confirm_password.send_keys(contrasena)            
                name.send_keys(nombre)
                first_name.send_keys(apellido_p)
                last_name.send_keys(apellido_m)
                date.send_keys(fecha)
                number.send_keys(telefono)

                select_sex.select_by_visible_text(sexo)
                driver.implicitly_wait(1)
            
                create_account = driver.find_element_by_xpath('//*[@id="container-princ"]/app-register/body/div/div/div/div[2]/div[10]/button')
                self.assertTrue(create_account.is_displayed() 
                and create_account.is_enabled())
                create_account.click()
                driver.implicitly_wait(2)

                accept_terms = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/button[2]')
                self.assertTrue(accept_terms.is_displayed() 
                and accept_terms.is_enabled())
                accept_terms.click()
                
                driver.implicitly_wait(4)

        

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'registro_usuario'))