import streamlit as st
import pandas as pd
from dataframe import ExtractData
from scraper import CustumScraper
from multiprocessing import Process,Queue
from logger import logging
import time

def run_scrap(data,queue):
    logging.info("create class WebScrap")
    WebScrap=CustumScraper()
    logging.info("Using applying functio")
    new_data=WebScrap.applying(data)
    logging.info("applying function Done ")
    queue.put(new_data)
    logging.info("queue.put done")

st.title("SECURITY SCORE CALCULATOR")

st.header("Upload the file here: ")

logging.info("Requested to upload file")


upload_file=st.file_uploader("upload file",type=["csv","xlsx"])

logging.info("File uploaded")

if upload_file is not None:

    if upload_file.name.endswith(".csv"):
        file_type="CSV"
        
        logging.info("Given CSV file")

    elif upload_file.name.endswith('.xlsx'):
        file_type="EXCEL"
        
        logging.info("Given EXCEL file")

    else:
        st.error("Unsupported file type. Please upload a CSV or Excel file.")
        logging.info("Uploaded file in wrong format")
        st.stop()

    logging.info("Ready to extract data and sent to ExtractData liberary")

    data=ExtractData()
    df=data.ReadData(upload_file,file_type)
    df=df[df.columns[0]][:3]
    logging.info("data has been prepared")

    st.success(f"Uploaded file successfully : {upload_file.name}") 

    if st.button("scrap data"):

        logging.info("Pressed button")

        queue=Queue()
        logging.info("queue has been created")
        process=Process(target=run_scrap,args=(df,queue))
        logging.info("process Done")
        process.start()
        logging.info("process.start done")
        process.join()
        logging.info("process.join done")
        new_data=queue.get()
        logging.info("got the new_data")
        st.write("scraped data")
        new_data=pd.DataFrame(new_data,columns=['Score'])
        df_concat=pd.concat([df,new_data],axis=1)

        st.write(df_concat)

        st.write('### Download Updated Data')
        csv=df_concat.to_csv(index=False)
        st.download_button(
            label="Download",
            data=csv,
            file_name="IPScoreReport.csv"
        )

if __name__=="__main__":
    pass








