import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#initial dataframe to store the champions stats
columns = ['Popularity','Champion','Games Played','KDA','Win rate','Pick rate','Ban rate','CS','Gold']
stats_df = pd.DataFrame(columns=columns)

# Initialize the webdriver 
driver = webdriver.Firefox()

try:
    # Navigate to your page
    driver.get("https://www.op.gg/statistics/champions")

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
    print(stats_df)
    stats_df.to_csv("Champion_stats.csv",index=False)


except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()
