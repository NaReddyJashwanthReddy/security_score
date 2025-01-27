from playwright.sync_api import sync_playwright
from logger import logging

class CustumScraper:

    def __init__(self):
        pass

    def DataRetrive(self, page, data_1):
        logging.info("enter the try block in DataRetriver")
        try:
            # Navigate to the URL
            page.goto(f"https://www.virustotal.com/gui/ip-address/{data_1}/summary", timeout=60000)
            logging.info(f"Navigated to {data_1}")

            # Wait for the element to be attached to the DOM
            page.wait_for_selector('#positives', state='attached', timeout=30000)
            logging.info("Element found")

        except Exception as e:
            logging.info(f"Error retrieving data for {data_1}: {e}")
            return None

        # Extract the element
        element = page.query_selector("#positives")
        logging.info("element querried")
        if element:
            text_content =  element.inner_text()
            logging.info(f"Data for {data_1}: {text_content}")
            return text_content
        else:
            logging.info(f"Element not found for {data_1}")
            return None

    def applying(self, data):
        logging.info("Starting data retrieval")
        with sync_playwright() as p:
            # Launch the browser
            browser =  p.chromium.launch(headless=True)
            page =  browser.new_page()
            logging.info("browser opened")
            # Apply the DataRetrive method to each row in the DataFrame
            new_data = data.apply(lambda x: self.DataRetrive(page,x))

            # Close the browser
            browser.close()
            logging.info("Browser closed")

        return new_data.values.tolist()

    

