from concurrent.futures import ProcessPoolExecutor
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#initial dataframe to store the champions stats
columns = ['Popularity','Champion','Games Played','KDA','Win rate','Pick rate','Ban rate','CS','Gold']

# Initialize the webdriver 
def getStats(url,filename,driver):

    stats_df = pd.DataFrame(columns=columns)
    
    
    try:
        # Navigate to your page
        driver.get(url)
    
        # Wait for the table to load (adjust timeout as needed)
        wait = WebDriverWait(driver, 5)  # waits up to 10 seconds
        table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-1o9zu66")))
    
        # Now get all td elements
        td_elements = table.find_elements(By.TAG_NAME, "td")
        
        # Extract text from each td
        for i in range(0,len(td_elements)-1,9):
            stats = {
                'Popularity':td_elements[i].text,'Champion':td_elements[i+1].text,'Games Played':td_elements[i+2].text,'KDA':td_elements[i+3].text,'Win rate':td_elements[i+4].text,'Pick rate':td_elements[i+5].text,'Ban rate':td_elements[i+6].text,'CS':td_elements[i+7].text,'Gold':td_elements[i+8].text
            }
            stats_df = pd.concat([stats_df,pd.DataFrame([stats])],ignore_index=True)
        stats_df.to_csv(filename,index=False)
    
    
    except Exception as e:
        print(f"An error occurred: {e}")

    
def getStatsAllRegions():
    print("started getting All Regions stats")

    driver = webdriver.Firefox()
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=na","champions_stat_na.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=euw","champions_stat_euw.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=me","champions_stat_me.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=kr","champions_stat_kr.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=eune","champions_stat_eune.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=oce","champions_stat_oce.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=jp","champions_stat_jp.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=br","champions_stat_br.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=las","champions_stat_las.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=lan","champions_stat_lan.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=ru","champions_stat_ru.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=tr","champions_stat_tr.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=sg","champions_stat_sg.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=ph","champions_stat_ph.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=tw","champions_stat_tw.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=vn","champions_stat_vn.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=th","champions_stat_th.csv",driver)
    driver.quit()

def getStatsAllRanks():
    print("started getting All Ranks stats")
    driver = webdriver.Firefox()
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=iron","champions_stat_iron.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=bronze","champions_stat_bronze.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=silver","champions_stat_silver.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=gold","champions_stat_gold.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=platinum","champions_stat_platinum.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=emerald","champions_stat_emerald.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=diamond","champions_stat_diamond.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=master","champions_stat_master.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=grandmaster","champions_stat_grandmaster.csv",driver)
    getStats("https://www.op.gg/statistics/champions?mode=ranked&region=global&tier=challenger","champions_stat_challenger.csv",driver)

    driver.quit()

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        future1 = executor.submit(getStatsAllRegions)
        future2 = executor.submit(getStatsAllRanks)
        
