from xmodule import *

@mark.feElkhpn
def testconfigandlogin():
    global driver
    driver = initDriver()
    login_admin(driver)

tambahagamatxt = 'Pendidikan Bagus'
ubahagamatxt= 'Pendidikan ga bagus'


def test_create_educations():
  driver.get("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/master/educations")
  sleep(driver)
  driver.find_element(By.ID, 'educations-button-page-create').click()
  driver.find_element(By.ID, 'educations-input-text-nama').send_keys(tambahagamatxt)
  driver.find_element(By.ID, 'educations-button-modal-create').click()
  sleep(driver)
def test_serch_agama():
  sleep(driver)
  srch = driver.find_element(By.ID, 'educations-input-page-search-by-keyword')
  srch.click()
  srch.send_keys(tambahagamatxt)
  pyautogui.press('enter')
  sleep(driver)
def test_update_agama():
  sleep(driver)
  driver.find_element(By.ID, 'educations-button-row-edit-0').click()
  sleep(driver)
  updagama = driver.find_element(By.ID, 'educations-input-text-nama')
  updagama.click()
  updagama.clear()
  updagama.send_keys(ubahagamatxt)
  driver.find_element(By.ID, 'educations-button-modal-edit').click()
  sleep(driver)
def test_serch_clear_agama():
  sleep(driver)
  srch = driver.find_element(By.ID, 'educations-input-page-search-by-keyword')
  srch.clear()
  srch.send_keys(ubahagamatxt)
  pyautogui.press('enter')
  sleep(driver)
def test_delete_agama():
  sleep(driver)
  driver.find_element(By.ID, 'educations-button-row-delete-0').click()
  sleep(driver)
  driver.find_element(By.ID, 'educations-button-modal-delete').click()
  sleep(driver)
def test_serch1_clear():
  sleep(driver)
  driver.refresh()
  sleep(driver)