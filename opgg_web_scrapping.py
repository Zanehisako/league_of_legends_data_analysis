from concurrent.futures import ProcessPoolExecutor
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




regions= ['na','euw','me','eune','oce','kr','jp','br','las','lan','ru','tr','sg','ph','tw','vn','th']
ranks = ['iron','bronze','silver','gold','platinum','emerald','diamond','master','grandmaster','challenger']

# Initialize the webdriver 
def getStats(region,tier,driver):

    stats_df = pd.DataFrame()
    
    
    try:
        # Navigate to your page
        driver.get(f"https://www.op.gg/statistics/champions?tier={tier}&region={region}")
    
        # Wait for the table to load (adjust timeout as needed)
        wait = WebDriverWait(driver, 60)  # waits up to 10 seconds
        table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-1o9zu66")))
    
        # Now get all td elements
        td_elements = table.find_elements(By.TAG_NAME, "td")
        
        # Extract text from each td
        for i in range(0,len(td_elements)-1,9):
            stats = {
                'Popularity':td_elements[i].text,'Champion':td_elements[i+1].text,'Games Played':td_elements[i+2].text.replace(',',''),'KDA':td_elements[i+3].text.replace(':1',''),'Win rate':td_elements[i+4].text.replace('%',''),'Pick rate':td_elements[i+5].text.replace('%',''),'Ban rate':td_elements[i+6].text.replace('%',''),'CS':td_elements[i+7].text,'Gold':td_elements[i+8].text.replace(',',''),'Region':region,'Rank':tier
            }
            stats_df = pd.concat([stats_df,pd.DataFrame([stats])],ignore_index=True)
        stats_df.to_csv(f"champions_stat_{region}_{tier}.csv",index=False)
    
    
    except Exception as e:
        print(f"An error occurred: {e}")

    
def getStatsAllRegionsRanks(regions_f,rank):
    print("started getting All Regions and ranks stats")
    driver = webdriver.Firefox()
    for region in regions_f:
        for rank in ranks:
            getStats(region=region,tier=rank,driver=driver)

    driver.quit()

if __name__ == "__main__":
    print(regions[:4])
    print(regions[4:9])
    print(regions[9:13])
    print(regions[13:])
    with ProcessPoolExecutor() as executor:
        future1 = executor.submit(getStatsAllRegionsRanks,regions[:4],ranks)
        future2 = executor.submit(getStatsAllRegionsRanks,regions[4:9],ranks)
        future3 = executor.submit(getStatsAllRegionsRanks,regions[9:13],ranks)
        future4 = executor.submit(getStatsAllRegionsRanks,regions[13:],ranks)
        
