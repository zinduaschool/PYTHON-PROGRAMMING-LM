# Jumia Product Scraper
### Implement a products scrapper for Jumia Online Shop (Kenya). 
Data will always win, right? The internet is absolutely the go-to datasource as such calling for your web scraping skills. Factually, Web scraping/crawling, whatever you want to call it, is the **only** way we can gain access to data. This data is not easily found in your convenient CSV files or the normal tabular formats you are used to. As such to gain this you'll have to employ web scraping.

This project's focus is to help you extend skill acquired in class to scrape the local [Jumia online shop](https://jumia.co.ke/) using Python, Beutiful soup and requests (latter two are python libaries). You will be required to scrape links of products **from the deals of the week in the homepage**. After that, you'll create an algorithm to determine a products popularity and make recommendations to sellers about the type of products they ought to sell. For a similar but no so close scraping case, visit this [site](https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/) to learn more. 
#### Standard Programming Procedures.
For this case, the following deliverables should be achieved at bare minimum.
- Set up your python environment to have bs4 and requests libraries if not exists. Optionally, you might need pandas for data displaying but I'll recommend using csv library for this. 
- Recall on regular expression and make neccessry imports.
- Using requests, check whether the link to the [jumia site](https://jumia.co.ke/) can be scrapped.  Remember the status code and what each means. 
- Explore the page structure with chrome devtools to understand the product division you want to scrape.
- From there, you'll be tasked to collect the following information:
**(Note: products scrapped should be from the deals of the week section in the homepage)**
    ```
    i) Product Name
    ii) Brand Name
    iii) Price (Ksh)
    iv) Discount if Available (%)
    v) Total Number of Reviews
    vi) Product Rating (out of 5). 
    vii) Remaining Product Stock
    ```
 - Combine the data to a CSV file or rather a Pandas DataFrame for Analyis. 
   *-- Hint:Make use of all the concepts learnt from week 1 till now):---* 
   
  
#### Further Notes:
The following assumptions apply to help gain insights from the data.
```
1) Number of review has a correlation with the number of product purchase. This will help determine the popularity of a particular product.
2) The product rating does not quantify the actuall customer satisfaction given the disparity in review count. Thus, add one negative and one positive review to better estimate the customer satisfaction from a product **(Product Rating Algorithm)**.
```
##### Parting Shot.
I hope this clearly outlines the project's scope and what is expected from you.  

#### Happy Scraping. 
