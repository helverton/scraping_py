from time import sleep
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



pathChrome = '#PATH/chromedriver_win32/chromedriver.exe'
email = '#EMAIL'
senha = '#PASSWORD'
data = datetime.now() - timedelta(minutes=28)
data2 = data.strftime("%d %B %Y %I:%M %p")


navegador = webdriver.Chrome(pathChrome)

def verifyElemnt(xPath, pathType):
    try:
        element = WebDriverWait(navegador, 10).until(
            lambda x: EC.presence_of_element_located((By.XPATH, xPath)) if pathType == 'html' else EC.presence_of_element_located((By.CSS_SELECTOR, xPath))
        )
        return True
    except:
        return False

def page1():
    navegador.get('https://app.pepperi.com/')
    sleep(10)

    if (verifyElemnt('#email', 'css')):
        campo_email = navegador.find_element_by_css_selector('#email')
        campo_email.send_keys(email)
        sleep(1)

        if (verifyElemnt('#nextBtn', 'css')):
            botao_proximo = navegador.find_element_by_css_selector('#nextBtn')
            botao_proximo.click()
            sleep(1)
            
            page2()
        else:
            page1()
    else:
        page1()


def page2():
    if (verifyElemnt('#password', 'css')):
        campo_senha = navegador.find_element_by_css_selector('#password')
        campo_senha.send_keys(senha)
        sleep(1)

        if (verifyElemnt('#loginBtn', 'css')):
            botao_entrar = navegador.find_element_by_css_selector('#loginBtn')
            botao_entrar.click()
            sleep(5)

            page3()
        else:
            print("F5")
            page2()
    else:
        navegador.quit()


def page3():
    navegador.get('https://app.pepperi.com/settings/home')
    sleep(5)

    navegador.get('https://app.pepperi.com/settings/00000-000-000-000-000000/OperationalDashboard')
    sleep(10)

    navegador.get('https://integration.pepperi.com/mgr/PluginSettings/OperationalDashboard?showMenu=true')
    sleep(5)

    navegador.get('https://integration.pepperi.com/mgr/PluginSettings/TransactionLogs')
    sleep(5)


    if (verifyElemnt('#searchFromDate_DateTimePicker', 'css')):
        navegador.find_element_by_css_selector('#searchFromDate_DateTimePicker').clear()
        hora = navegador.find_element_by_css_selector('#searchFromDate_DateTimePicker')
        hora.send_keys(data2)
        sleep(4)

        page4()
    else:
        print("F5")


def page4():

    if (verifyElemnt('//*[@id="k-block"]/div[2]/div[2]/div/table/thead/tr/th[9]/a', 'html')):
        opcao = navegador.find_element_by_xpath('//*[@id="k-block"]/div[2]/div[2]/div/table/thead/tr/th[9]/a')
        opcao.click()
        sleep(2)


        if (verifyElemnt('/html/body/div[11]/div/ul/li[3]/span', 'html')):
            opcao2 = navegador.find_element_by_xpath('/html/body/div[11]/div/ul/li[3]/span')
            opcao2.click()
            sleep(2)


            if (verifyElemnt('/html/body/div[11]/div/ul/li[3]/div/ul/li/div/form/div/span[2]/span/span[1]', 'html')):
                opcao3 = navegador.find_element_by_xpath('/html/body/div[11]/div/ul/li[3]/div/ul/li/div/form/div/span[2]/span/span[1]')
                opcao3.click()
                sleep(2)

                
                if (verifyElemnt('/html/body/div[11]/div/ul/li[3]/div/ul/div[2]/div/div[3]/ul/li[2]', 'html')):
                    failure = navegador.find_element_by_xpath('/html/body/div[11]/div/ul/li[3]/div/ul/div[2]/div/div[3]/ul/li[2]')
                    failure.click()
                    sleep(2)

                    if (verifyElemnt('/html/body/div[11]/div/ul/li[3]/div/ul/li/div/form/div/div[2]/button', 'html')):
                        filtrar = navegador.find_element_by_xpath('/html/body/div[11]/div/ul/li[3]/div/ul/li/div/form/div/div[2]/button')
                        filtrar.click()
                        sleep(3)

                        if (verifyElemnt('/html/body/div[2]/span[2]/button', 'html')):
                            resubmited = navegador.find_element_by_xpath('/html/body/div[2]/span[2]/button')
                            resubmited.click()
                            sleep(2)

                            if (verifyElemnt('/html/body/div[4]/div[2]/div[3]/button', 'html')):
                                ok = navegador.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/button')
                                ok.click()
                                sleep (5)

                                navegador.quit()
                            else:
                                print("F5")
                                page4()
                        else:
                            print("F5")
                            page4()
                    else:
                        print("F5")
                        page4()
                else:
                    print("F5")
                    page4()
            else:
                print("F5")
                page4()
        else:
            print("F5")
            page4()
    else:
        print("F5")
        page4()


page1()