# Security Score Calculator

## Overview

The **Security Score Calculator** is a Streamlit-based web application designed to calculate security scores for a list of IP addresses by scraping data from the VirusTotal website. The application allows users to upload a CSV or Excel file containing IP addresses, processes the data, and retrieves security scores using a custom web scraper. The updated data, including the security scores, can then be downloaded as a CSV file.

## Features

- **File Upload**: Users can upload CSV or Excel files containing IP addresses.
- **Data Processing**: The application processes the uploaded file and extracts the IP addresses.
- **Web Scraping**: The application uses Playwright to scrape security scores from the VirusTotal website.
- **Multiprocessing**: The scraping process is handled in a separate process to avoid blocking the main application.
- **Data Download**: Users can download the updated data, including the security scores, as a CSV file.

## Installation

To run the application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/security-score-calculator.git
   cd security-score-calculator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload a File**: 
   - Click on the "Upload the file here" section and upload a CSV or Excel file containing IP addresses.

2. **Scrape Data**:
   - After uploading the file, click the "Scrap Data" button to start the scraping process.

3. **Download Updated Data**:
   - Once the scraping is complete, the updated data with security scores will be displayed. You can download this data as a CSV file by clicking the "Download" button.

## Code Structure

- **app.py**: The main Streamlit application script.
- **dataframe.py**: Contains the `ExtractData` class for reading and processing CSV/Excel files.
- **scraper.py**: Contains the `CustumScraper` class for scraping security scores from VirusTotal.
- **logger.py**: Handles logging for the application.

## Disclaimer

**Important**: Web scraping may violate the terms of service of some websites. This application is provided for **educational purposes only**. The developers of this application do not condone or encourage the use of web scraping in violation of any website's terms of service. Users are solely responsible for ensuring that their use of this application complies with all applicable laws and website policies.

The VirusTotal website, in particular, has strict terms of service regarding automated access and scraping. Please review their [terms of service](https://www.virustotal.com/gui/terms-of-service) before using this application. Unauthorized scraping of their website may result in legal action or being blocked from accessing their services.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Support

For any questions or issues, please open an issue on the GitHub repository.

---

**Note**: This application is intended for educational purposes only. Use it responsibly and ensure compliance with all applicable laws and website policies.
