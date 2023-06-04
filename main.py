import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_job_listings():
    base_url = "https://examplejobsite.com/jobs?page="


    with open("job_listings.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Job Title", "Company Name", "Location"])


        for page_num in range(1, 6):
            page_url = base_url + str(page_num)


            time.sleep(15)
            response = requests.get(page_url)
            soup = BeautifulSoup(response.content, "html.parser")


            job_listings = soup.find_all("div", class_="job-listing")

            for job in job_listings:
                title = job.find("h2", class_="job-title").text.strip()
                company = job.find("p", class_="company-name").text.strip()
                location = job.find("p", class_="location").text.strip()


                writer.writerow([title, company, location])

            print(f"Page {page_num} scraped successfully.")


    print("Scraping complete. Job listings saved to job_listings.csv.")

scrape_job_listings()
