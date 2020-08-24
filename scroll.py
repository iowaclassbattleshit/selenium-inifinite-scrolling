import time

# driver: the webdriver used for the scraping
# timeout: the amount of time (in seconds) the script will wait to scroll to the bottom again
# maxBumps: the amount of times the script will retry scrolling to the bottom
# callback: the callback function signalling the end of the script execution

def scroll(driver, timeout, maxBumps, callback=None):
    bumps = 0
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(timeout)

        new_height = driver.execute_script("return document.body.scrollHeight;")

        if new_height == last_height:
            bumps = bumps + 1
            print(f"Bottom reached, bumped {bumps}/{maxBumps} times.")
            if bumps == maxBumps:
                print(f"{bumps}/{maxBumps} bumps have been reached, quitting.")
                if callback is not None:
                    callback(driver)
                break
        else:
            print(f"scrolling can continue")
            last_height = new_height
            bumps = 0